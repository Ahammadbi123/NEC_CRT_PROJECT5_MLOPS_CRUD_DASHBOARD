from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import subprocess

app = Flask(__name__)
CSV_FILE = 'data.csv'

# Ensure CSV exists
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=['Name', 'Age']).to_csv(CSV_FILE, index=False)

def read_data():
    return pd.read_csv(CSV_FILE)

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

@app.route('/')
def index():
    df = read_data()
    records = df.to_dict(orient='records')
    stats = {
        'total': len(df),
        'avg': round(df['Age'].mean(), 1) if len(df) > 0 else 0,
        'trained': os.path.exists('model.pkl')
    }
    
    # Edit logic
    edit_id = request.args.get('edit_id')
    edit_data = None
    if edit_id is not None:
        try:
            edit_data = records[int(edit_id)]
        except:
            edit_id = None
            
    return render_template('index.html', records=records, stats=stats, edit_id=edit_id, edit_data=edit_data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    age_raw = request.form.get('age')
    edit_id = request.form.get('edit_id')
    
    try:
        age = int(age_raw)
    except:
        age = 0

    df = read_data()
    if edit_id: # UPDATE
        idx = int(edit_id)
        df.at[idx, 'Name'] = name
        df.at[idx, 'Age'] = age
    else: # CREATE
        new_row = pd.DataFrame([[name, age]], columns=['Name', 'Age'])
        df = pd.concat([df, new_row], ignore_index=True)
    
    save_data(df)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    df = read_data()
    df = df.drop(index=id)
    save_data(df)
    return redirect(url_for('index'))

@app.route('/retrain')
def retrain():
    subprocess.run(["python", "train.py"])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)