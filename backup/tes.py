import pandas as pd
# load csv data
df = pd.read_csv('prediksi_var.csv')
print(df)

# change column to datetime
df['Tanggal'] = pd.to_datetime(df['Tanggal'])
print(df)

df.info()