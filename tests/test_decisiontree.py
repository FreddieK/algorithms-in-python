import unittest
from decisiontree.decisiontree import DecisionTree
import pandas as pd
from sklearn.datasets import load_iris


class TestDecisionTree(unittest.TestCase):
    # Next Steps
    # - Implement support for handling multiple features (including categorical)
    # - Support taking DF for predictions, to properly assess performance
    # - Write GBM that can use the trees to make more powerful predictions

    def setUp(self):
        iris = load_iris()
        self.df = pd.DataFrame(iris.data, columns=iris.feature_names)

    def test_can_import(self):
        tree = DecisionTree()
        self.assertTrue(type(tree) is DecisionTree)

    def test_prediction(self):
        set_ = pd.DataFrame(data={'x': self.df['sepal length (cm)'],
                                  'y': self.df['sepal width (cm)']})
        tree = DecisionTree()
        tree.build_tree(set_)
        result = tree.predict(5)

        self.assertEqual(result, 3.090625)

    @unittest.skip
    def test_can_use_multiple_features(self):
        self.fail()
