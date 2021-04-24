# plp

کتابخانه ای برای پیش پردازش و پردازش داده های متنی فارسی که پایه ی کتابخانه هضم ساخته شده است.

## نحوه راه اندازی

برای نصب این کتابخانه می توانید از پکیچ منجیر [پیپ] استفاده کنید.

```bash
pip install /to/path
```

## نحوه استفاده

```python
from plp import loader

corpus = loader.files2pylist(
    mypath='path/for/load/document/files',
    file_format='txt')  # returns [[all],[document],]
```

```python
from plp.extractor import Stopwords
from plp import persian_pre_processing as plp_hazm_base

stopword_tools = Stopwords(
    stopwords_list='list_other_than_the_default_list')
p = plp_hazm_base.TripleP(
    stopwords_list=stopword_tools.STOPWORDSLIST)
normal_string = p.normal_string(
    string='unnormal_string')  # return 'normal string'
string_tokenize = p.tokens('string')  # return [[word],[tokenize],[by],[hazm],]
string_without_stop_words = p.without_stop_words(
    'string without stop words'
)  # return 'string words'
```

```python
from plp.extractor import Stopwords, Keywords

stopword_tools = Stopwords(stopwords_list='list_other_than_the_default_list')

minimum_frequency = 0.0  # 0.0 < float < 1.0
maximum_frequency = 1.0  # 0.0 < float < 1.0
keywords_tools = Keywords(
    stopwords_list=stopword_tools.STOPWORDSLIST,
    minimum_frequency=minimum_frequency,
    maximum_frequency=maximum_frequency
)

corpus = files2pylist('path/for/load/document/files', 'txt')  # returns [[all],[document],]
```

