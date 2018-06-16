# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re
from knock_20 import extract_uk

for line in re.finditer(r"\[\[Category:([^|\]]*)", extract_uk()):
    print(line.group(1))