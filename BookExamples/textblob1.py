from transformers import pipeline

# 日本語の感情分析用の事前学習済みBERTモデルをロード
model_name = "daigo/bert-base-japanese-sentiment"
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

tweet = "今年の漢字が発表されましたが、私の今年の漢字は「進」です。歴史を画するような様々な課題に対して、悪質な献金被害の救済新法や防衛力の抜本強化、新しい資本主義の具体化などを、一つ一つ進めており、また、来年も進めていきます。"
result = sentiment_pipeline(tweet)

print(result)


