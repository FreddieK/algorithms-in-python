import unittest
from decisiontree.decisiontree import DecisionTree
import pandas as pd
from sklearn.datasets import load_iris


class TestDecisionTree(unittest.TestCase):
    # Next Steps
    # - don't keep y as dataframe (or find efficient conversion)
    # - Write GBM that can use the trees to make more powerful predictions

    @classmethod
    def setUpClass(self):
        iris = load_iris()
        self.df = pd.DataFrame(iris.data, columns=iris.feature_names)

        self.y = pd.DataFrame(self.df['sepal width (cm)'])
        self.x = pd.DataFrame(self.df.drop('sepal width (cm)', axis=1))
        self.tree = DecisionTree(5, 5)
        self.tree.build_tree(self.x, self.y)

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
        self.assertTrue(type(self.tree._tree) is dict)
        self.assertIn('depth', self.tree._tree)

    def test_prediction_using_multiple_features(self):
        row = self.x.iloc[0]
        result = self.tree.predict(row)
        self.assertEqual(result, 3.60625)

    def test_can_predict_for_df(self):
        rows = self.x.iloc[0:10]
        result = self.tree.predict(rows)
        self.assertTrue(len(result) == 10)

    def test_can_validate_result(self):
        y = self.y.iloc[0:10, 0]
        rows = self.x.iloc[0:10]
        y_pred = self.tree.predict(rows)
        result = self.tree.score(y, y_pred)
        self.assertEqual(result, 0.16790909090909079)

    @unittest.skip
    def test_can_use_categorical_features(self):
        self.fail()

    @unittest.skip
    def test_equal_result_to_sklearn_regressiontree(self):
        # Manually verified for Boston data set, though
        # - Root should be lvl 0, not one, comparing to sklearn
        # - SKlearn uses <= as splitting criteria, which means split point is
        # the clostest smaller value to the one used by me
        self.fail()