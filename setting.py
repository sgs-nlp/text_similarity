from logging import basicConfig, info, DEBUG
from os.path import join, dirname
from time import time

from repository import (
    _files2csvformat,
    _create_dictionary,
    _coding,
    _create_documents2vectors_model,
    _data_tokenize,
)

DATASETS_URL = '/home/ya_hasan_mojtaba/my_projects/datasets'
RESOURCES_URL = '/home/ya_hasan_mojtaba/my_projects/resources'
POSTAGGER_MODEL_URL = join(RESOURCES_URL, 'hazm/resources-0.5/postagger.model')

START_TIME = time()

basicConfig(
    format='[%(asctime)s] - [%(filename)s:%(lineno)d] %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=DEBUG,
)

BASE_DIR = dirname(__file__)

DATA = _files2csvformat(
    directory_name=join(DATASETS_URL, 'hamshahri_news/news-corpus'),
    file_num=10,
)

DICTIONARY, DICTIONARY4CODING, DICTIONARY4DECODING = _create_dictionary()

DATA_CODE = _coding()
DATA_TOKEN = _data_tokenize()

DOCUMENTS_TO_VECTORS_MODEL = _create_documents2vectors_model()

info(f'import - [runtime: {time() - START_TIME}]')
