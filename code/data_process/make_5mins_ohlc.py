# coding: utf-8
import os
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_1mins_time(input_df):
    last_ts = 0
    for row in input_df.index:
        if last_ts == 0 or input_df.loc[row]['ts'] - last_ts == 60000:
            last_ts = input_df.loc[row]['ts']
        else:
            return False
    return True
            

def make_5mins_ohlc_file(one_mins_file, five_mins_file):
    df_1mins = pd.read_csv(one_mins_file, names=['ts', 'time', 'open', 'high', 'low', 'close', 'volume'], sep='\t')
    if not check_1mins_time(df_1mins):
        return
    
    df_5mins = pd.DataFrame(data=None,columns=['ts', 'time', 'open', 'high', 'low', 'close', 'volume'])
     
    for row_id in range(0, df_1mins.shape[0], 5):
        open_ = -1
        high = -99999
        low = 99999
        close = -1
        ts = 0
        time = ''
        volume = 0
        if row_id+4 >= df_1mins.shape[0]:
            break
        for i in range(5):
            if i == 0:
                open_ = df_1mins.loc[row_id+i]['open']
            elif i == 4:
                close = df_1mins.loc[row_id+i]['close']
                ts = df_1mins.loc[row_id+i]['ts']
                time = df_1mins.loc[row_id+i]['time']
            if df_1mins.loc[row_id+i]['low'] < low:
                low = df_1mins.loc[row_id+i]['low']
            if df_1mins.loc[row_id+i]['high'] > high:
                high = df_1mins.loc[row_id+i]['high']
            volume += df_1mins.loc[row_id+i]['volume']
        df_5mins.loc[len(df_5mins)] = [ts, time, open_, high, low, close, volume]
        open_ = -1
        high = -99999
        low = 99999
        close = -1
        ts = 0
        time = ''
        volume = 0
    df_5mins.to_csv(five_mins_file, sep='\t')

def make_5mins_ohlc_dir(input_dir, output_dir):
    for filename in sorted(os.listdir(input_dir)):
        logger.info(filename)
        make_5mins_ohlc_file(one_mins_file=os.path.join(input_dir, filename), five_mins_file=os.path.join(output_dir, filename))
        

if __name__ == '__main__':
    #make_5mins_ohlc_dir('/Users/xiaokunfan/code/program_trading/data/tiger_1m_log_after/TSLA', '/Users/xiaokunfan/code/program_trading/data/tiger_1m_log_after/TSLA_5mins_ohlc')
    #make_5mins_ohlc_dir('/Users/xiaokunfan/code/program_trading/data/xueqiu_1m_log_after/MSFT/2022', '/Users/xiaokunfan/code/program_trading/data/xueqiu_1m_log_after/MSFT_5mins_ohlc/2022')
    make_5mins_ohlc_dir('/Users/xiaokunfan/code/program_trading/data/taobao_new_TSLA/TSLA/2020', '/Users/xiaokunfan/code/program_trading/data/taobao_new_TSLA/TSLA_5mins_ohlc/2020')
    #make_5mins_ohlc_dir('/Users/xiaokunfan/code/program_trading/data/taobao_TSLA_2021/', '/Users/xiaokunfan/code/program_trading/data/taobao_TSLA_5mins_ohlc_2021/')
    #make_5mins_ohlc_file(one_mins_file='./2022-08-30_TSLA_tiger', five_mins_file='./2022-08-30_TSLA_tiger_5mins.csv')
