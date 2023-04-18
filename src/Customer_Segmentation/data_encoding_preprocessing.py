import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

class DataEncoder:
    def __init__(self):
        pass
    try:
        def encode_csv(self, filepath):
            if not os.path.isfile(filepath):
                raise Exception("File path doesn't exist.")
            
            df = pd.read_csv(filepath)
            df.dropna(inplace=True)
            df.drop(columns=['ID'], inplace=True)

            # encode categorical columns
            categorical_cols = ['Gender', 'Ever_Married', 'Graduated', 'Profession', 'Spending_Score', 'Var_1']
            for col in categorical_cols:
                encoder = LabelEncoder()
                df[col] = encoder.fit_transform(df[col])

            return df
    except Exception as e:
        print('An error has occured', e)
