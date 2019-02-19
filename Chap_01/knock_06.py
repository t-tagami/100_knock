# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

from knock_05 import n_gram
from pprint import pprint

def check_set(word, f_set):
    return(word + ' exists in ') if word in f_set else (word + ' does not exists in ')

X = set(n_gram(2, 1, "paraparaparadise"))
Y = set(n_gram(2, 1, "paragraph"))
pprint("和集合:{} 積集合:{} (X-Y)の差集合:{} (Y-X)の差集合:{}".format(X | Y, X & Y, X - Y, Y - X))
print(check_set('se', X) + 'X\t',check_set('se', Y) + 'Y')