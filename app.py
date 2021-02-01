from flask import *
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import json
import pickle
app = Flask(__name__)
app.debug = True
app.secret_key = 'Ranuga D 2008'
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        date = request.form['D']
        date = date.replace('-','')
        country = request.form['C']
        json_info = json.load(open('./country_info.json','r'))
        model = pickle.load(open('./model.pkl','rb'))
        array = np.array([date,country])
        df = pd.DataFrame(array)
        try:
            result = model.predict(df)
        except:
            result = model.predict(df.T)
        flash(f'Total Cases : {round(result[0][0])} | Total Recover : {round(result[0][1])} | Total Deaths : {round(result[0][2])}','success')
        return redirect('/')
    else:
        json_info = json.load(open('./country_info.json','r'))
        return render_template('index.html',zip=zip,json_info=json_info,list=list)

if __name__ == "__main__":
    app.run(host='192.168.1.9')