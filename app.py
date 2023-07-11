from flask import Flask, render_template
import pandas as pd
import json, os, plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # load csv data
    df = pd.read_csv('tpa.csv')
    # change column to datetime
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    # create a line chart
    fig = px.line(df, x='Tanggal', y=['Jumlah sampah'])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', graphJSON=graphJSON)

@app.route('/prediksi')
def prediksi():
    # load csv data
    df = pd.read_csv('prediksi_arima.csv')
    # change column to datetime
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    # create a line chart
    fig = px.line(df, x='Tanggal', y=['Jumlah sampah', 'Prediksi Jumlah Sampah'])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    title="Prediksi jumlah sampah di TPA Jatibarang"
    header="Grafik Prediksi Jumlah Sampah"
    description = """
    A academic study of the number of apples, oranges and bananas in the cities of
    San Francisco and Montreal would probably not come up with this chart.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, title=title, header=header, description=description)

@app.route('/suhu')
def suhu():
    # load csv data
    df = pd.read_csv('prediksi_var.csv')
    # change column to datetime
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    # create a line chart
    fig = px.line(df, x='Tanggal', y=['Jumlah sampah', 'Prediksi Jumlah Sampah'])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    title="Prediksi jumlah sampah di TPA Jatibarang berdasarkan suhu"
    header="Grafik Prediksi Jumlah Sampah Berdasarkan Suhu"
    description = """
    The rumor that vegetarians are having a hard time in London and Madrid can probably not be
    explained by this chart.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, title=title, header=header, description=description)

if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000))