# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import re
from knock_20 import extract_uk

for line in re.finditer(r'\[\[Category:.*\]\]', extract_uk()):
    print(line.group())