from csv import reader, writer
from json import dumps, loads
from logging import debug
from os.path import isfile, dirname, join
from os import mkdir
from time import time


def is_empty(obj) -> bool:
    if obj is None:
        return True
    if len(obj) == 0:
        return True
    if obj == 'None':
        return True
    if obj == 'none':
        return True
    return False


PERSISAN_SYMBOL = ['!', '"', '#', '(', ')', '*', ',', '-', '.', '/', ':', '[', ']', '«', '»', '،', '؛', '؟', '+', '=',
                   '_', '-', '&', '^', '%', '$', '#', '@', '!', '~', '"', "'", ':', ';', '>', '<', '.', ',', '/', '\\',
                   '|', '}', '{', '-', 'ـ', ]


def is_symbol(character: str) -> bool:
    if character in PERSISAN_SYMBOL:
        return True
    return False


def _files2csvformat(
        directory_name: str,
        file_num: int,
        file_name: str = '.files/.nvd',
) -> list:
    from setting import BASE_DIR
    file_name = join(BASE_DIR, f'{file_name}.data')
    if isfile(file_name):
        debug(f'{file_name} file exist')
        debug(f'try for load {file_name} file ->->->->->->->->->->')
        time_start = time()
        with open(file_name, 'rt')as file:
            data = list(reader(file))
        debug(f'load {file_name} file - [runtime: {time() - time_start}]')
    else:
        debug(f'{file_name} file not exist')
        time_start = time()
        debug(f'try for create {file_name} file ->->->->->->->->->->')
        debug('try for load dictionary-label2code-tags.csv ->->->->->->->->->->')
        time_start_1 = time()
        with open(f'{directory_name}/dictionary-label2code-tags.csv', 'r') as file:
            _fdict = file.read()
        tags = []
        debug(
            f'load dictionary-label2code-tags.csv - [runtime: {time() - time_start_1}] <-<-<-<-<-<-<-<-<-<-')
        from hazm import Normalizer as hazm_normilizer
        normalizer = hazm_normilizer(
            remove_extra_spaces=True,
            persian_style=True,
            persian_numbers=True,
            remove_diacritics=True,
            affix_spacing=True,
            token_based=True,
            punctuation_spacing=True
        )
        for _row in _fdict.split('\n'):
            _rd = []
            for _field in _row.split(','):
                if not is_empty(_field):
                    _rd.append(_field)
            if not is_empty(_rd):
                tags.append(_rd)
        data = [["text", "label", "tag_1", "tag_2", "tag_3", "tag_4"], ]
        for i in range(file_num):
            j = 0
            while True:
                j += 1
                _file_name = f'{directory_name}/{i + 1}-{j}.txt'
                _data = []
                time_start_2 = time()
                if isfile(_file_name):
                    debug(f'try for load {_file_name} file ->->->->->->->->->->')
                    with open(_file_name, 'r') as file:
                        txt = file.read()
                    # dar in ghesmat character haye alaem ra az alfba ba yek fasele joda mikonam
                    # ta kalamat bedone dar nazar gerfte shudane alaem baresi shavand.
                    # -> ->
                    _txt = ''
                    for c in txt:
                        if is_symbol(c):
                            _txt += f' {c} '
                            continue
                        _txt += c
                    txt = _txt
                    # <- <-
                    # normal kardane matn -> ->
                    txt = normalizer.normalize(txt)
                    _data = [txt, f"{i + 1}"]
                    for tag in tags[i]:
                        _data.append(tag)
                    data.append(_data)
                    debug(
                        f'load {_file_name} file - [runtime: {time() - time_start_2}] <-<-<-<-<-<-<-<-<-<-')
                else:
                    break
        debug(f'create {file_name} file - [runtime: {time() - time_start}] <-<-<-<-<-<-<-<-<-<-')
        mkdir(dirname(file_name))
        time_start = time()
        debug(f'try for save {file_name} file ->->->->->->->->->->')
        with open(file_name, 'w')as file:
            _writer = writer(file)
            for row in data:
                _writer.writerow(row)
        debug(f'save {file_name} file - [runtime: {time() - time_start}] <-<-<-<-<-<-<-<-<-<-')
    return data


