class Stopwords:
    def __init__(self, stopwords_list: list = None):
        if stopwords_list is not None:
            self.STOPWORDSLIST = stopwords_list
        else:
            from json import loads
            with open('./persian.stopword.json', 'r', encoding='utf-8') as file:
                s = file.read()
                s = loads(s)
            self.STOPWORDSLIST = s

    def is_stopword(self, word: str) -> bool:
        if word in self.STOPWORDSLIST:
            return True
        return False


class Keywords:
    def __init__(self, stopwords_list: list = None, minimum_frequency: float = 0.51,
                 maximum_frequency: float = 1) -> None:
        """

        :param stopwords_list: list paythoni az stopword ha.
        :param minimum_frequency: adadi beyene sefr va yek,
         kamtarin frquency ehtemali baraye shenasayi kalamate ba arzeshe bishtar.
        :param maximum_frequency: adadi beyene sefr va yek,
         bishtarin frquency ehtemali baraye shenasayi kalamate ba arzeshe bishtar.
        """
        if stopwords_list is not None:
            self.stopwords_list = stopwords_list

        self.minimum_frequency = minimum_frequency
        self.maximum_frequency = maximum_frequency

        fry = Frequency(self.stopwords_list)
        self.frequency_func = fry.normal_tfidf

    stopwords_list = []

    def by_frequency(self, document: list, func=None) -> list:
        if func is None:
            func = self.frequency_func
        keywords = []
        res = func(document)
        for (word, value) in res.items():
            if self.minimum_frequency <= value <= self.maximum_frequency:
                keywords.append(word)
        return keywords


class Frequency:
    def __init__(self, stopwords_list: list = None):
        if stopwords_list is not None:
            self._stopwords_list = stopwords_list

    _stopwords_list = []

    def tfidf(self, document: list) -> dict:
        """

        :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
            konim.

        :return: yek dictionary pythoni bar migardanad k keyword haye an kalamate darone document ast va value an
        barabarast ba meghdare tfidf mohasebe shude.
        """
        sum_all_fre = 0
        for sent in document:
            sum_all_fre += len(sent)

        document_term_frequency = {}
        for sent in document:
            for word in sent:
                if word not in self._stopwords_list:
                    if word not in document_term_frequency:
                        document_term_frequency[word] = 1 / sum_all_fre
                    else:
                        document_term_frequency[word] += 1 / sum_all_fre

        document_tfidf = {}
        from math import log as logarithm
        for (word, tf) in document_term_frequency.items():
            document_tfidf[word] = tf * (logarithm(1 / tf))

        return document_tfidf

    def normal_tfidf(self, document: list) -> dict:
        """

        :param document: documenti k be sorate yek string pythoni ast va mikhahim kalamte ba arzeshe an ra estekhraj
            konim.


        :return: yek dictionary pythoni bar migardanad k keyword haye an kalamate darone document ast va value an
        barabarast ba meghdare tfidf mohasebe shude.
        """
        document_tfidf = self.tfidf(document)

        values = document_tfidf.values()
        maximum_frequency = max(values)
        minimum_frequency = min(values)
        for (word, value) in document_tfidf.items():
            if minimum_frequency == maximum_frequency:
                document_tfidf[word] = 1
                continue
            document_tfidf[word] = (value - minimum_frequency) / (maximum_frequency - minimum_frequency)

        return document_tfidf
