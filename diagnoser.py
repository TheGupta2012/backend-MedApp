import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.ensemble import RandomForestClassifier


class Train_Diagnosis:
    """
    This class is actually used to train and update the model and the data that I have
    Prediction is going to be done through a function.

    Class to predict the ailment based on the textual information provided
    on the site
    ATTRIBUTES:
    data : the processed and lemmatized dataframe loaded from the memory (
    contains stemmed_data column and the prompt column)
    ailments_dict_keyname/_keyint : dictionaries representing the unique ailments present
                   in the data set
    vectorizer : TfIdf vectorizer used for transforming data
    ( based on the latest state of the data file)
    model :
    """

    def __init__(self):
        self.data = self.get_latest_data()
        self.ailments_dict_keyname = self.get_ailments(0)
        self.ailments_dict_keyint = self.get_ailments(1)
        self.vectorizer = self.get_vectorizer()
        self.model = self.get_model()
        self.vector_path = "models/vectorizer.pkl"
        self.model_path = "models/model.pkl"

    def get_latest_data(self):
        """Function to load in the latest dataframe
        that you have for the model training"""
        data = pd.read_csv(r"data/trial_data.csv")
        return data

    def get_ailments(self, type_of_dict):
        """Function to load the unique ailment dictionary
        PARAMETERS: type_of_dict: 0,1 : how to form the
                     keys of the dictionary
        RETURNS : dictionary of the ailments"""
        D = {}
        ailments = self.data["Prompt"].unique()
        if type_of_dict == 0:
            # By name
            for i, k in enumerate(ailments):
                D[k] = i
        else:
            # By indexing
            for i, k in enumerate(ailments):
                D[i] = k
        return D

    def get_vectorizer(self):
        """Return a vectorizer to fit on the data"""
        TfIdf = TfidfVectorizer(stop_words="english", ngram_range=(1, 3), max_df=0.7)
        return TfIdf

    def get_training_x(self):
        """Returns the transformed data for training"""
        X = (self.vectorizer).fit_transform(self.data["stemmed_phrase"])
        X = X.toarray()
        # update the vectorizer here
        self.vectorizer = self.vectorizer.fit(self.data["stemmed_phrase"])
        # save the vectorizer at this point, after you have fit it
        pickle.dump(self.vectorizer, open(self.vector_path, "wb"))
        return X

    def get_training_y(self):
        """Returns the encoded classes for training"""
        Y = self.data["Prompt"].map(self.ailments_dict_keyname)
        return Y

    def get_model(self):
        """Returns a model for the data"""
        M = RandomForestClassifier(n_estimators=36, min_samples_leaf=2)
        return M

    # METHODS
    # 1. Trains the model

    def train_model(self):
        """Trains the model as and when you want
        with the loaded data"""
        X = self.get_training_x()
        Y = self.get_training_y()
        # validation is actually done on the query not the test data
        self.model.fit(X, Y)
        pickle.dump(self.model, open(self.model_path, "wb"))

        # that's it
