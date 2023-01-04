#Simple api where you could get the data
#Add post, get, delete later

from flask import Flask, jsonify
import pandas as pd
app = Flask(__name__)

@app.route('/tehokkainjuoma')
def get_data():
    df = pd.read_csv('Tehokkainjuoma')
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run()
