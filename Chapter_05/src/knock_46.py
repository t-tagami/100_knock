# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
# 45の仕様に加えて，以下の仕様を満たすようにせよ．

# 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
# 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
# 「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の
# ２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような
# 出力になるはずである．

# 始める  で      ここで
# 見る    は を   吾輩は ものを

from knock_40 import Morph
from knock_41 import Chunk

for sent in Chunk.make_chunk_object_list():
    for chunk in filter(lambda x:x.check_contain_pos('動詞'), sent):

        particles = ' '.join(sent[src].get_surface_pos('助詞') for src in chunk.srcs
                            if sent[src].check_contain_pos('助詞'))

        terms = ' '.join(sent[src].get_morph_surface()
                         for src in chunk.srcs if sent[src].check_contain_pos('助詞'))
        if particles:
            print('{:10}\t{}\t{}'.format(chunk.get_left_base('動詞'), particles, terms))