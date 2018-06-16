# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import requests
from knock_25 import extract_field

url = 'https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=imageinfo&iiprop=url&titles=File:' + extract_field()['国旗画像']
print(requests.get(url).json()['query']['pages']['-1']['imageinfo'][0]['url'])