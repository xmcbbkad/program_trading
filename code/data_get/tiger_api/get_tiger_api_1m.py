# -*- coding: utf-8 -*-
import datetime
import time
import pytz
import logging
import pandas as pd
from tigeropen.common.consts import Language, BarPeriod
from tigeropen.quote.domain.filter import OptionFilter
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='a', )
logger = logging.getLogger('TigerOpenApi')


def get_client_config():
    """
    https://www.itiger.com/openapi/info 开发者信息获取
    :return:
    """
    is_sandbox = False
    client_config = TigerOpenClientConfig(sandbox_debug=is_sandbox)
    client_config.private_key = read_private_key('/root/tiger/rsa_private_key.pem')
    client_config.tiger_id = '20150578'
    client_config.account = 'U8677892'  # 环球账户
    client_config.standard_account = None  # 标准账户
    client_config.paper_account = None  # 模拟账户
    client_config.language = Language.en_US
    return client_config


client_config = get_client_config()
openapi_client = QuoteClient(client_config, logger=logger)

def ts2str(ts):
    ts = ts/1000
    str = datetime.datetime.fromtimestamp(ts, pytz.timezone('America/New_York')).strftime('%Y-%m-%d %H:%M:%S GMT%z')
    return str

def get_1m_data(code):
    tz = pytz.timezone('America/New_York')
    file_name = datetime.datetime.now(tz).strftime('%Y-%m-%d')
    ts = (int(time.time())-86400*5)*1000 
    bars = openapi_client.get_bars(symbols=[code], begin_time=ts, period=BarPeriod.ONE_MINUTE, limit=5000)
    
    time_str = bars['time'].apply(ts2str)
    bars.insert(1, 'time_str', time_str)
   
     
    #with open("../data/tiger_1m_log/{}/{}_{}".format(code, file_name, code), 'a+') as f:
    bars.to_csv("../data/tiger_1m_log/{}/{}_{}".format(code, file_name, code), index=0)

if __name__ == '__main__':
    get_1m_data(".IXIC")
    time.sleep(10)
    get_1m_data("TSLA")
    time.sleep(10)
    get_1m_data("AAPL")
    time.sleep(10)
    get_1m_data("AMD")
    time.sleep(10)
    get_1m_data("NVDA")
    time.sleep(10)
    get_1m_data("FB")
    time.sleep(10)
    get_1m_data("MSFT")
    time.sleep(10)
    get_1m_data("GOOG")
    time.sleep(10)
    get_1m_data("AMZN")
