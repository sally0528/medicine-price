💊 醫院藥品快速查價系統 
這是一個專為醫療行政與藥劑科設計的輕量化 Web 應用程式。透過整合 Python 資料處理、JavaScript 前端檢索與 Power BI 數據分析，解決健保藥價頻繁異動導致的查詢痛點。

🌟 核心功能
即時關鍵字檢索：支援藥品名稱與健保代碼的模糊搜尋。
自動化價格狀態判定：系統自動比對當前日期與生效日，標示「生效中」、「已失效」或「預計生效」。
視覺化色彩管理：針對不同藥品劑量（如 mg, mg/mL）進行高亮顯示，提升辨識度。
數據儀表板整合：嵌入 Power BI 動態報表，追蹤藥價異動趨勢。
離線查詢架構：採用靜態 JSON 驅動，無需後端伺服器即可實現毫秒級響應。

🛠️ 技術棧
Frontend: HTML5, CSS3, JavaScript (Vanilla JS)
Backend/Tools: Python (Pandas)
Data Format: JSON, Excel
Deployment: Firebase Hosting
Analytics: Power BI Embedded

🚀 系統架構
本專案經歷了從「動態 API」到「靜態資料驅動」的優化過程，以確保在醫院環境下的極致穩定性。
資料轉換：使用 convert.py 將原始健保公告 Excel 轉為標準化 data.json。
前端處理：index.html 在初始化時載入 JSON，並透過 JS 執行民國/西元日期轉換運算。
雲端發佈：託管於 Firebase Hosting，提供安全且快速的存取環境。

📂 檔案結構
Plaintext
├── convert.py           # Python 資料轉換腳本 (Excel to JSON)
├── data.json            # 系統核心資料庫 (由腳本產生)
├── index.html           # 系統主要網頁介面與搜尋邏輯
├── firebase.json        # Firebase 部署設定檔
└── med_data.xlsx        # 原始藥品健保公告資料

