import unittest
from algorithms.randomforest import RandomForest
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split


class TestRandomForest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        np.random.seed(1337)

        data = load_boston()
        x = data.data
        y = data.target

        x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                            test_size=0.2)

        x_train = pd.DataFrame(x_train, columns=data.feature_names)

        self.model = RandomForest(5, 4, 5, 5)
        self.model.train(x_train, y_train)

        self.x_train = x_train
        self.y_train = y_train
        self.x_test = pd.DataFrame(x_test, columns=data.feature_names)
        self.y_test = y_test

    def test_can_import_class(self):
        self.assertEqual(type(self.model), RandomForest)

    def test_can_train_model(self):
        self.assertEqual(len(self.model.trees), 5)

    def test_can_make_predictions(self):
        y_pred_test = self.model.predict(self.x_test)
        mae_test = np.sum(abs(self.y_test - y_pred_test)) / len(self.y_test)

        self.assertEqual(mae_test, 3.1197613225896164)
