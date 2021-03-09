# get predictions needs to be a separate function as it just needs to get the 
# predictions 
from flask import Flask, request, jsonify
from flask_cors import CORS 
from diagnoser import Train_Diagnosis
from predictor import Predictions
import pickle
import numpy as np
## 1. prediction 
## moreover, model and vectorizer need not be loaded again and again

# build 1 end point
app = Flask(__name__)
CORS(app)

def load_from_pickle(file):
    loaded = pickle.load(open(file,'rb'))
    return loaded

# got the models     

# parameter 1 -> 
    # processes the query given by the site and make prediction   

@app.route('/process',methods = ['GET'])
def get_diagnosis():

    vectorizer = load_from_pickle('models/vectorizer.pkl')
    model = load_from_pickle('models/model.pkl')

    trainer = Train_Diagnosis()
    ailments = trainer.get_ailments(1)
    diagnoser = Predictions(model,'data/trial_data.csv')

    q = request.args.get('query')
    processed = diagnoser.process_query(q)
    
    # now transform
    query = [processed]
    query = vectorizer.transform(query)
    
    # and predict 
    preds = model.predict_proba(query)
    res = list(np.argsort(preds))[0]
    res = res[::-1][:3] # top 3 
    ailment_top = ailments[res[0]]
    
    # append record to the data
    diagnoser.append_query(query,ailment_top)
    
    #gather predictions 
    predictions = []
    for k in res: 
        predictions.append(ailments[k])

# parameter point 2 -> 
    # re-trains the model on the acquired data and 
    # reloads model and vectorizer 
    
    # 0 -> do not train 
    # 1 -> train again 
    train = int(request.args.get('train')) # ->
    if(train is not None and train == 1):
        # means I need to train along with this query 
        trainer.train_model()
        # at this point load the vectorizer and model again 
        # with the new queries
        vectorizer = load_from_pickle('models/vectorizer.pkl')
        model = load_from_pickle('models/model.pkl')
    
    return jsonify(predictions)


if __name__=='__main__':
    app.run(port = 5000, debug = True)