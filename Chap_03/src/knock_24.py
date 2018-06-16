# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import re
from knock_20 import extract_uk

for line in re.finditer(r'(File:|ファイル:)([^|]+)', extract_uk()):
    print(line.group(2))