""" main.py
Code challenge
"""

import numpy as np
import pandas as pd
# import yfinance as yf # Uncomment this line if you are wish to work with `yfinance` outside of Ed

# Write this function
def fx_code(from_cur, to_cur):
    """ Creates a string with the ticker required to download exchange rates
    using yfinance. The exchange rate will be the price of one unit of the `from_cur` in terms
    of the `to_cur`.

    Parameters
    ----------
    from_cur : str
        The ISO code of the currency to be priced.

    to_cur : str
        The ISO code of the currency with the value of one unit of `from_cur`.


    Returns
    -------
        A string that meets the `yfinance` ticker standards with ALL characters in upper case.
        The function should also be able to ignore leading and trailing spaces. For example,
        " aud", "Aud ", and " AUD " all are treated as "AUD" internally. See the
        Notes section below for more information.

    Notes
    -----
    Yahoo finance uses the following naming rules to define the ticker of the
    exchange rate AAA/BBB:
    usd/aud

    1. If AAA is the USD, then the ticker is "BBB=X", i.e., the second currency
       code with "=X" added at the end.
    2. If AAA is not the USD, then the ticker is "AAABBB=X"

    For example, the ticker for AUD/USD is "AUDUSD=X", while the ticker for
    USD/AUD is "AUD=X"

    So, if `from_cur=AAA` and the `to_cur=BBB`, the YF ticker will be:
    1. "BBB=X" if AAA is USD
    2. "AAABBB=X" if AAA is not the USD
    """
    ticker =''
    if from_cur == 'USD':
        ticker = to_cur + '=X'
    else:
        ticker = from_cur + to_cur +'=X'

    return ticker.replace(" ", "").upper()

# get_fx is provided to demonstrate how you can download currency data from `yfinance`.
# Once your fx_code function above is correct, get_fx should work on a computer
# that has the `yfinance` package installed.
def get_fx(from_cur, to_cur, period=None, interval=None):
    """ Downloads the exchange rate between the `from_cur` and the `to_cur`.
    The exchange rate will be the price of one unit of the `from_cur` in terms
    of the `to_cur`

    Parameters
    ----------
    from_cur : str
        The ISO code of the currency to be priced

    to_cur : str
        The ISO code of the currency with the value of one unit of
        `from_cur`.

    period : str, None
        valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        (optional, default is '1mo')

    interval : str, None
        valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        (optional, default is '1d')

    Returns
    -------
    df
        Dataframe with daily exchange rates from Yahoo Finance

    """
    # Defaults
    if period is None:
        period = '1mo'
    if interval is None:
        interval = '1d'

    tic = fx_code(from_cur, to_cur)

    # fetches the data
    df = yf.download(tic, period=period, interval=interval)

    return df
