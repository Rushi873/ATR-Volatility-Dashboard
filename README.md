## 📊 Trading Chart Web App

![image](https://github.com/user-attachments/assets/2b34cb75-d1ff-4a8e-833b-eac0b11eb692)


### 📌 Overview
This is a **Flask-based Trading Chart Web App** that visualizes candlestick data and technical indicators like:
- **Average True Range (ATR)**
- **Standard Deviation (Std Dev)**
- **Volume**

It uses **Lightweight Charts** for frontend charting and provides a **REST API** for retrieving indicator data.

---

## 🚀 Features
✅ **Interactive Trading Chart**  
✅ **ATR & Std Dev Indicators**  
✅ **Live Data Fetching via API**  
✅ **Indicator Customization (User Inputs)**  
✅ **Flask Backend with REST Endpoints**  

---

## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/trading-chart-app.git
cd trading-chart-app
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run the Flask App**
```sh
python app.py
```
This will start the server at `http://127.0.0.1:5000/`.

---

## 📂 Project Structure
```
📦 trading-chart-app
├── 📄 app.py              # Flask backend
├── 📄 requirements.txt    # Dependencies
├── 📄 data.csv            # Sample data file
├── 📄 templates/
│   ├── 📄 index.html      # Frontend (Lightweight Charts)
└── 📄 README.md           # Documentation
```

---

## 📡 API Endpoints
### 📊 **1. Candlestick Data**
**GET `/data`**  
📌 Returns OHLC (Open, High, Low, Close) data.  
```json
[
    {"time": 1700000000, "open": 45000, "high": 45500, "low": 44800, "close": 45200}
]
```

### 📈 **2. ATR Indicator**
**GET `/atr`**  
📌 Returns the **Average True Range (ATR)** values.  
```json
[
    {"time": 1700000000, "ATR": 120.5}
]
```

### 📉 **3. Standard Deviation**
**GET `/stddev`**  
📌 Returns **Standard Deviation** of close prices.  
```json
[
    {"time": 1700000000, "Std_Dev": 300.8}
]
```

### 📊 **4. Volume Data**
**GET `/volume`**  
📌 Returns **trading volume data**.  
```json
[
    {"time": 1700000000, "volume": 1500}
]
```

### 🔄 **5. Update ATR & Std Dev Period**
**POST `/update`**  
📌 Updates **ATR & Std Dev calculation periods**.  
📥 **Request JSON:**
```json
{
    "atr_period": 20,
    "std_period": 30
}
```
📤 **Response JSON:**
```json
{"message": "Indicators updated"}
```

---

## 🎨 Frontend (Lightweight Charts)
- **Library Used:** [Lightweight Charts](https://tradingview.github.io/lightweight-charts/)
- **Real-time updates from Flask API**
- **User controls for ATR & Std Dev**

---

## 🛠 Troubleshooting
### ⚠ **Issue: `ModuleNotFoundError`**
Run:
```sh
pip install -r requirements.txt
```

### ⚠ **Issue: Flask App Not Running**
Make sure **`data.csv`** exists in the project directory.

---

## 🤝 Contributing
Feel free to fork this repo and improve it! Pull requests are welcome.

---

## 📜 License
MIT License

---

This `README.md` is **detailed & professional**, making it easy for users to set up and use your project. 🚀
