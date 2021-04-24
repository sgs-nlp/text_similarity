def main():
    from setting import DATA
    from setting import DOCUMENTS_TO_VECTORS_MODEL as model

    sent_1 = ['است', 'یافته', 'افزایش', 'اصفهان', 'در', 'طلاق']
    doc_vec_for_sent_1 = model.infer_vector(sent_1)

    sent_2 = ['است', 'یافته', 'افزایش', 'مشهد', 'در', 'طلاق']
    doc_vec_for_sent_2 = model.infer_vector(sent_2)

    sent_3 = ['بود', 'نیافته', 'کاهش', 'تهران', 'در', 'ازدواج']
    doc_vec_for_sent_3 = model.infer_vector(sent_3)

    sent_4 = ['است', 'غنی', 'فرهنگ', 'با', 'شهری', 'همدان']
    doc_vec_for_sent_4 = model.infer_vector(sent_4)
    #
    # sent_1 = ['اصفهان', 'طلاق']
    # doc_vec_for_sent_1 = model.infer_vector(sent_1)
    #
    # sent_2 = ['مشهد', 'طلاق']
    # doc_vec_for_sent_2 = model.infer_vector(sent_2)
    #
    # sent_3 = ['تهران', 'ازدواج']
    # doc_vec_for_sent_3 = model.infer_vector(sent_3)
    #
    # sent_4 = ['فرهنگ', 'همدان']
    # doc_vec_for_sent_4 = model.infer_vector(sent_4)

    from scipy import spatial
    _distance_1_1 = spatial.distance.cosine(doc_vec_for_sent_1, doc_vec_for_sent_1)

    print(f'distance[1 vs 1] :{_distance_1_1}')

    _distance_1_2 = spatial.distance.cosine(doc_vec_for_sent_1, doc_vec_for_sent_2)

    print(f'distance[1 vs 2] :{_distance_1_2}')

    _distance_1_3 = spatial.distance.cosine(doc_vec_for_sent_1, doc_vec_for_sent_3)
    print(f'distance[1 vs 3] :{_distance_1_3}')

    _distance_1_4 = spatial.distance.cosine(doc_vec_for_sent_1, doc_vec_for_sent_4)
    print(f'distance[1 vs 4] :{_distance_1_4}')

    _distance_2_2 = spatial.distance.cosine(doc_vec_for_sent_2, doc_vec_for_sent_2)
    print(f'distance[2 vs 2] :{_distance_2_2}')

    _distance_2_3 = spatial.distance.cosine(doc_vec_for_sent_2, doc_vec_for_sent_3)
    print(f'distance[2 vs 3] :{_distance_2_3}')

    _distance_2_4 = spatial.distance.cosine(doc_vec_for_sent_2, doc_vec_for_sent_4)
    print(f'distance[2 vs 4] :{_distance_2_4}')

    _distance_3_3 = spatial.distance.cosine(doc_vec_for_sent_3, doc_vec_for_sent_3)
    print(f'distance[3 vs 3] :{_distance_3_3}')

    _distance_3_4 = spatial.distance.cosine(doc_vec_for_sent_3, doc_vec_for_sent_4)
    print(f'distance[3 vs 4] :{_distance_3_4}')

    _distance_4_4 = spatial.distance.cosine(doc_vec_for_sent_4, doc_vec_for_sent_4)
    print(f'distance[4 vs 4] :{_distance_4_4}')


if __name__ == '__main__':
    main()
    from setting import START_TIME
    from time import time
    from logging import info

    info(f'total time for application running - [runtime: {time() - START_TIME}]')
