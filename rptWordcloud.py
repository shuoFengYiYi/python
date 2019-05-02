<<<<<<< HEAD
import jieba
import wordcloud
from scipy.misc import imread

#mask = imread("Chinamap.png")
f = open("T.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white")
w.generate(txt)
w.to_file("grwordcloud.png")
=======
import jieba
import wordcloud
from scipy.misc import imread

#mask = imread("Chinamap.png")
f = open("T.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white")
w.generate(txt)
w.to_file("grwordcloud.png")
>>>>>>> 3bfebb983d229ad281892b06b223b88c55206e14