def _create_dictionary(
        file_name: str = '.files/.nvd',
        dictionary_key_len=10,
        postfix='',
        prefix=''
) -> [dict, dict, dict]:
    from setting import BASE_DIR
    file_name = join(BASE_DIR, file_name)
    _dictionary_dict = {}
    _dict4coding_dict = {}
    _dict4decoding_dict = {}
    if isfile(f'{file_name}.dictionary') and \
            isfile(f'{file_name}.dictionary4coding') and \
            isfile(f'{file_name}.dictionary4decoding'):

        debug(f'{file_name}.dictionary file exist')
        time_start = time()
        debug(f'try load {file_name}.dictionary file ->->->->->->->->->->')
        with open(f'{file_name}.dictionary', 'r')as file:
            _dictionary_dict = loads(file.read())
        debug(
            f"load {file_name}.dictionary file - [runtime: {time() - time_start}] "
            f"<-<-<-<-<-<-<-<-<-<-")

        debug(f'{file_name}.dictionary4coding file exist')
        time_start = time()
        debug(f'try load {file_name}.dictionary4coding file ->->->->->->->->->->')
        with open(f'{file_name}.dictionary4coding', 'r')as file:
            _dict4coding_dict = loads(file.read())
        debug(
            f"load {file_name}.dictionary4coding file - [runtime: {time() - time_start}] "
            f"<-<-<-<-<-<-<-<-<-<-")

        debug(f'{file_name}.dictionary4decoding file exist')
        time_start = time()
        debug(f'try load {file_name}.dictionary4decoding file ->->->->->->->->->->')
        with open(f'{file_name}.dictionary4decoding', 'r')as file:
            _dict4decoding_dict = loads(file.read())
        debug(
            f"load {file_name}.dictionary4decoding file - [runtime: {time() - time_start}] "
            f"<-<-<-<-<-<-<-<-<-<-")
    else:
        debug(f'{file_name}.dictionary file not exist')
        debug(f'{file_name}.dictionary4coding file not exist')
        debug(f'{file_name}.dictionary4decoding file not exist')
        debug(f'try for create {file_name}.* files ->->->->->->->->->->')
        time_start_1 = time()
        _dict = {}
        _dict_2 = {}
        dict_idx = 0
        sentences = []

        from hazm import POSTagger as hazm_postagger
        from setting import BASE_DIR
        tagger = hazm_postagger(model=join(BASE_DIR, 'resources-0.5', 'postagger.model'))
        from hazm import SentenceTokenizer as hazm_sentence_tokenizer
        sent_tokenizer = hazm_sentence_tokenizer()
        from hazm import WordTokenizer as hazm_word_tokenizer
        word_tokenizer = hazm_word_tokenizer(join_verb_parts=True)
        from setting import DATA
        data = DATA
        for doc in data:
            _doc = ''
            for itm in doc:
                _doc += f' {itm} ,'
            text = _doc
            # tokenizer
            sents = sent_tokenizer.tokenize(text)
            _sents = []
            for sent in sents:
                _sents.append(word_tokenizer.tokenize(sent))
            text = _sents
            _text = []
            for txt in text:
                _text.append(tagger.tag(txt))
            doc = _text
            # <- end_tokenizer
            for sent in doc:
                __sent = []
                for word in sent:
                    word_2 = word
                    word = str(word)
                    if word not in _dict:
                        _dict[word] = dict_idx
                        _dict_2[dict_idx] = word_2
                        dict_idx += 1
                    __sent.append(word)
                sentences.append(__sent)

        from gensim.models.word2vec import Word2Vec as gensim_word_to_vector
        model = gensim_word_to_vector(
            sentences=sentences,
            size=1,
            alpha=0.02,
            window=10,
            min_count=0,
            workers=4,
            min_alpha=0.00001,
            sg=1,
            iter=5
        )
        _dictionary = {}
        _dict4coding = {}
        _dict4decoding = {}
        for key in _dict:
            val = {'string': _dict_2[_dict[key]][0], 'post_tag': _dict_2[_dict[key]][1]}
            key = str((model.wv[key][0] + 100) * (10 ** dictionary_key_len))[0:dictionary_key_len]
            key = f'{prefix}{key}{postfix}'
            _dictionary[key] = val
            _dict4coding[val['string']] = key
            _dict4decoding[key] = val['string']
        _dictionary_dict = _dictionary
        _dict4coding_dict = _dict4coding
        _dict4decoding_dict = _dict4decoding
        debug(f'create file - [runtime: {time() - time_start_1}] <-<-<-<-<-<-<-<-<-<-')
        debug(f'try for save {file_name}.* files ->->->->->->->->->->')
        time_start = time()
        with open(f'{file_name}.dictionary', 'w') as file:
            file.write(dumps(_dictionary))
        with open(f'{file_name}.dictionary4coding', 'w') as file:
            file.write(dumps(_dict4coding))
        with open(f'{file_name}.dictionary4decoding', 'w') as file:
            file.write(dumps(_dict4decoding))
        debug(f'save {file_name}.* files - [runtime: {time() - time_start}] <-<-<-<-<-<-<-<-<-<-')
    return _dictionary_dict, _dict4coding_dict, _dict4decoding_dict


