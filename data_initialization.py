import pandas as pd


def initialize_data():
    # Load the dataset
    df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

    df.drop(columns=['ADDRESSLINE2'], inplace=True)
    df['STATE'] = df['STATE'].fillna(value='Unknown', inplace=True)
    df['POSTALCODE'] = df['POSTALCODE'].fillna(value='0', inplace=True)
    df['TERRITORY'] = df['TERRITORY'].fillna(value='Unknown', inplace=True)

    return df