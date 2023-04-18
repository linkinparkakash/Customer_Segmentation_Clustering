import pandas as pd
import os

class DataValidator:
    
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            def validate(self):
                if not self.is_csv():
                    raise ValueError("File is not in CSV format")
                
                df = pd.read_csv(self.filepath)
                columns = ['ID', 'Gender', 'Ever_Married', 'Age', 'Graduated', 'Profession', 
                        'Work_Experience', 'Spending_Score', 'Family_Size', 'Var_1', 'Segmentation']
                missing_cols = set(columns) - set(df.columns)
                
                if missing_cols:
                    raise ValueError(f"Dataset is missing the following columns: {missing_cols}")
                
                print("Dataset is valid.")
            
            def is_csv(self):
                _, extension = os.path.splitext(self.filepath)
                return extension.lower() == '.csv'
        except Exception as e:
            print('An error has occured:', e)