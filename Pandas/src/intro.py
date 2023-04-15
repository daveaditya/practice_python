import pandas as pd
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = web.DataReader("AAPL", "google", start, end)

print(df.head())
