from flask import Flask, render_template, request, send_file
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictions', methods=['POST'])
def predictions():
    try:
        # get the file path from the form
        filepath = request.form['filepath']
        
        # check if the file path exists
        if not os.path.isfile(filepath):
            raise Exception("File path doesn't exist.")
        
        # read in the CSV file and drop the 'ID' column
        df = pd.read_csv(filepath)
        df.dropna(inplace=True)
        df.drop(columns=['ID'], inplace=True)

        # encode categorical columns
        categorical_cols = ['Gender', 'Ever_Married', 'Graduated', 'Profession', 'Spending_Score', 'Var_1']
        for col in categorical_cols:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col])

        # load the joblib model and make predictions
        model = joblib.load('kmeans_model.joblib')
        predictions = model.predict(df)

        # save the predictions to a CSV file in the same location as the input file
        output_filepath = os.path.splitext(filepath)[0] + '_predictions.csv'
        if os.path.isfile(output_filepath):
            raise Exception("Output file already exists.")
        df['Segmentation'] = predictions
        df.to_csv(output_filepath, index=False)

        return send_file(output_filepath, as_attachment=True)

    except Exception as e:
        print('An error has occurred', e)
        return 'An error has occurred: {}'.format(e)

if __name__ == '__main__':
    app.run(debug=True)
