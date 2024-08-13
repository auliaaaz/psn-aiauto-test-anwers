import pandas as pd
import numpy as np

def load_and_prepare_data(filepath):
    # read csv file
    df = pd.read_csv(filepath)
    
    # data imputation
    df['Value'] = df['Value'].replace('Null', np.nan)
    df_imputed = df.ffill()
    
    df_imputed['Value'] = df_imputed['Value'].astype('int')

    # convert epoch time to datetime
    df_imputed['DateTime'] = pd.to_datetime(df_imputed['DateTime'])

    return df_imputed

def calculate_downtime(df):
    mask = df.Value == 1
    next_time = df.DateTime.shift(-1)
    downtime = (next_time - df.DateTime).dt.total_seconds()
    total_down = downtime[mask].sum()
    
    return total_down

if __name__ == "__main__":
    # path to csv file
    filepath = 'path_to_file\device_network_data.csv'
    device_net_imputed = load_and_prepare_data(filepath)
    total_downtime = calculate_downtime(device_net_imputed)
    print(f"Total Downtime: {total_downtime} seconds")
