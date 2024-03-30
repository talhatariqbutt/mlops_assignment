import unittest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import pickle

from i202652_i200951 import imdb_df, X_train, X_test, y_train, y_test, model

class TestImdbModel(unittest.TestCase):

    def test_data_loading(self):
        self.assertIsInstance(imdb_df, pd.DataFrame)
        self.assertEqual(imdb_df.shape[0], 100)

    def test_data_preprocessing(self):
        self.assertEqual(imdb_df['review'].dtype, 'object')
        
    def test_train_test_split(self):
        self.assertEqual(len(X_train), 80) 
        self.assertEqual(len(X_test), 20) 

    def test_model_training(self):
        self.assertIsInstance(model, LogisticRegression)

    def test_model_evaluation(self):
        score = model.score(X_test, y_test)
        self.assertGreater(score, 0.5)

    def test_model_saving(self):
        try:
            with open('model.pkl', 'wb') as f:
                pickle.dump(model, f)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Model saving failed: {e}")

if __name__ == '__main__':
    unittest.main()
