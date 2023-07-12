from flask import Flask, render_template
import pandas as pd
import json, os, plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # load csv data
    df = pd.read_csv('datasets/tpa.csv')
    # change column to datetime
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    # create a line chart
    fig = px.line(df, x='Tanggal', y=['Jumlah sampah'])
    # Update the layout to move the legend/variable below the plot
    fig.update_layout(legend=dict(orientation="h", y=-0.2, x=0.5))
    # Set the y-axis title
    fig.update_layout(yaxis_title='Jumlah Sampah (ton)')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', graphJSON=graphJSON)

@app.route('/prediksi')
def prediksi():
    # load csv data
    df = pd.read_csv('datasets/prediksi_arima.csv')
    # change column to datetime
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    # create a line chart
    fig = px.line(df, x='Tanggal', y=['Jumlah sampah', 'Prediksi Jumlah Sampah'], color_discrete_sequence=px.colors.qualitative.Dark2)
    # Update the layout to move the legend/variable below the plot
    fig.update_layout(legend=dict(orientation="h", y=-0.2, x=0.5))
    # Set the y-axis title
    fig.update_layout(yaxis_title='Jumlah Sampah (ton)')
    # Create table visualization
    table = df.to_html(classes='table table-striped')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    title="Prediksi jumlah sampah di TPA Jatibarang"
    header="Grafik Prediksi Jumlah Sampah"
    description = """
    Berdasarkan grafik prediksi jumlah sampah di TPA Jatibarang, terdapat tren naik turun dalam jumlah sampah dari bulan ke bulan. Pada awal tahun 2021, jumlah sampah mencapai 27.726.357 ton, kemudian mengalami penurunan pada bulan Februari dan Maret. Namun, seiring berjalannya waktu, jumlah sampah kembali naik dan mencapai puncaknya pada bulan Desember 2021 dengan 29.487.597 ton. Prediksi jumlah sampah pada tahun 2022 menunjukkan fluktuasi yang tidak terlalu signifikan. Namun, pada tahun 2023, prediksi jumlah sampah menunjukkan kecenderungan yang menurun dari bulan ke bulan. Meskipun terdapat sedikit fluktuasi, prediksi jumlah sampah tetap tinggi, dengan perkiraan mencapai 27.573.124 ton pada bulan Januari 2023. Prediksi ini dapat menjadi acuan dalam mengembangkan strategi pengelolaan sampah yang efektif dan berkelanjutan di TPA Jatibarang.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, title=title, header=header, description=description, table=table)

@app.route('/suhu')
def suhu():
    # load csv data
    df = pd.read_csv('datasets/prediksi_cuaca_var.csv')
    # change column to datetime
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    # create a line chart
    fig = px.line(df, x='Tanggal', y=['Jumlah sampah', 'Jumlah Sampah Prediction'], color_discrete_sequence=px.colors.qualitative.Dark2)
    # Update the layout to move the legend/variable below the plot
    fig.update_layout(legend=dict(orientation="h", y=-0.2, x=0.5))
    # Set the y-axis title
    fig.update_layout(yaxis_title='Jumlah Sampah (ton)')
    # Create table visualization
    table = df.to_html(classes='table table-striped')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    title="Prediksi jumlah sampah di TPA Jatibarang berdasarkan suhu"
    header="Grafik Prediksi Jumlah Sampah Berdasarkan Suhu"
    description = """
    Berdasarkan grafik prediksi jumlah sampah di TPA Jatibarang yang dikaitkan dengan suhu udara 2 m di atas tanah (T2M), terdapat beberapa pola yang menarik. Pada tahun 2021, jumlah sampah cenderung fluktuatif dengan sedikit korelasi terhadap suhu udara. Namun, pada tahun 2022, terlihat adanya korelasi yang lebih jelas antara suhu udara dan jumlah sampah. Pada bulan-bulan dengan suhu udara yang lebih rendah, jumlah sampah cenderung meningkat, sedangkan pada bulan dengan suhu udara yang lebih tinggi, jumlah sampah cenderung menurun. Prediksi jumlah sampah untuk tahun 2023 menunjukkan kecenderungan yang stabil dengan fluktuasi yang lebih kecil. Meskipun terdapat beberapa peningkatan atau penurunan yang terjadi dari bulan ke bulan, pola umum menunjukkan bahwa suhu udara masih memiliki pengaruh pada jumlah sampah yang dihasilkan. Hal ini menunjukkan pentingnya mempertimbangkan faktor lingkungan seperti suhu udara dalam pengelolaan sampah yang berkelanjutan di TPA Jatibarang.
    """
    return render_template('notdash2.html', graphJSON=graphJSON, title=title, header=header, description=description, table=table)

if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000))