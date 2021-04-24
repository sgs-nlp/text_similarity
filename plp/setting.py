from os.path import dirname
from pathlib import Path
BASE_DIR = dirname(__file__)
PARENT_BASE_DIR = Path(BASE_DIR).parent
STOP_WORDS_PATH = './persian.stopword.json'
