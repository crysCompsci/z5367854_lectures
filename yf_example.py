# Downloads Qantas share price beginning 1 January 2020
import yfinance
start = '2020-01-01'                                      # (3)
end = None

# Qantas Stock Prices
tic = "QAN.AX"                                            # (2)                                              # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')

# Wesfarmers Stock prices
tic = "WES.AX"                                            # (2)                                              # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('wes_stk_prc.csv')

# alternative code
# tickers = ["QAN.AX", "WES.AX"]
# for tic in tickers:
#     df = yfinance.download(tic, start, end, ignore_tz=True)
#     print(df)
#     tic_base = tic.lower().split('.')[0]

#     df.to_csv(f'{tic_base}_stk_prc.csv')
