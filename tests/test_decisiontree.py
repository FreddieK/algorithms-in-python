import unittest
from decisiontree.decisiontree import DecisionTree
import pandas as pd
from sklearn.datasets import load_iris


class TestDecisionTree(unittest.TestCase):

    def test_can_import(self):
        tree = DecisionTree()
        self.assertTrue(type(tree) is DecisionTree)

    def test_prediction(self):
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        set_ = pd.DataFrame(data={'x': df['sepal length (cm)'],
                                  'y': df['sepal width (cm)']})
        tree = DecisionTree()
        iris = tree.iterate(set_)

        self.assertEqual(tree.predict(iris, 5), 3.090625)