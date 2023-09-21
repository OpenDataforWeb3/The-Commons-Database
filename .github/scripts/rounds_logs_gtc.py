import pandas as pd
import numpy as np
import datetime
from datetime import  timedelta
import re
import os
import requests
from supabase import create_client
from dotenv import load_dotenv


load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
print(url,key)
supabase = create_client(url, key)

def rounds_info(chain_id, start_time, end_time):
    chain_url = 'https://indexer-grants-stack.gitcoin.co/data/' + chain_id + '/rounds.json'
    try:
        response = requests.get(chain_url)
        if response.status_code == 200:
            chain_data = response.json()
            rounds = []
            for round in chain_data:
                if round['metadata'] is not None:
                    try:
                        round_data = {
                            'chainId' : chain_id,
                            'id': round['id'],
                            'grantsProgramRoundId': round['metadata']['name'],
                            'roundStartTime': datetime.datetime.utcfromtimestamp(int(round['roundStartTime'])), # create a datetime object from the timestamp in UTC time
                            'roundEndTime': datetime.datetime.utcfromtimestamp(int(round['roundEndTime']))
                        }
                        rounds.append(round_data)
                    except:
                        continue    
            df = pd.DataFrame(rounds)
            df = df[(df['roundStartTime'] >= start_time) & (df['roundEndTime'] <= end_time)]
            return df 
    except: 
        return pd.DataFrame()
    
#getting last update date and getting rounds that were indexed after the last update
table_name = 'rounds_logs'
lastUpdatedAt = supabase.table(table_name).select('createdAt').execute()
lastUpdatedAt = pd.DataFrame.from_dict(lastUpdatedAt.data).max()[0]
lastUpdatedAt = datetime.datetime.strptime(lastUpdatedAt, '%Y-%m-%dT%H:%M:%S.%f')
lastUpdatedAt = datetime.datetime(lastUpdatedAt.year, lastUpdatedAt.month, lastUpdatedAt.day, 23, 59, 0)


#getting rounds that were creted between the specified date 
days_to_offset = 4
chainIds = ['1','10','250', '42161', '421613', '424', '5', '58008']
start_time = lastUpdatedAt -  timedelta(days=days_to_offset)
end_time = lastUpdatedAt


chain_data_df = pd.DataFrame()

for chain_id in chainIds:

    chain_data = rounds_info(chain_id, start_time, end_time)
    chain_data_df = pd.concat([chain_data_df, chain_data], axis= 0 ) 
    chain_data_df.reset_index(inplace = True, drop= True)
    
    
chain_data_df.reset_index( inplace = True)
chain_data_df['grantsProgram'] = 'gitcoin_rounds'    
chain_data_df['roundStartTime'] = chain_data_df['roundStartTime'].apply(lambda x: str(x))
chain_data_df['roundEndTime'] = chain_data_df['roundEndTime'].apply(lambda x: str(x))
chain_data_df['createdAt'] = str(datetime.datetime.now())

table_name = 'rounds_logs'

supabase.table(table_name).upsert(chain_data_df.to_dict(orient='records')).execute()
