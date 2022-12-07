# coding: utf-8
import os
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def t0_close(df, row_id):
    return round(df.loc[row_id]['close'], 4)

def t0_close_ratio_last(df, row_id):
    return round(df.loc[row_id]['close']/df.loc[row_id-1]['close'], 4)

def t1_open(df, row_id):
    return round(df.loc[row_id-1]['open'], 4)

def t1_open_ratio_last(df, row_id):
    return round(df.loc[row_id-1]['open']/df.loc[row_id-2]['close'], 4)

def t1_high(df, row_id):
    return round(df.loc[row_id-1]['high'], 4)

def t1_high_ratio_last(df, row_id):
    return round(df.loc[row_id-1]['high']/df.loc[row_id-2]['close'], 4)

def t1_low(df, row_id):
    return round(df.loc[row_id-1]['low'], 4)

def t1_low_ratio_last(df, row_id):
    return round(df.loc[row_id-1]['low']/df.loc[row_id-2]['close'], 4)

def t1_close(df, row_id):
    return round(df.loc[row_id-1]['close'], 4)

def t1_close_ratio_last(df, row_id):
    return round(df.loc[row_id-1]['close']/df.loc[row_id-2]['close'], 4)

def t2_open(df, row_id):
    return round(df.loc[row_id-2]['open'], 4)

def t2_open_ratio_last(df, row_id):
    return round(df.loc[row_id-2]['open']/df.loc[row_id-3]['close'], 4)

def t2_high(df, row_id):
    return round(df.loc[row_id-2]['high'], 4)

def t2_high_ratio_last(df, row_id):
    return round(df.loc[row_id-2]['high']/df.loc[row_id-3]['close'], 4)

def t2_low(df, row_id):
    return round(df.loc[row_id-2]['low'], 4)

def t2_low_ratio_last(df, row_id):
    return round(df.loc[row_id-2]['low']/df.loc[row_id-3]['close'], 4)

def t2_close(df, row_id):
    return round(df.loc[row_id-2]['close'], 4)

def t2_close_ratio_last(df, row_id):
    return round(df.loc[row_id-2]['close']/df.loc[row_id-3]['close'], 4)

def t3_open(df, row_id):
    return round(df.loc[row_id-3]['open'], 4)

def t3_open_ratio_last(df, row_id):
    return round(df.loc[row_id-3]['open']/df.loc[row_id-4]['close'], 4)

def t3_high(df, row_id):
    return round(df.loc[row_id-3]['high'], 4)

def t3_high_ratio_last(df, row_id):
    return round(df.loc[row_id-3]['high']/df.loc[row_id-4]['close'], 4)

def t3_low(df, row_id):
    return round(df.loc[row_id-3]['low'], 4)

def t3_low_ratio_last(df, row_id):
    return round(df.loc[row_id-3]['low']/df.loc[row_id-4]['close'], 4)

def t3_close(df, row_id):
    return round(df.loc[row_id-3]['close'], 4)

def t3_close_ratio_last(df, row_id):
    return round(df.loc[row_id-3]['close']/df.loc[row_id-4]['close'], 4)

def t4_open(df, row_id):
    return round(df.loc[row_id-4]['open'], 4)

def t4_open_ratio_last(df, row_id):
    return round(df.loc[row_id-4]['open']/df.loc[row_id-5]['close'], 4)

def t4_high(df, row_id):
    return round(df.loc[row_id-4]['high'], 4)

def t4_high_ratio_last(df, row_id):
    return round(df.loc[row_id-4]['high']/df.loc[row_id-5]['close'], 4)

def t4_low(df, row_id):
    return round(df.loc[row_id-4]['low'], 4)

def t4_low_ratio_last(df, row_id):
    return round(df.loc[row_id-4]['low']/df.loc[row_id-5]['close'], 4)

def t4_close(df, row_id):
    return round(df.loc[row_id-4]['close'], 4)

def t4_close_ratio_last(df, row_id):
    return round(df.loc[row_id-4]['close']/df.loc[row_id-5]['close'], 4)

def t5_open(df, row_id):
    return round(df.loc[row_id-5]['open'], 4)

def t5_open_ratio_last(df, row_id):
    return round(df.loc[row_id-5]['open']/df.loc[row_id-6]['close'], 4)

def t5_high(df, row_id):
    return round(df.loc[row_id-5]['high'], 4)

def t5_high_ratio_last(df, row_id):
    return round(df.loc[row_id-5]['high']/df.loc[row_id-6]['close'], 4)

def t5_low(df, row_id):
    return round(df.loc[row_id-5]['low'], 4)

def t5_low_ratio_last(df, row_id):
    return round(df.loc[row_id-5]['low']/df.loc[row_id-6]['close'], 4)

def t5_close(df, row_id):
    return round(df.loc[row_id-5]['close'], 4)

def t5_close_ratio_last(df, row_id):
    return round(df.loc[row_id-5]['close']/df.loc[row_id-6]['close'], 4)

def t6_open(df, row_id):
    return round(df.loc[row_id-6]['open'], 4)

def t6_open_ratio_last(df, row_id):
    return round(df.loc[row_id-6]['open']/df.loc[row_id-7]['close'], 4)

def t6_high(df, row_id):
    return round(df.loc[row_id-6]['high'], 4)

