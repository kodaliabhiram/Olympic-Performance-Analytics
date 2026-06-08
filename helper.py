import pandas as pd

def preprocess():
    df = pd.read_csv('data/athlete_events.csv')
    regions = pd.read_csv('data/noc_regions.csv')

    df = df.merge(regions, on='NOC', how='left')

    return df