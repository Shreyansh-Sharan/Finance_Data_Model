import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

yahoo_financials = YahooFinancials('AAPL')
data = yahoo_financials.get_historical_price_data(start_date='2018-01-01', 
                                                  end_date='2023-08-30', 
                                                  time_interval='weekly')
aapl_df = pd.DataFrame(data['AAPL']['prices'])
aapl_df = aapl_df.drop('date', axis=1).set_index('formatted_date')
aapl_df.head()

aapl_df = yf.download('AAPL',period="7d",interval="1m")
print(aapl_df)