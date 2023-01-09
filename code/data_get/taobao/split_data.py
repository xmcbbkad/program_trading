import pandas as pd
import csv
import datetime

input_file = "/Users/xiaokunfan/code/program_trading/data/taobao_new_TSLA/TSLA.csv"
output_dir = "/Users/xiaokunfan/code/program_trading/data/taobao_new_TSLA/TSLA"

dt = pd.read_csv(input_file)
dt = dt.iloc[::-1]
dt.loc[:, 'ts'] = dt.apply(lambda row: str(int(datetime.datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S').timestamp()*1000)), axis=1)

dt = dt[['ts', 'date', 'open', 'high', 'low', 'close', 'volume']]

last_date = ""
f = None
for i in range(len(dt)):
    date = dt.iloc[i]['date'].split()[0]
    if date != last_date:
        if f:
            f.close()
        f = open("{}/{}".format(output_dir, date),"w+")
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(dt.iloc[i])
        last_date = date
    else:
        writer.writerow(dt.iloc[i])
    
    if i == len(dt) -1:
        f.close()
