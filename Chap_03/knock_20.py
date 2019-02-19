
# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip, json

def main():
    print(extract_uk())

def extract_uk():
    with gzip.open('../data/jawiki-country.json.gz', 'rt') as f20:
        for line in f20:
            if (json.loads(line)['title'] == 'イギリス'): return(json.loads(line)['text'])


if __name__ == '__main__':
    main()