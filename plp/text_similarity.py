from json import dumps
from json import loads
from os import mkdir
from os.path import join, isfile

from gensim.models.doc2vec import Doc2Vec as gensim_document_to_vector
from gensim.models.doc2vec import TaggedDocument
from scipy import spatial

from .setting import PARENT_BASE_DIR
from .extractor import Keywords, Stopwords
from .loader import files2pylist
from .persian_pre_processing import TripleP

from logging import debug
from time import time


class Similarity:
    def __init__(self, data_path: str = None, exist_tags: bool = False):
        self.stpwrds = Stopwords()
        self.kywrds = Keywords(self.stpwrds.STOPWORDSLIST)
        self._load_data(data_path)
        self.exist_tags = exist_tags
        self._load_tags(data_path)
        self._documents2vectors()

    @property
    def data(self):
        file_name = join(PARENT_BASE_DIR, '.files', 'data.data.json')
        if isfile(file_name):
            debug(f'{file_name} file is exist.')
            debug(f'try for load {file_name} file ->->->->->->->->->->')
            start_load_file = time()
            with open(file_name, 'r', encoding='utf-8')as file:
                data = file.read()
                data = loads(data)
            debug(f'load file - [runtime: {time() - start_load_file}] <-<-<-<-<-<-<-<-<-<-')
            return data, 'data exist.'
        else:
            debug(f'{file_name} file is not exist.')
            return None, 'data not exist in "base directory/.files/data.data.json"'

    @property
    def tags(self):
        if not self.exist_tags:
            return [], ''
        file_name = join(PARENT_BASE_DIR, '.files', 'tags.data.json')
        if isfile(file_name):
            debug(f'{file_name} file is exist.')
            debug(f'try for load {file_name} file ->->->->->->->->->->')
            start_load_file = time()
            with open(file_name, 'r', encoding='utf-8')as file:
                data = file.read()
                data = loads(data)
            debug(f'load file - [runtime: {time() - start_load_file}] <-<-<-<-<-<-<-<-<-<-')
            return data, 'data exist.'
        else:
            debug(f'{file_name} file is not exist.')
            return None, 'tags not exist in "base directory/.files/tags.data.json"'

    @property
    def doc2vec_model(self):
        file_name = join(PARENT_BASE_DIR, '.files/model.model')
        if isfile(file_name):
            mdl = gensim_document_to_vector.load(file_name)
            return mdl, 'model exist.'
        else:
            return None, 'model not exist in "base directory/.files/model.model"'

    def by_distance_vectors(self, string_1, string_2):
        """
        in tabe do string bar asase bordare gensim.doc2vec marboot b keyword hayeshan va
        bar asase metre spatial.distance.cosine ba yekdigar moghayese mishavand.
        :param string_1:
        :param string_2:
        :return:
        """
        string_1 = self.kywrds.by_frequency(string_1)
        string_2 = self.kywrds.by_frequency(string_2)
        model = self.doc2vec_model[0]
        doc_vec_1 = model.infer_vector(string_1)
        doc_vec_2 = model.infer_vector(string_2)
        return spatial.distance.cosine(doc_vec_1, doc_vec_2)

    def _load_data(self, data_path: str = None):
        file_name = join(PARENT_BASE_DIR, '.files', 'data.data.json')
        if isfile(file_name):
            data = self.data
            return data[0]
        else:
            data_list = files2pylist(data_path, file_format='txt')
            message = data_list[1]
            data_list = data_list[0]
            if data_list[0] is []:
                return message
            plp = TripleP(stopwords_list=self.stpwrds.STOPWORDSLIST)
            _data_list = []
            for d in data_list:
                _data_list.append(plp.tokens(d))
            data = _data_list
            dir_name = join(PARENT_BASE_DIR, '.files')
            mkdir(dir_name)
            jdata = dumps(data)
            with open(join(dir_name, 'data.data.json'), 'w', encoding='utf-8')as file:
                file.write(jdata)
        return data

    def _load_tags(self, data_path: str = None):
        if not self.exist_tags:
            tags = self.tags
            return tags[0]
        file_name = join(PARENT_BASE_DIR, '.files', 'tags.data.json')
        if isfile(file_name):
            tags = self.tags
            return tags[0]
        else:
            tags_list = files2pylist(data_path, file_format='tag')
            message = tags_list[1]
            tags = tags_list[0]
            if tags[0] is []:
                return message
            _tags = []
            for tag in tags:
                _tags.append(tag.split('\n'))
            tags = _tags
            dir_name = join(PARENT_BASE_DIR, '.files')
            jdata = dumps(tags)
            with open(join(dir_name, 'tags.data.json'), 'w', encoding='utf-8')as file:
                file.write(jdata)
        return tags

    def _documents2vectors(
            self,
            dm=1,
            vector_size=2 ** 7,
            window=2 ** 3,
            alpha=2 ** -6,
            min_alpha=2 ** -11,
            min_count=3,
            workers=2 ** 2,
            epochs=2 ** 7,
            dm_mean=0,
            dm_concat=0,
            dm_tag_count=2 ** 5,
            dbow_words=1,
    ):

        file_name = join(PARENT_BASE_DIR, '.files/model.model')
        if isfile(file_name):
            model = gensim_document_to_vector.load(file_name)
        else:
            data = self.data
            data = data[0]
            tags = self.tags
            tags = tags[0]
            corpus_keywords_list = []

            for doc in data:
                corpus_keywords_list.append(self.kywrds.by_frequency(doc))
            _data = []
            for doc in data:
                _doc = []
                for _sent in doc:
                    for wrd in _sent:
                        _doc.append(wrd)
                _data.append(_doc)
            data = _data

            documents = []
            for i in range(len(data)):
                keywords_list = corpus_keywords_list[i]
                if self.exist_tags:
                    for tag in tags[i]:
                        keywords_list.append(tag)
                documents.append(TaggedDocument(data[i], keywords_list))

            model = gensim_document_to_vector(
                documents=documents,
                dm=dm,
                vector_size=vector_size,
                window=window,
                alpha=alpha,
                min_alpha=min_alpha,
                min_count=min_count,
                workers=workers,
                epochs=epochs,
                dm_mean=dm_mean,
                dm_concat=dm_concat,
                dm_tag_count=dm_tag_count,
                dbow_words=dbow_words,
            )
            model.save(file_name)
        return model
