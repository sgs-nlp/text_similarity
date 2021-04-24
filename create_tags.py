import glob
from logging import debug
from os.path import isdir
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


my_path = '/home/nvd/my_projects/datasets/hamshahri/news_all'
filenames = glob.glob(f'{my_path}/*.txt')
with open(f'{my_path}/dictionary-label2code-tags.csv', 'r') as file:
    _fdict = file.read()
tags = []
for _row in _fdict.split('\n'):
    _rd = []
    for _field in _row.split(','):
        if not is_empty(_field):
            _rd.append(_field)
        if not is_empty(_rd):
            tags.append(_rd)
from json import dumps
for filename in filenames:
    with open(f'{filename.split(".")[0]}.tag', 'w', encoding='utf-8') as file:
        idx = filename.split('/')[-1]
        idx = idx.split('-')[0]
        idx = int(idx)-1
        for tag in tags[idx]:
            file.write(tag)
            file.write('\n')

# filenames = glob.glob(f'{my_path}/*.tag')
# from json import loads
# for filename in filenames:
#     with open(filename, 'r', encoding='utf-8') as file:
#         _fdict = file.read()
#         print(_fdict.split('\n'))
# tags = []