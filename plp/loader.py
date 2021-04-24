import glob
from logging import debug
from os.path import isdir
from time import time


def files2pylist(mypath: str, file_format: str = 'txt') -> [list, str]:
    """
    in tabe masiri ra daryaft mikonad va tamame file haye .txt daron an directory ra khaande va dar ghalebe ye liste
    pythoni erae midahad.
    :param file_format:
    :param mypath: masire gharar gereftane file haye txt
    :return: [liste pythoni shamele maghadire darone file ha,
    payami dar rabete ba emkane load kardane file ha ya natavanestan]
    """
    if not isdir(mypath):
        return [], 'directory is not exist.'
    debug(f'try for load files ->->->->->->->->->->')
    load_start_time = time()
    filenames = glob.glob(f'{mypath}/*.{file_format}')
    res = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
        debug(f'load {filename} file.')
        res.append(data)
    debug(f'load files - [runtime: {time() - load_start_time}] <-<-<-<-<-<-<-<-<-<-')
    return res, ''
