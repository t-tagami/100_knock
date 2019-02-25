# 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

# 各文節は（表層形の）形態素列で表現する
# パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
# 「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

# 吾輩は -> 見た
# ここで -> 始めて -> 人間という -> ものを -> 見た
# 人間という -> ものを -> 見た
# ものを -> 見た

from knock_40 import Morph
from knock_41 import Chunk

for sent in Chunk.make_chunk_object_list():
    for chunk in filter(lambda x: x.check_contain_pos('名詞'), sent):
        chunk_list = [chunk]
        while chunk_list[-1].dst != -1:
            chunk_list.append(sent[chunk_list[-1].dst])
        print(' -> '.join(chunk.get_morph_surface() for chunk in chunk_list))