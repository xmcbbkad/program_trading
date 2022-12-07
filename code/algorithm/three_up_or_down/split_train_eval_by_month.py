# coding: utf-8

import os
import re
import pandas as pd
import numpy as np
import logging

from data_load.data_loader import DataLoader
from evaluate.evaluator import Evaluator
from algorithm.three_up_or_down.three_up_or_down import Three_up_or_down

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def split_train_eval_by_month(data_dir, feature_file):
    model = Three_up_or_down()
    month = []
    for filename in sorted(os.listdir(data_dir)):
        month.append(filename[:7])
    month = sorted(list(set(month)))

    evaluator = Evaluator()
    random_evaluator = Evaluator()
    for i in range(len(month)):
        data_loader = DataLoader(feature_file=feature_file)
        df_eval = data_loader.load_data_from_dir(data_dir=data_dir, pattern=month[i], not_pattern='ffff')
        x_eval, y_eval = data_loader.split_x_y(df=df_eval, label='t0_close_ratio_last')
        logger.info('------------------------------')

        y_pred = model.predict(x_eval)

        logger.info("eval_month={}".format(month[i]))
        g = evaluator.cal_metrics(y_eval.values, y_pred)

        logger.info("gain={}, long_gain={}, short_gain={}".format(format(evaluator.all_m['gain'],'.2%'), format(evaluator.all_m['long_gain'],'.2%'), format(evaluator.all_m['short_gain'],'.2%')))

        logger.info('random_metrics:')
        rg = random_evaluator.cal_random_metrics(y_eval.values)
        logger.info("random_gain={}, random_long_gain={}, random_short_gain={}".format(format(random_evaluator.all_m['gain'],'.2%'), format(random_evaluator.all_m['long_gain'],'.2%'), format(random_evaluator.all_m['short_gain'],'.2%')))
       



if __name__ == '__main__':
    #split_train_eval_by_month(data_dir='/Users/xiaokunfan/code/program_trading/data/taobao_TSLA_5mins_features_2019_2022', feature_file='/Users/xiaokunfan/code/program_trading/code/data_process/features_5mins.txt')
    split_train_eval_by_month(data_dir='/Users/xiaokunfan/code/program_trading/data/tiger_1m_log_after/TSLA_5mins_features', feature_file='/Users/xiaokunfan/code/program_trading/code/data_process/features_5mins.txt')
    exit(0)


