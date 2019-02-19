# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
# 内部リンクマークアップ  [[記事名]], [[記事名|表示文字]], [[記事名#節名|表示文字]]

import re
from knock_20 import extract_uk
from knock_25 import extract_field
from knock_26 import rm_markup

def main():
    dict_field = rm_link(rm_markup(extract_field()))
    for key, value in dict_field.items():
        print(key, value)

def rm_link(fdict):
    for key, value in fdict.items():
        if len(re.findall(r'\[{2}.*?((\|)|(#.*?\|)).*?\]{2}', value)): #[記事名|表示文字]と[[記事名#節名|表示文字]]
            value = re.sub(r'[|#]', '', value)
        fdict[key] = re.sub(r'\[{2}|\]{2}', '', value)
    return fdict

if __name__ == '__main__':
    main()