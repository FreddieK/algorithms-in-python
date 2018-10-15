import unittest
from decisiontree.gbm import GBM
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

class TestGBM(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        data = load_boston()
        X = data.data

        self.y = data.target
        self.X_df = pd.DataFrame(X, columns=data.feature_names)

        self.model = GBM(3, 0.5)
        self.model.train(self.X_df, self.y)

    def test_can_import_class(self):
        model = GBM()
        self.assertEqual(type(model), GBM)

    def test_mae_decreases(self):
        self.assertEqual(self.model.mae, [6.647207423956008,
                                          4.64223543227224,
                                          3.5060203764688502,
                                          3.0035297382705246])

    def test_can_predict_with_model(self):
        breakpoint()
        x_pred = self.X_df[]