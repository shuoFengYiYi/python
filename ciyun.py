<<<<<<< HEAD
#GovRptWordCloudv2.py
import jieba
import wordcloud
import scipy.misc
mask = imageio.imread("Chinamap.png")
f = open("T.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )
w.generate(txt)
=======
#GovRptWordCloudv2.py
import jieba
import wordcloud
import scipy.misc
mask = imageio.imread("Chinamap.png")
f = open("T.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )
w.generate(txt)
>>>>>>> 3bfebb983d229ad281892b06b223b88c55206e14
w.to_file("grwordcloudm.png")