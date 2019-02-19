# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

import re
from knock_20 import extract_uk
from knock_25 import extract_field

def main():
    dict_field = rm_markup(extract_field())
    for key, value in dict_field.items():
        print(key, repr(value))

def rm_markup(fdict):
    for key, value in fdict.items():
        fdict[key] = re.sub(r'\'{2,5}', '', value)
    return fdict

if __name__ == '__main__':
    main()