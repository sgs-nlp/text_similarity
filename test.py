a = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
b = [0.011, 0.015, 0.1, 0.09, 0.013, 0.01, 0.011, 0.012, 0.013, 0.014]
from scipy.spatial import distance
from textdistance import hamming
from textdistance import cosine

dist_ = distance.cosine(a, b)
print(dist_)
dist_2 = cosine(a, b)
print(dist_2)