def _coding(file_name: str = '.files/.nvd.code') -> list:
    from setting import BASE_DIR
    file_name = join(BASE_DIR, file_name)
    _data_coding = []
    if isfile(file_name):
        debug(f'{file_name} file exist')
        time_start = time()
        debug(f'try for load {file_name} file')
        with open(file_name, 'r')as file:
            _data = loads(file.read())
        _data_coding = _data
        debug(f'load {file_name} file - [runtime: {time() - time_start}]')
    else:
        debug(f'{file_name} file not exist')
        debug(f'try for create {file_name} file')
        time_start = time()
        _data = []
        from hazm import SentenceTokenizer as hazm_sentence_tokenizer
        sent_tokenizer = hazm_sentence_tokenizer()
        from hazm import WordTokenizer as hazm_word_tokenizer
        word_tokenizer = hazm_word_tokenizer(join_verb_parts=True)
        from setting import DATA, DICTIONARY4CODING
        data = DATA
        dictionary = DICTIONARY4CODING
        for row in data:
            _row = []
            for itm in row:
                sents = sent_tokenizer.tokenize(itm)
                _sents = []
                for sent in sents:
                    _sent = []
                    for word in word_tokenizer.tokenize(sent):
                        _sent.append(f'{dictionary[word]}')
                    _sents.append(_sent)
                _row.append(_sents)
            _data.append(_row)
        debug(f'create {file_name} file - [runtime: {time() - time_start}]')
        debug(f'try for save {file_name} file')
        time_start = time()
        with open(file_name, 'w')as file:
            file.write(dumps(_data))
        debug(f'save {file_name} file - [runtime: {time() - time_start}]')
        _data_coding = _data
    return _data_coding


def word2code(word: str) -> str:
    from setting import DICTIONARY4CODING
    if word not in DICTIONARY4CODING:
        return 'None'
    return DICTIONARY4CODING[word]


def code2word(code: str) -> str:
    from setting import DICTIONARY4DECODING
    if code not in DICTIONARY4DECODING:
        return 'None'
    return DICTIONARY4DECODING[code]


def _create_documents2vectors_model(
        dm=1,
        vector_size=2**7,
        window=2**3,
        alpha=2**-6,
        min_alpha=2**-11,
        min_count=3,
        workers=2**2,
        epochs=2**7,
        dm_mean=0,
        dm_concat=0,
        dm_tag_count=2**5,
        dbow_words=1,
        file_name='.files/.nvd.model',
):
    from setting import BASE_DIR
    file_name = join(BASE_DIR, file_name)
    if isfile(file_name):
        debug(f'{file_name} file is exist')
        debug(f'try for load {file_name} file ->->->->->->->->->->')
        time_start = time()
        from gensim.models.doc2vec import Doc2Vec as gensim_document_to_vector
        model = gensim_document_to_vector.load(file_name)
        debug(f'load {file_name} file - [runtime: {time() - time_start}] <-<-<-<-<-<-<-<-<-<-')
    else:
        debug(f'{file_name} file is not exist')
        debug(f'try for create {file_name} file ->->->->->->->->->->->')
        time_start = time()
        from setting import DATA as data
        data = data[1:]
        keywords = []
        tags = []
        for doc in data:
            _tags = doc[2:]
            tags.append(_tags)
            doc = doc[0]
            _keywords = extract_keywords_from_text(doc)
            for tag in _tags:
                _keywords.append(tag)
            keywords.append(_keywords)
        documents = []

        from setting import DATA_TOKEN as data
        data = data[1:]
        _wdocs = []
        for row in data:
            for sent in row[0]:
                _doc = []
                for word in sent:
                    _doc.append(word)
                _wdocs.append(_doc)

        from gensim.models.doc2vec import TaggedDocument
        for i in range(len(keywords)):
            documents.append(TaggedDocument(_wdocs[i], keywords[i]))
        from gensim.models.doc2vec import Doc2Vec as gensim_document_to_vector

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

        debug(f'create {file_name} file - [runtime: {time() - time_start}] <-<-<-<-<-<-<-<-<-<-')
        time_start = time()
        debug(f'try for save {file_name} file ->->->->->->->->->->')
        model.save(file_name)
        debug(f'save {file_name} file - [runtime: {time() - time_start}]<-<-<-<-<-<-<-<-<-<-')
    return model


def extract_keywords_from_text(text: str) -> list:
    with open('repo/persian.stopword.json') as file:
        stopwords = file.read()
    import json
    stopwords = json.loads(stopwords)
    from rake_nltk import Rake
    r = Rake()
    r.extract_keywords_from_text(text)

    fry = r.get_word_frequency_distribution()
    max_fry = max(fry.values())
    keywords_list = []
    for itm in fry.items():
        if itm[0] in stopwords:
            continue
        if 12 < (itm[1] / max_fry) * 100:
            keywords_list.append(itm[0])
    return keywords_list


def dictionary_update(word: str):
    pass


def _data_tokenize():
    from setting import DATA
    data = DATA[1:]
    from hazm import SentenceTokenizer, WordTokenizer
    sent_tokenizer = SentenceTokenizer().tokenize
    word_tokenizer = WordTokenizer().tokenize
    _docs = []
    for row in data:
        sents = sent_tokenizer(row[0])
        _sents = []
        for sent in sents:
            words = word_tokenizer(sent)
            _sents.append(words)
        _docs.append(_sents)
    _tags = []
    for row in data:
        tags = row[2:]
        _tag = []
        for tag in tags:
            words = word_tokenizer(tag)
            _tag.append([words])
        _tags.append(_tag)
    _data = [[[[DATA[0][0]]], [[DATA[0][1]]], [[DATA[0][2]]], [[DATA[0][3]]], [[DATA[0][4]]]]]
    for i in range(len(data)):
        _temp = [_docs[i], [data[i][1]]]
        for tag in _tags[i]:
            _temp.append(tag)
        _data.append(_temp)
    return _data
