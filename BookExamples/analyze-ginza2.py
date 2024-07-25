import spacy

nlp = spacy.load("ja_ginza")
text = ("昨日の天気は晴れでした。明日も晴れるでしょう。")
doc = nlp(text)
for token in doc:
    print("{}\t{}\t{}\t{}".format(token, token.lemma_, token.pos_, token.tag_))