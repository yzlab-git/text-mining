from transformers import pipeline
import pandas as pd

# パイプラインを作成
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment",device=0)

# CSVファイルを読み込む
csv_file = 'アンケート結果.csv'
df = pd.read_csv(csv_file)

print(df)
# 感情分析を実行
emotions = []
for text in df['回答']:
    results = classifier(text)
    predicted_emotion = results[0]['label']
    highest_prob = results[0]['score']
    emotions.append((predicted_emotion, highest_prob))

# 結果をDataFrameに追加
df['感情'] = [emotion[0] for emotion in emotions]
df['確率'] = [emotion[1] for emotion in emotions]

# 結果を出力
print(df)
