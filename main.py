from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd
import uvicorn
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    conn = sqlite3.connect('nhi_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def root():
    return {"message": "API 運行中，請使用 /data 或 /search"}

@app.get("/data")
def get_all_data():
    try:
        conn = get_db_connection()
        df = pd.read_sql("SELECT * FROM medicine_prices", conn)
        conn.close()
        df = df.replace({np.nan: None, np.inf: None, -np.inf: None})
        return df.to_dict(orient='records')
    except Exception as e:
        return {"error": str(e)}

@app.get("/search")
def search_medicine(name: str = Query(None)):
    if not name:
        return {"error": "請輸入搜尋關鍵字"}
    
    try:
        conn = get_db_connection()
        # ⚠️ 注意：這裡使用 "Unnamed: 3" 並加上雙引號，因為欄位名含有冒號
        query = 'SELECT * FROM medicine_prices WHERE "Unnamed: 3" LIKE ?'
        df = pd.read_sql(query, conn, params=(f'%{name}%',))
        conn.close()

        df = df.replace({np.nan: None, np.inf: None, -np.inf: None})
        return df.to_dict(orient='records')
    except Exception as e:
        return {"error": "搜尋失敗", "details": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)