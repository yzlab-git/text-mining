import pandas as pd

# アンケート結果をリストに格納
responses = [
    "製品の品質は素晴らしいです。特にデザインが気に入りました。使いやすさも抜群です。",
    "製品は普通です。期待通りの性能で、特に良い点や悪い点はありませんでした。",
    "製品は期待外れでした。機能が不安定で、操作性も悪いです。購入を後悔しています。"
]

# リストをDataFrameに変換
df = pd.DataFrame({'回答': responses})

# CSVファイルに保存
df.to_csv('アンケート結果.csv', index=False, encoding='utf-8-sig')
