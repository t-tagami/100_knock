# 文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，
# 係り受けパスは以下の仕様を満たすものとする．

# 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
# 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
# また，係り受けパスの形状は，以下の2通りが考えられる．

# 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
# 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから
# 文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
# 例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

# Xは | Yで -> 始めて -> 人間という -> ものを | 見た
# Xは | Yという -> ものを | 見た
# Xは | Yを | 見た
# Xで -> 始めて -> Y
# Xで -> 始めて -> 人間という -> Y
# Xという -> Y

from itertools import combinations
from knock_40 import Morph
from knock_41 import Chunk

for sent in Chunk.make_chunk_object_list():
    for idx_i, idx_j in combinations(Chunk.get_idx(sent, '名詞'), 2):
        path_i = [sent[idx_i].replace_surface('X')]
        dst_num = sent[idx_i].dst
        while dst_num != -1:
            if dst_num == idx_j:
                path_i.append(sent[dst_num].replace_surface('Y'))
                print(' -> '.join(path_i))
                break
            else:
                path_i.append(sent[dst_num].get_morph_surface())
                dst_num = sent[dst_num].dst

        path_j = [sent[idx_j].replace_surface('Y')]
        dst_num = sent[idx_j].dst
        while dst_num != -1:
            path_j.append(sent[dst_num].get_morph_surface())
            if path_j[-1] in path_i:
                path_i_str = ' -> '.join(path_i[:path_i.index(path_j[-1])])
                path_j_str = ' -> '.join(path_j[:-1])
                print(' | '.join([path_i_str, path_j_str, path_j[-1]]))
                break
            dst_num = sent[dst_num].dst