def t6_high_ratio_last(df, row_id):
    return round(df.loc[row_id-6]['high']/df.loc[row_id-7]['close'], 4)

def t6_low(df, row_id):
    return round(df.loc[row_id-6]['low'], 4)

def t6_low_ratio_last(df, row_id):
    return round(df.loc[row_id-6]['low']/df.loc[row_id-7]['close'], 4)

def t6_close(df, row_id):
    return round(df.loc[row_id-6]['close'], 4)

def t6_close_ratio_last(df, row_id):
    return round(df.loc[row_id-6]['close']/df.loc[row_id-7]['close'], 4)

def t7_open(df, row_id):
    return round(df.loc[row_id-7]['open'], 4)

def t7_open_ratio_last(df, row_id):
    return round(df.loc[row_id-7]['open']/df.loc[row_id-8]['close'], 4)

def t7_high(df, row_id):
    return round(df.loc[row_id-7]['high'], 4)

def t7_high_ratio_last(df, row_id):
    return round(df.loc[row_id-7]['high']/df.loc[row_id-8]['close'], 4)

def t7_low(df, row_id):
    return round(df.loc[row_id-7]['low'], 4)

def t7_low_ratio_last(df, row_id):
    return round(df.loc[row_id-7]['low']/df.loc[row_id-8]['close'], 4)

def t7_close(df, row_id):
    return round(df.loc[row_id-7]['close'], 4)

def t7_close_ratio_last(df, row_id):
    return round(df.loc[row_id-7]['close']/df.loc[row_id-8]['close'], 4)

def t8_open(df, row_id):
    return round(df.loc[row_id-8]['open'], 4)

def t8_open_ratio_last(df, row_id):
    return round(df.loc[row_id-8]['open']/df.loc[row_id-9]['close'], 4)

def t8_high(df, row_id):
    return round(df.loc[row_id-8]['high'], 4)

def t8_high_ratio_last(df, row_id):
    return round(df.loc[row_id-8]['high']/df.loc[row_id-9]['close'], 4)

def t8_low(df, row_id):
    return round(df.loc[row_id-8]['low'], 4)

def t8_low_ratio_last(df, row_id):
    return round(df.loc[row_id-8]['low']/df.loc[row_id-9]['close'], 4)

def t8_close(df, row_id):
    return round(df.loc[row_id-8]['close'], 4)

def t8_close_ratio_last(df, row_id):
    return round(df.loc[row_id-8]['close']/df.loc[row_id-9]['close'], 4)

def t9_open(df, row_id):
    return round(df.loc[row_id-9]['open'], 4)

def t9_open_ratio_last(df, row_id):
    return round(df.loc[row_id-9]['open']/df.loc[row_id-10]['close'], 4)

def t9_high(df, row_id):
    return round(df.loc[row_id-9]['high'], 4)

def t9_high_ratio_last(df, row_id):
    return round(df.loc[row_id-9]['high']/df.loc[row_id-10]['close'], 4)

def t9_low(df, row_id):
    return round(df.loc[row_id-9]['low'], 4)

def t9_low_ratio_last(df, row_id):
    return round(df.loc[row_id-9]['low']/df.loc[row_id-10]['close'], 4)

def t9_close(df, row_id):
    return round(df.loc[row_id-9]['close'], 4)

def t9_close_ratio_last(df, row_id):
    return round(df.loc[row_id-9]['close']/df.loc[row_id-10]['close'], 4)


def read_feature_list(feature_file='./features.txt', mode='use'):
    feature_list = []
    with open(feature_file, 'r') as f:
        for line in f.readlines():  
            line = line.strip()
            feature, use = line.split(' ')
            if (mode == 'use' and use == '1') or mode == 'all':
                feature_list.append(feature)
    return feature_list        

def make_feature_file(input_file, output_file):
    df_5mins = pd.read_csv(input_file, sep='\t')
    df_features = pd.DataFrame(data=None, columns=read_feature_list(feature_file='./features.txt', mode='all'))

    for row_id in range(10, df_5mins.shape[0]):
        features = [eval(func)(df_5mins, row_id)  for func in read_feature_list(feature_file='./features.txt', mode='all')] 
        df_features.loc[len(df_features)] = features
    df_features.to_csv(output_file, sep='\t')

def make_feature_dir(input_dir, output_dir):
    for filename in sorted(os.listdir(input_dir)):
        logger.info(filename)
        make_feature_file(input_file=os.path.join(input_dir, filename), output_file=os.path.join(output_dir, filename))

if __name__ == '__main__':
    make_feature_dir(input_dir='/Users/xiaokunfan/code/data/tiger_1m_log_after/TSLA_5mins_ohlc', output_dir='/Users/xiaokunfan/code/data/tiger_1m_log_after/TSLA_5mins_features')
    #make_feature_dir(input_dir='/Users/xiaokunfan/code/data/taobao_TSLA_5mins_ohlc', output_dir='/Users/xiaokunfan/code/data/taobao_TSLA_5mins_features')
    #make_feature_dir(input_dir='/Users/xiaokunfan/code/data/TSLA_5mins_ohlc_202211', output_dir='/Users/xiaokunfan/code/data/TSLA_5mins_features_202211')
    #make_feature_file(input_file='./2022-08-30_TSLA_tiger_5mins.csv', output_file='./2022-08-30_TSLA_tiger_5mins_features.csv')
