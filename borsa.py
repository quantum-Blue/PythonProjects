# https://api.yapikredi.com.tr/api/stockmarket/v1/

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from prophet import Prophet

# VAKBN
# AKBNK
# ADESE
# ENKAI

# yahoo finance sitesinden bakabilirsin, verileri oradan alıyor

"""
Bu adimda hissenin verilerini aliyoruz. Bazi parametreleri degistirebiliriz,

period="max": yazan parametreyi degistirerek ne kadar gecmisten data alacagimiz.("1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max")
interval="1d": aldigimiz verilerin cozunurlugu.("1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo")
"""
# ADESE : hisse şirketinin adı, .IS (istanbul borsası olduğunu belirtir)
adese = yf.Ticker('ADESE.IS')

hist_df = adese.history(period="max", interval="1d", auto_adjust=True)

print(hist_df)

hist_df.plot(y=["Close"], figsize=(20,10))
#hist_df.plot(y=["Low","High"], figsize=(30,15))
plt.show()

"""
Prophet hakkinda daha detayli bilgi: https://facebook.github.io/prophet/

Sadece sonunda bir "ds" ve "y" degeri gerekiyor bize. Prophet bu sekilde calisiyor.

"ds" sutunundan da timezone bilgisini silmemiz gerekiyor.
"""

df = pd.DataFrame()

df['ds_tz'] = hist_df.index
df['ds'] = df['ds_tz'].dt.tz_localize(None) # ds_tz sutunundan timezone bilgisini cikartip "ds" sutununa yaz.
df.drop(columns=['ds_tz'],inplace=True) # ds_tz sutununu sil.
df['y'] = hist_df['Close'].values

print(df.tail(10))

#Prophet bu asamada tahminimizi yapiyor

m = Prophet(daily_seasonality=False)

m.fit(df)

future = m.make_future_dataframe(365, freq='D')

forecast = m.predict(future)

print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(7))

# print(forecast) #tüm tahminleri gruplayarak gösterir

m.plot(forecast)
plt.show()


