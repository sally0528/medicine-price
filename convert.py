import pandas as pd
import json

# 讀取你目前的資料表 (請更換成你正確的檔名)
df = pd.read_excel("11502公告_3月份健保用藥項目價格檔異動.xlsx") 

# 將資料轉換成 JSON 格式
# orient='records' 會讓它變成像 [{}, {}, {}] 的清單格式
data = df.to_json(orient='records', force_ascii=False)

with open("data.json", "w", encoding="utf-8") as f:
    f.write(data)

print("data.json 已產生！請將此檔案下載並放到 Firebase 專案目錄中。")