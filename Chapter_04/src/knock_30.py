# 30. 形態素解析結果の読み込み
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base）
# ，品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
# 第4章の残りの問題では，ここで作ったプログラムを活用せよ．

from itertools import groupby, islice
from pprint import pprint


def parse():
    with open('../work/neko.txt.mecab') as f:
        for is_eos, grouped in groupby(f, key=lambda x: x == 'EOS\n'):
            if not is_eos:
                parsed_sent = []
                for line in grouped:
                    surf, *parts = line.rstrip().replace('\t', ',').split(',')
                    parsed_sent.append({'surface': surf, 'base': parts[6],
                                        'pos': parts[0], 'pos1': parts[1]})
                yield parsed_sent


def main():
    for i in islice(parse(), 5): pprint(i)


if __name__ == '__main__':
    main()