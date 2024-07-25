import nltk
from rake_nltk import Rake

# punktデータセットをダウンロード
nltk.download('punkt')

r = Rake()
# テキストの例
text = """
1. ICTを活用した授業の事例を調べる中でICTを活用しやすいのは算数や理科などの理系科目だと感じた。国語でも電子黒板やデジタル教科書を使って文章を読みやすくしたりはできるが、従来と大きな変化はないと思う。しかし、算数や理科ではモノの動きを観察することが多く、カメラを使って大きくみせたり、動画を見せることでよりイメージしやすくなる。また、算数の問に対する考えや、理科の実験から考えたことなどを生徒が発表する時もICTは便利であると感じた。
2. 理科の授業で実験がある場合、生徒に危険をもたらしてしまう可能性がある実験は、映像にして生徒に見せることができる。可視化できることは授業を聞くよりだけよりも効果的に記憶に定着するように感じる。さらに、アプリを使用するなどすると、生徒一人一人の意見や生徒の解答などを先生が即座に知ることができ、理解状況を把握しやすくなったり、テストの採点が楽になったりする。
3. 数学では、イメージしにくいグラフを式を入れるだけで作ってくれるアプリを使って教える。
"""

# キーフレーズを抽出する
r.extract_keywords_from_text(text)

# キーフレーズとそのスコアを表示する
print(r.get_ranked_phrases_with_scores())

# RAKEオブジェクトの作成
#r = Rake()

# テキストを解析
#r.extract_keywords_from_text(text)

# キーフレーズとそのスコアを取得
#keywords = r.get_ranked_phrases_with_scores()

# 結果を表示
#for score, phrase in keywords:
   # print(f"{score}: {phrase}")

#print(keywords)