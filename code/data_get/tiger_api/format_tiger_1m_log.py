# -*- coding: utf-8 -*-
import os,sys
import json
import pytz,time,datetime
import pandas as pd

def in_filter(f, filter):
    if not filter:
        return True
    filter = filter.split('_')
    for kw in filter:
        if kw in f:
            return True
    return False

def get_dir_result(dir_name, code, filter, output_dir):
    file_list = os.listdir(dir_name)
    timestamp_dict = {}
    output_list = []

    for f in file_list:
        if not in_filter(f, filter):
            continue
    
        print(f) 
        data_csv = pd.read_csv(dir_name+f)
        day_dict = {}
 
        for i in range(len(data_csv)):
            content = "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(data_csv.loc[i]['time'], data_csv.loc[i]['time_str'], data_csv.loc[i]['open'], data_csv.loc[i]['high'], data_csv.loc[i]['low'], data_csv.loc[i]['close'], data_csv.loc[i]['volume'])
            file_name = data_csv.loc[i]['time_str'].split(' ')[0]
            #print(file_name)
            if file_name not in day_dict:
                day_dict[file_name] = []
            day_dict[file_name].append(content)


        for key in day_dict:
            if os.path.exists(output_dir+key):
                with open(output_dir+key, 'r') as f:
                    day_dict[key].extend(f.readlines())


        for key in day_dict:
            day_dict[key] = sorted(list(set(day_dict[key])))
            with open(output_dir+key, 'w') as f:
                for line in day_dict[key]:
                    f.write(line)
                
        


if __name__ == "__main__":
    code = sys.argv[1]
    dir_name = "/root/program_trading/data/tiger_1m_log/{}/".format(code)
    filter = None
    if(len(sys.argv) == 3):
        filter = sys.argv[2]
    output_dir = "/root/program_trading/data/tiger_1m_log_after/{}/".format(code)
    
    get_dir_result(dir_name, code, filter, output_dir) 
