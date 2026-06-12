import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

def train():
    if not os.path.exists('data.csv'):
        print("Dataset missing!")
        return

    df = pd.read_csv('data.csv')
    
    if len(df) > 1:
        print(f"Training ML Model on {len(df)} records...")
        X = [[i] for i in range(len(df))]
        y = df['Age'].values
        
        model = LinearRegression()
        model.fit(X, y)

        with open('model.pkl', 'wb') as f:
            pickle.dump(model, f)
        
        print("Success: model.pkl updated!")
    else:
        print("Wait: Add at least 2 records to train.")

if __name__ == "__main__":
    train()