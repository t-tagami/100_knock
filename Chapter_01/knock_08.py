
# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．英小文字ならば(219 - 文字コード)の
# 文字に置換．その他の文字はそのまま出力．この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(sent):
    return ("".join([chr(219-ord(word)) if word.islower() else word for word in sent]))

print(cipher("i have a pen"))
print(cipher(cipher("i have a pen")))