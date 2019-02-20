# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand
# what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

def main():
    str_typo = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(' '.join([i1 if len(i1) < 5 else i1[0] + ''.join(shuffle(list(i1[1:-1]))) + i1[-1] for i1 in str_typo.split()]))

def shuffle(f_list):
    random.shuffle(f_list)
    return f_list

if __name__ == '__main__':
    main()