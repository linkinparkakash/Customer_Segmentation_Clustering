import pandas as pd
from sklearn.cluster import KMeans
import joblib

"""
This class is responisble for the clustering of the dataset and saving the model.
Author: Akash Pathania
Version: 1.0.0

"""

class KMeansModel:
    def __init__(self, n_clusters=4):
        self.n_clusters = n_clusters
        self.kmeans = KMeans(n_clusters=self.n_clusters)
    
    def fit(self, df):
        try:
            self.kmeans.fit(df)
        except Exception as e:
            print(f"An error occurred while fitting the model: {e}")
    
    def predict(self, df):
        try:
            labels = self.kmeans.predict(df)
            return labels
        except Exception as e:
            print(f"An error occurred while predicting labels: {e}")
    
    def score(self, df):
        try:
            accuracy = self.kmeans.score(df)
            print(f"Accuracy: {accuracy:.2f}")
        except Exception as e:
            print(f"An error occurred while computing accuracy: {e}")
    
    def save_model(self, filename):
        try:
            joblib.dump(self.kmeans, filename)
        except Exception as e:
            print(f"An error occurred while saving the model: {e}")

#  USAGE 

"""
# Load data
df = pd.read_csv("data.csv")

# Create KMeansModel instance
model = KMeansModel(n_clusters=4)

# Fit the model to the data
model.fit(df)

# Get cluster assignments for each instance
labels = model.predict(df)

# Print accuracy
model.score(df)

# Save the model
model.save_model("kmeans_model.joblib")
"""