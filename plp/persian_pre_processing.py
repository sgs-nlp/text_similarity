class TripleP:
    def __init__(self, stopwords_list: list = None):
        """
        in class baraye pish pardazeshe motone farsi sakhte shude ast k bar payeye hazm kar mikonad.
        :param stopwords_list: shuma mitavanid liste stopword haye khod ra be in class bedahid
        ya az defult khgode an estefade konid.
        """
        if stopwords_list is not None:
            self._STOPWORDSLIST = stopwords_list
        from hazm import Normalizer as hazm_normilizer
        self.normalizer = hazm_normilizer(
            remove_extra_spaces=True,
            persian_style=True,
            persian_numbers=True,
            remove_diacritics=True,
            affix_spacing=True,
            token_based=True,
            punctuation_spacing=True
        )

    def normal_string(self, string: str) -> str:
        """
        dar in ghesmat yek string farsi ra migirm va normal mikonim baraye etelae az chegonegiye normal kardan
        documention hazm ra motalee befarmaeid.
        :param string:
        :return: string noral shude
        """
        _str = ''
        for c in string:
            if self._is_symbol(c):
                _str += f' {c} '
                continue
            _str += c
        string = _str
        string = self.normalizer.normalize(string)
        return string

    def tokens(self, string) -> list:
        """
        dar in ghesmat yek string farsi k shamele chand jole ast daryaft mishavad va dar nahayat tamame in string bar
         asase kalamate darone an tokenize mishavad va darone ye liste pythoni gharar migirad
        ghabele tavajoh mibashad:
        :param string: yek reshteye farsi
        :return:yek list pythoni k -> [jomleye1:list, jomleye2:list, ...] va
         har jomle niz yek listpythoni k -> [kalame1:str, kalame2:str, ...].
        """

        from hazm import SentenceTokenizer, WordTokenizer
        sent_tokenizer = SentenceTokenizer().tokenize
        word_tokenizer = WordTokenizer().tokenize
        string = self.normal_string(string)
        sentences_list = sent_tokenizer(string)
        _sents = []
        for sent in sentences_list:
            words = word_tokenizer(sent)
            _sents.append(words)
        sentences_list = _sents
        return sentences_list

    def without_stop_words(self, string: str, stopwords_list: list = None) -> str:
        """
        ba estefade az in tabe mitavanid mati k darid ra normal va bedone stopword konid.
        :param string:
        :param stopwords_list:
        :return:
        """
        from .extractor import Stopwords
        if stopwords_list is not None:
            stpws = Stopwords(stopwords_list)
        else:
            stpws = Stopwords(self._STOPWORDSLIST)
        string = self.normal_string(string)
        is_sword = stpws.is_stopword
        string_split = string.split(' ')
        _str = ''
        for _wrd in string_split:
            string_split.remove(_wrd)
            if not is_sword(_wrd):
                _str = _wrd
                break
        for _wrd in string_split:
            if not is_sword(_wrd):
                _str += f' {_wrd}'
        string = _str
        return string

    @staticmethod
    def _is_symbol(character: str) -> bool:
        PERSISAN_SYMBOL = ['!', '"', '#', '(', ')', '*', ',', '-', '.', '/', ':', '[', ']', '«', '»', '،', '؛', '؟',
                           '+', '=', '_', '-', '&', '^', '%', '$', '#', '@', '!', '~', '"', "'", ':', ';', '>', '<',
                           '.', ',', '/', '\\', '|', '}', '{', '-', 'ـ', ]
        if character in PERSISAN_SYMBOL:
            return True
        return False
