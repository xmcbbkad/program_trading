# coding: utf-8

import os
import re
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader():
    def __init__(self, feature_file):
         super(DataLoader, self).__init__()
         self.feature_names = self.read_feature_list(feature_file=feature_file)

    def read_feature_list(self, feature_file='./features.txt', mode='use'):
        feature_list = []
        with open(feature_file, 'r') as f:
            for line in f.readlines():  
                line = line.strip()
                feature, use = line.split(' ')
                if (mode == 'use' and use == '1') or mode == 'all':
                    feature_list.append(feature)
        return feature_list        


    def load_data_from_file(self, data_file):
        df = pd.read_csv(data_file, header=0, sep='\t')
        df = df[self.feature_names]
    
        return df


    def load_data_from_dir(self, data_dir, pattern='.', not_pattern='fffff'):
        df_all = pd.DataFrame(columns = self.feature_names)
        for name in sorted(os.listdir(data_dir)):
            if os.path.isdir(os.path.join(data_dir, name)):
                df = self.load_data_from_dir(data_dir=os.path.join(data_dir, name), pattern=pattern, not_pattern=not_pattern)
            else: # is file:
                if (not re.search(pattern, name)) or re.search(not_pattern, name):
                    continue
                #logger.info("read_file={}".format(os.path.join(data_dir, name)))
                df = self.load_data_from_file(data_file=os.path.join(data_dir, name))
            df_all = df_all.append(df, ignore_index=True)
       
        return df_all

    def split_x_y(self, df, label):
        X = df.drop(label, axis=1)
        Y = df[label]
        return X, Y


