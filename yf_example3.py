"""yf_example3.py

yf_example3.py will download stock price data for Qantas for a given year and save the information in a CSV file
"""

import os
import toolkit_config as cfg
import yf_example2

"""
Download Qantas stock prices for a given year into a CSV file
The name of this file will be qan_prc_YYYY.csv, where the YYYY stands for the year in year.
"""
def qan_prc_to_csv(year):
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(tic, pth, start='2020-01-01', end='2020-12-31')


if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)