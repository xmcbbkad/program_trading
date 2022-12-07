# coding: utf-8

import pandas as pd
import numpy as np
import logging

from data_load.data_loader import DataLoader
from evaluate.evaluator import Evaluator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Three_up_or_down():
    def __init__(self):
        super(Three_up_or_down, self).__init__()

    def predict(self, data):
        
        eval_y = np.full([len(data)], fill_value=-1, dtype=float)
        for i in range(len(data)):
            if data.iloc[i]['t1_close_ratio_last'] > 1.002 and data.iloc[i]['t2_close_ratio_last'] > 1.002 and data.iloc[i]['t3_close_ratio_last'] > 1.002:
                eval_y[i] = 1.5
            elif data.iloc[i]['t1_close_ratio_last'] < 0.998 and data.iloc[i]['t2_close_ratio_last'] < 0.998 and data.iloc[i]['t3_close_ratio_last'] > 0.998:
                eval_y[i] = 0.5
            

        return eval_y
            
if __name__ == '__main__':
    pass
