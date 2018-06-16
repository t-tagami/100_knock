# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import re
from knock_20 import extract_uk

for line in re.finditer(r'(\={2,5})(.+)?\1', extract_uk()):
    print(line.group(1).count('=')-1, line.group(2).strip())