from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from joblib import dump, load
from datetime import datetime

class Machine:

    def __init__(self, df):
        self.name = "Random Forest Classifier"
        # df['Rarity'] = df['Rarity'].apply(lambda x: int(x.replace('Rank ', '')))
        self.target = df['Rarity']
        self.features = df.drop(columns='Rarity')
        self.model = RandomForestClassifier()
        self.model.fit(self.features, self.target)

    def __call__(self, feature_basis):
        prediction = self.model.predict(feature_basis)[0]
        probability = self.model.predict_proba(feature_basis)
        confidence = np.max(probability, axis=1)
        return prediction, confidence[0]

    def save(self, filepath):
        dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        model = load(filepath)
        machine_instance = Machine.__new__(Machine)
        machine_instance.model = model
        machine_instance.name = "Random Forest Classifier"
        machine_instance.initialized_at = datetime.now()
        return machine_instance

    def info(self):
        timestamp_str = self.initialized_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"Base Model: {self.name}, Timestamp: {timestamp_str}"
