import pke
#import ginza
import nltk
from spacy.lang import ja


pke.base.stopwords['ja_ginza_electra'] = 'japanese'
# ↓は以前のバージョンの書き方でうまく動かない
# pke.base.ISO_to_language['ja_ginza']

stopwords = list(ja.STOP_WORDS)
nltk.corpus.stopwords.words_org = nltk.corpus.stopwords.words
nltk.corpus.stopwords.words = lambda lang : stopwords if lang == 'japanese' else nltk.corpus.stopwords.words_olg(lang)


# Wikipedia カエルより引用
# https://ja.wikipedia.org/wiki/%E3%82%AB%E3%82%A8%E3%83%AB
text = ("地域によっては、授業の中心がICTになっているところもあれば、発達していないところもあり、" + \
        "結構な差があったように感じた。" + \
        "ICTを活用しているのとしていないのでは、学ぶことも大きく違ってくると思うので、" + \
        "地域差をできるだけなくしていく必要があるのではないかと考えた。"
        )

extractor = pke.unsupervised.TopicRank()

# normalization=None を指定しないと，デフォルトの Stemming 処理が走りそれが日本語未対応のためエラーになる
extractor.load_document(input=text, language = 'ja', normalization=None)

extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ', 'NUM'})
extractor.candidate_weighting()

keyphrases = extractor.get_n_best(n = 10)

print(keyphrases)