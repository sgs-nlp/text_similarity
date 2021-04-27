# plp

کتابخانه ای برای پیش پردازش و پردازش داده های متنی فارسی که پایه ی کتابخانه هضم ساخته شده است.

## نحوه راه اندازی

برای نصب این کتابخانه می توانید از پکیچ منجیر [پیپ] استفاده کنید.

```bash
pip install /to/path
```

## نحوه استفاده

در این قسمت می‌توانید نحوه ی استفاده ابزار فراخوانی کردن دیتا درون برنامه را مشاهده کنید.

```python
from plp import loader

corpus = loader.files2pylist(
    mypath='path/for/load/document/files',
    file_format='txt')  # returns [[all],[document],]
```

در این قسمت از ابزار پیش پردازش داده استفاده شده است که عموم این ابزار بر اساس نیاز، از ترکیب ابزار درون کتابخانه هضم
استفاده شده است.

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

در این قسمت در رابطه با ابزار مربوط به واکشی ایست واژه‌ها و استخراج کلمات کلیدی توضیح داده شده است.

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

from plp.loader import files2pylist

corpus = files2pylist(
    mypath='path/for/load/document/files',
    file_format='txt'
)  # returns [[all],[documents],]
from plp.extractor import Frequency

fry = Frequency(
    stopwords_list=stopword_tools.STOPWORDSLIST
)
documents_keywords = []
for doc in corpus:
    documents_keywords.append(
        keywords_tools.by_frequency(
            document=doc,
            func=fry.normal_tfidf
        )
    )

```

این قسمت در رابطه با پیش مقدمات مشابهت متن و توضیح ابزار این مجموعه صحبت شده است.

```python
from plp.text_similarity import Similarity
from plp.extractor import Stopwords, Keywords
from plp.persian_pre_processing import TripleP

txt_simi = Similarity(
    data_path='path/for/load/document/files',
    exist_tags=True,
)
stpwrds = Stopwords()
ppp = TripleP(
    stopwords_list=stpwrds.STOPWORDSLIST,
)
kywrds = Keywords(
    stopwords_list=stpwrds.STOPWORDSLIST,
    minimum_frequency=0.2,
)

# load text one
with open('path/sample/text_1.txt', 'r', encoding='utf-8') as file:
    doc_1 = file.read()
doc_1 = ppp.tokens(doc_1)


# load text two
with open('path/sample/text_2.txt', 'r', encoding='utf-8') as file:
    doc_2 = file.read()
doc_2 = ppp.tokens(doc_2)


distance_between_document_1_and_document_2 = \ 
txt_simi.by_distance_vectors(doc_1, doc_2)



```