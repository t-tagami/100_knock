# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

import re
from knock_20 import extract_uk
from knock_25 import extract_field
from knock_26 import rm_markup
from knock_27 import rm_link

def rm_medwiki(fdict):
    for key, value in fdict.items():
        value = re.sub(r'\[http.*\]', '', value) #外部リンク除去
        value = re.sub(r'(\**{{.*}}\（?)|((\）(?=<))|:)', '', value) #公式国名を整形
        value = re.sub(r'(<ref nam)|(<\/?ref>)|(<.*br.*>)', '', value) #ref nam br除去
        fdict[key] = value
    return fdict

dict_field = rm_medwiki(rm_markup(rm_link(extract_field())))
for key, value in dict_field.items():
    print(key, value)