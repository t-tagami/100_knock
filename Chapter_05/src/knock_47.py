# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

# 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
# 例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

# 返事をする      と に は        及ばんさと 手紙に 主人は
# このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

# コーパス中で頻出する述語（サ変接続名詞+を+動詞）
# コーパス中で頻出する述語と助詞パターン

from knock_40 import Morph
from knock_41 import Chunk

for sent in Chunk.make_chunk_object_list():
	for chunk in filter(lambda x: x.check_contain_pos('動詞'), sent):

		temp_chunk = ' '.join(sent[src].get_morph_surface() for src in chunk.srcs
							  if sent[src].check_contain_sahen_wo())
		if temp_chunk:
			particles = ' '.join(sent[src].get_surface_pos('助詞') for src in chunk.srcs
								 if sent[src].check_contain_pos('助詞') and not sent[src].check_contain_pos1('サ変接続'))

			terms = ' '.join(sent[src].get_morph_surface() for src in chunk.srcs
							 if sent[src].check_contain_pos('助詞') and not sent[src].check_contain_pos1('サ変接続'))
			if terms:
				print('{}{}\t{}\t{}'.format(temp_chunk, chunk.get_left_base('動詞'), particles, terms))