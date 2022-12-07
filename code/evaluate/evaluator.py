# coding: utf-8

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Evaluator():
    def __init__(self):
        super(Evaluator, self).__init__()
        self.all_m = {}

    def sum_metrics(self, m):
        self.all_m['gain'] = self.all_m['gain'] + m['gain'] if 'gain' in self.all_m.keys() else m['gain']
        self.all_m['long_gain'] = self.all_m['long_gain'] + m['long_gain'] if 'long_gain' in self.all_m.keys() else m['long_gain']
        self.all_m['short_gain'] = self.all_m['short_gain'] + m['short_gain'] if 'short_gain' in self.all_m.keys() else m['short_gain']


    def cal_random_metrics(self, y_true):
        y_random = np.random.rand(len(y_true))
        y_random += 0.5
        
        m = self.cal_metrics(y_true, y_random)
        return m

    def cal_metrics(self, y_true, y_pred):
        tp = 0
        fp = 0
        tn = 0
        fn = 0
       
        gain = 0
        long_gain = 0
        short_gain = 0
        
        rmse = mean_squared_error(y_true, y_pred) ** 0.5

        for i in range(len(y_true)):
            #logger.info("y_pred:{}  y_true:{}".format(round(y_pred[i], 4), y_true[i]))
            #print("y_pred:{}  y_true:{}".format(round(y_pred[i], 4), y_true[i]))
            
            if y_pred[i] == -1:  #不召回不处理
                continue


            if y_pred[i] > 1 and y_true[i] > 1:
                tp +=1
                long_gain += y_true[i]-1
            elif y_pred[i] > 1 and y_true[i] < 1:
                fp +=1
                long_gain -= (1-y_true[i])
            elif y_pred[i] < 1 and y_true[i] > 1:
                fn +=1
                short_gain -= (y_true[i]-1)
            elif y_pred[i] < 1 and y_true[i] < 1:
                tn +=1
                short_gain += (1-y_true[i])
       
        gain = round(long_gain + short_gain, 4)
        long_gain = round(long_gain, 4)
        short_gain = round(short_gain, 4)

        acc = round((tp+tn)*1.0/(tp+tn+fp+fn), 4)
        long_acc = round(tp*1.0/(tp+fp+1e-10), 4)
        short_acc = round(tn*1.0/(tn+fn+1e-10), 4)
        m = {"rmse":rmse, "tp":tp, "fp":fp, "fn":fn, "tn":tn, "acc":acc, "long_acc":long_acc, "short_acc":short_acc, "gain":gain, "long_gain":long_gain, "short_gain":short_gain}
        logger.info("rmse={}, tp={}, fp={}, fn={}, tn={}, acc={}, long_acc={}, short_acc={}, gain={}, long_gain={}, short_gain={}".format(round(m['rmse'],4), m['tp'], m['fp'], m['fn'], m['tn'] ,format(m['acc'],'.2%'), format(m['long_acc'],'.2%'), format(m['short_acc'],'.2%'), format(m['gain'],'.2%'), format(m['long_gain'],'.2%'), format(m['short_gain'],'.2%')))
        self.sum_metrics(m)
        return m



