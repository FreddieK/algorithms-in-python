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

    def test_prediction_using_one_feature(self):
        y = pd.DataFrame(self.df['sepal width (cm)'])
        x = pd.DataFrame(self.df['sepal length (cm)'])
        tree = DecisionTree()
        tree.build_tree(x, y)

        row = x.iloc[0]
        result = tree.predict(row)

        self.assertEqual(result, 3.5)

    def test_can_build_tree_using_multiple_continuous_features(self):
        y = pd.DataFrame(self.df['sepal width (cm)'])
        x = pd.DataFrame(self.df.drop('sepal width (cm)', axis=1))
        tree = DecisionTree()
        tree.build_tree(x, y)

        self.assertTrue(type(tree._tree) is dict)
        self.assertIn('depth', tree._tree)

    def test_prediction_using_multiple_features(self):
        y = pd.DataFrame(self.df['sepal width (cm)'])
        x = pd.DataFrame(self.df.drop('sepal width (cm)', axis=1))
        tree = DecisionTree(5, 5)
        tree.build_tree(x, y)

        row = x.iloc[0]
        result = tree.predict(row)
        self.assertEqual(result, 3.60625)

    def test_can_predict_for_df(self):
        y = pd.DataFrame(self.df['sepal width (cm)'])
        x = pd.DataFrame(self.df.drop('sepal width (cm)', axis=1))
        tree = DecisionTree(5, 5)
        tree.build_tree(x, y)

        rows = x.iloc[0:10]
        result = tree.predict(rows)
        self.assertTrue(len(result) == 10)

    @unittest.skip
    def test_can_validate_result(self):
        self.fail()

    @unittest.skip
    def test_can_use_categorical_features(self):
        self.fail()
