# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import re
from knock_20 import extract_uk
from collections import OrderedDict

def main():
    dict_field = extract_field()
    for key, value in dict_field.items():
        print(key, value)


def extract_field():
    odict_field = OrderedDict()
    # 基礎情報該当行の抽出
    str_correspond = re.search(r'(?=\{\{基礎情報)(.|\n)*?(?<=\n\}\})', extract_uk())
    # 行末でsplit
    list_field = re.split(r'\n[\||\}\}]', str_correspond.group())
    for i1 in range(len(list_field) - 2):
        temp = re.split(' = ', list_field[i1 + 1])
        odict_field[temp[0]] = temp[1]
    return odict_field

if __name__ == '__main__':
    main()