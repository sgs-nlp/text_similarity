class Test:
    def __init__(self):
        from plp.text_similarity import Similarity
        from plp.persian_pre_processing import TripleP
        from plp.extractor import Keywords, Stopwords

        self.txt_smy = Similarity('./news_all', exist_tags=True)
        self.stpwrds = Stopwords()
        self.ppp = TripleP(stopwords_list=stpwrds.STOPWORDSLIST)
        self.kywrds = Keywords(stopwords_list=stpwrds.STOPWORDSLIST, minimum_frequency=0.4)

        with open(f'./news/1.txt', 'r', encoding='utf-8') as file:
            sent_1 = file.read()
        self.sent_1 = ppp.tokens(sent_1)

        with open(f'./news/1.tag', 'r', encoding='utf-8') as file:
            tags_1 = file.read()
        self.tags_1 = tags_1.split('\n')

        with open(f'./news/2.txt', 'r', encoding='utf-8') as file:
            sent_2 = file.read()
        self.sent_2 = ppp.tokens(sent_2)

        with open(f'./news/2.tag', 'r', encoding='utf-8') as file:
            tags_2 = file.read()
        self.tags_2 = tags_2.split('\n')

        with open(f'./news/3.txt', 'r', encoding='utf-8') as file:
            sent_3 = file.read()
        self.sent_3 = ppp.tokens(sent_3)

        with open(f'./news/3.tag', 'r', encoding='utf-8') as file:
            tags_3 = file.read()
        self.tags_3 = tags_3.split('\n')

        with open(f'./news/4.txt', 'r', encoding='utf-8') as file:
            sent_4 = file.read()
        self.sent_4 = ppp.tokens(sent_4)

        with open(f'./news/4.tag', 'r', encoding='utf-8') as file:
            tags_4 = file.read()
        self.tags_4 = tags_4.split('\n')


# from logging import basicConfig, DEBUG
# basicConfig(
#     format='[%(asctime)s] - [%(filename)s:%(lineno)d] %(levelname)s - %(message)s',
#     datefmt='%d-%b-%y %H:%M:%S',
#     level=DEBUG,
# )
from plp.text_similarity import Similarity
from plp.persian_pre_processing import TripleP
from plp.extractor import Keywords, Stopwords

txt_smy = Similarity('/home/ya_hasan_mojtaba/my_projects/datasets/hamshahri/news_all', exist_tags=True)
stpwrds = Stopwords()
ppp = TripleP(stopwords_list=stpwrds.STOPWORDSLIST)
kywrds = Keywords(stopwords_list=stpwrds.STOPWORDSLIST, minimum_frequency=0.2)

path_sample_text = '/home/ya_hasan_mojtaba/my_projects/datasets/hamshahri/news'
with open(f'{path_sample_text}/66-93.txt', 'r', encoding='utf-8') as file:
    sent_1 = file.read()
print('*************************************************\nsentence 1:\n', sent_1)
with open(f'{path_sample_text}/66-93.tag', 'r', encoding='utf-8') as file:
    tags_1 = file.read()
    tags_1 = tags_1.split('\n')
print('##################################################\ntags:\n', tags_1)
sent_1 = ppp.tokens(sent_1)
k_sent_1 = kywrds.by_frequency(sent_1)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nkeywords:\n', k_sent_1)

with open(f'{path_sample_text}/66-94.txt', 'r', encoding='utf-8') as file:
    sent_2 = file.read()
print('*************************************************\nsentence 2:\n', sent_2)
with open(f'{path_sample_text}/66-94.tag', 'r', encoding='utf-8') as file:
    tags_2 = file.read()
    tags_2 = tags_2.split('\n')
print('##################################################\ntags:\n', tags_2)
sent_2 = ppp.tokens(sent_2)
k_sent_2 = kywrds.by_frequency(sent_2)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nkeywords:\n', k_sent_2)

with open(f'{path_sample_text}/66-95.txt', 'r', encoding='utf-8') as file:
    sent_3 = file.read()
print('*************************************************\nsentence 3:\n', sent_3)
with open(f'{path_sample_text}/66-95.tag', 'r', encoding='utf-8') as file:
    tags_3 = file.read()
    tags_3 = tags_3.split('\n')
print('##################################################\ntags:\n', tags_3)
sent_3 = ppp.tokens(sent_3)
k_sent_3 = kywrds.by_frequency(sent_3)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nkeywords:\n', k_sent_3)

with open(f'{path_sample_text}/9-1.txt', 'r', encoding='utf-8') as file:
    sent_4 = file.read()
print('*************************************************\nsentence 4:\n', sent_4)
with open(f'{path_sample_text}/9-1.tag', 'r', encoding='utf-8') as file:
    tags_4 = file.read()
    tags_4 = tags_4.split('\n')
print('##################################################\ntags:\n', tags_4)
sent_4 = ppp.tokens(sent_4)
k_sent_4 = kywrds.by_frequency(sent_4)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\nkeywords:\n', k_sent_4)

print('Distance between document sent_1 and document sent_1: ', txt_smy.by_distance_vectors(sent_1, sent_1))
print('Distance between document sent_1 and document sent_2: ', txt_smy.by_distance_vectors(sent_1, sent_2))
print('Distance between document sent_1 and document sent_3: ', txt_smy.by_distance_vectors(sent_1, sent_3))
print('Distance between document sent_1 and document sent_4: ', txt_smy.by_distance_vectors(sent_1, sent_4))
# print('Distance between document sent_2 and document sent_2: ', txt_smy.by_distance_vectors(sent_2, sent_2))
print('Distance between document sent_2 and document sent_3: ', txt_smy.by_distance_vectors(sent_2, sent_3))
print('Distance between document sent_2 and document sent_4: ', txt_smy.by_distance_vectors(sent_2, sent_4))
# print('Distance between document sent_3 and document sent_3: ', txt_smy.by_distance_vectors(sent_3, sent_3))
print('Distance between document sent_3 and document sent_4: ', txt_smy.by_distance_vectors(sent_3, sent_4))
# print('Distance between document sent_4 and document sent_4: ', txt_smy.by_distance_vectors(sent_4, sent_4))
