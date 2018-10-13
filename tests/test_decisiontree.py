import unittest
from decisiontree.decisiontree import DecisionTree
import pandas as pd
from sklearn.datasets import load_iris


class TestDecisionTree(unittest.TestCase):
    # Next Steps
    # - Write GBM that can use the trees to make more powerful predictions

    def setUp(self):
        iris = load_iris()
        self.df = pd.DataFrame(iris.data, columns=iris.feature_names)

    def test_can_import(self):
        tree = DecisionTree()
        self.assertTrue(type(tree) is DecisionTree)

    def test_prediction(self):
        y = pd.DataFrame(self.df['sepal width (cm)'])
        x = pd.DataFrame(self.df.drop('sepal width (cm)', axis=1))

        tree = DecisionTree()
        tree.build_tree(x, y)

        result = tree.predict_v2(5)

        self.assertEqual(result, 3.090625)

    def test_can_build_tree_using_multiple_continuous_features(self):
        y = pd.DataFrame(self.df['sepal width (cm)'])
        x = pd.DataFrame(self.df.drop('sepal width (cm)', axis=1))

        tree = DecisionTree()
        tree.build_tree(x, y)

        self.assertTrue(type(tree._tree) is dict)
        self.assertIn('depth', tree._tree)

    @unittest.skip
    def test_can_predict_for_df(self):
        self.fail()

    @unittest.skip
    def test_can_use_categorical_features(self):
        self.fail()
