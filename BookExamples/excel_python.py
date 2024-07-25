import pandas as pd
import oseti

# CSVファイルのパス
file_path = 'Earthgumi1.csv'

# CSVファイルの読み込み
data = pd.read_csv(file_path)

import re

# 制御文字のパターン
#control_chars = re.compile(r'[\n]')

control_chars = re.compile(r'[\x00-\x1F\x7F]')  # 制御文字の正規表現
data['cleaned_text'] = data['商品レビュー'].map(lambda x: control_chars.sub('', str(x)))  # カラム名を置き換え


# データフレーム内のすべての文字列から制御文字を削除
#data = data.map(lambda x: control_chars.sub('', x) if isinstance(x, str) else x)
#analyzer = oseti.Analyzer()

#results = data.apply(lambda x: analyzer.analyze_detail(x))

# 結果を表示
#for result in results:
 #   print(result)

analyzer = oseti.Analyzer()

# 各要素を個別に分析
results = data['cleaned_text'].apply(lambda x: analyzer.analyze_detail(x))

# 結果を表示
for result in results:
    print(result)







