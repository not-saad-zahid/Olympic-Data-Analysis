import pandas as pd


def preprocess(df, region_df):
    # Filtering on Summer Season
    df = df[df['Season'] == 'Summer']
    # merging region with df on NOC
    df = df.merge(region_df, on = 'NOC', how = 'left')
    df.drop_duplicates(inplace=True)
    # Applying OHE on Medal and concatinate with original df
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
