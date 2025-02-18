from flask import Flask, render_template, request, jsonify
import pandas as pd
import ta

app = Flask(__name__)

# ✅ Load and Process Data
df = pd.read_csv('data.csv')
df['time'] = pd.to_datetime(df['Timestamp']).astype('int64') // 10**9  # Convert to UNIX timestamp
df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'}, inplace=True)

DEFAULT_ATR_PERIOD = 14
DEFAULT_STD_DEV_PERIOD = 20

def calculate_indicators(atr_period, std_period):
    df['ATR'] = ta.volatility.AverageTrueRange(df['high'], df['low'], df['close'], window=atr_period).average_true_range()
    df['Std_Dev'] = df['close'].rolling(window=std_period).std()
    return df[['time', 'ATR', 'Std_Dev', 'volume']].dropna()

indicators_df = calculate_indicators(DEFAULT_ATR_PERIOD, DEFAULT_STD_DEV_PERIOD)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_candlestick_data():
    return jsonify(df[['time', 'open', 'high', 'low', 'close']].to_dict(orient='records'))

@app.route('/atr')
def get_atr():
    return jsonify(indicators_df[['time', 'ATR']].dropna().to_dict(orient='records'))

@app.route('/stddev')
def get_stddev():
    return jsonify(indicators_df[['time', 'Std_Dev']].dropna().to_dict(orient='records'))

@app.route('/volume')
def get_volume():
    return jsonify(df[['time', 'volume']].to_dict(orient='records'))

@app.route('/update', methods=['POST'])
def update_indicators():
    data = request.json
    atr_period = int(data.get('atr_period', DEFAULT_ATR_PERIOD))
    std_period = int(data.get('std_period', DEFAULT_STD_DEV_PERIOD))
    global indicators_df
    indicators_df = calculate_indicators(atr_period, std_period)
    return jsonify({'message': 'Indicators updated'})

if __name__ == '__main__':
    app.run(debug=True)
