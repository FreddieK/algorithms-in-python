import unittest
from decisiontree.decisiontree import DecisionTree
import pandas as pd
from sklearn.datasets import load_iris


class TestDecisionTree(unittest.TestCase):
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