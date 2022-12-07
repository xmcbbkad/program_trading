# coding: utf-8

import os
import re
import lightgbm as lgb
import pandas as pd
import numpy as np
import logging

from data_load.data_loader import DataLoader
from evaluate.evaluator import Evaluator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Lightgbm4pt():
    def __init__(self):
        super(Lightgbm4pt, self).__init__()

        #https://lightgbm.apachecn.org/#/docs/6
        self.params = {
            "task" : "train",
            "boosting_type" : "gbdt",
            "objective" : "regression",
            "metric" : "l2",
            "max_bin" : 255,
            "num_iterations" : 100,
            "learning_rate" : 0.02,
            "num_leaves" : 31,
            "min_data_in_leaf" : 10,
            "feature_fraction" : 1,
            "bagging_fraction": 1,
        }

    def train(self, x_train, y_train, x_eval, y_eval, model_path='model.txt'):
        lgb_train = lgb.Dataset(x_train, y_train)
        lgb_eval = lgb.Dataset(x_eval, y_eval)

        #callbacks = [lgb.log_evaluation(period=100), lgb.early_stopping(stopping_rounds=30)]
        #callbacks = [lgb.early_stopping(stopping_rounds=10)]
        callbacks=[]
        self.gbm = lgb.train(self.params,
                        lgb_train,
                        valid_sets=lgb_eval,
                        callbacks=callbacks)

        logger.info("saving model...")
        self.gbm.save_model(model_path)

    def predict(self, test_data, model_path='model.txt'):
        if model_path:
            self.gbm = lgb.Booster(model_file=model_path)
        y_pred = self.gbm.predict(test_data, num_iteration=self.gbm.best_iteration)
        return y_pred

    def feature_importance(self, feature_names):
        logger.info(pd.DataFrame({
                'column': feature_names[1:],
                'importance': self.gbm.feature_importance(),
            }).sort_values(by='importance', ascending=False))


   
if __name__ == '__main__':
    lightgbm4pt = Lightgbm4pt()
    lightgbm4pt.split_train_eval_by_month(data_dir='/Users/xiaokunfan/code/data/tiger_1m_log_after/NVDA_5mins_features', feature_file='/Users/xiaokunfan/code/candle_features/features.txt')
    #lightgbm4pt.split_train_eval_by_month(data_dir='/Users/xiaokunfan/code/data/taobao_TSLA_5mins_features_2019_2022')
    #lightgbm4pt.split_train_eval_by_month(data_dir='/Users/xiaokunfan/code/data/TSLA_5mins_features')
    exit(0)



    #x_train, y_train = lightgbm4pt.load_data_from_dir(data_dir='/Users/xiaokunfan/code/data/TSLA_5mins_features')
    x_train, y_train = lightgbm4pt.load_data_from_dir(data_dir='/Users/xiaokunfan/code/data/taobao_TSLA_5mins_features_2019_2022')
    x_eval, y_eval  = lightgbm4pt.load_data_from_dir(data_dir='/Users/xiaokunfan/code/data/TSLA_5mins_features', pattern='2022-11')
    #x_eval, y_eval  = lightgbm4pt.load_data_from_dir(data_dir='/Users/xiaokunfan/code/data/taobao_TSLA_5mins_features')

    lightgbm4pt.train(x_train, y_train, x_eval, y_eval)
    y_pred = lightgbm4pt.predict(x_eval)

    lightgbm4pt.cal_metrics(y_eval, y_pred)
    
    y_random = np.random.rand(len(y_pred))
    y_random += 0.5
    logger.info('random_metrics:')
    m = lightgbm4pt.cal_metrics(y_eval, y_random)


    #lightgbm4pt.feature_importance(feature_names=)

    exit(0)
    #--------------------------------------------------------------------------------

    pred_dir = '/Users/xiaokunfan/code/data/TSLA_5mins_features_202211'
    for filename in sorted(os.listdir(pred_dir)):
        df = lightgbm4pt.load_data_from_file(os.path.join(pred_dir, filename))
        x = df.drop('t0_close_ratio_last', axis=1).values
        y = df['t0_close_ratio_last'].values 

        y_pred = lightgbm4pt.predict(x)
        logger.info(filename)
        lightgbm4pt.cal_metrics(y, y_pred)
        lightgbm4pt.cal_metrics(y, y_pred)

        logger.info('random_metrics:')
        y_random = np.random.rand(len(y_pred))
        y_random += 0.5
        lightgbm4pt.cal_metrics(y, y_random)

        logger.info('--------------------------------------------------')

    x, y = lightgbm4pt.load_data_from_dir(data_dir=pred_dir)
    y_pred = lightgbm4pt.predict(x)
    lightgbm4pt.cal_metrics(y, y_pred)
    
    logger.info('random_metrics:')
    y_random = np.random.rand(len(y_pred))
    y_random += 0.5
    lightgbm4pt.cal_metrics(y, y_random)


