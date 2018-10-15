from algorithms.decisiontree import DecisionTree
import numpy as np
import pandas as pd


class GBM:
    mae = None
    models = None
    initial_model = None

    def __init__(self, nr_trees=10, learning_rate=0.5):
        self.nr_trees = nr_trees
        self.learning_rate = learning_rate

    def train(self, x, y):
        self.initial_model = np.mean(y)
        y_pred = self.initial_model

        mae, models = [], []
        mae.append(DecisionTree.score(y, y_pred))

        for i in range(self.nr_trees):
            dx = y - y_pred  # L2 Loss
            dx_df = pd.DataFrame(dx)  # refactor this
            dx_df.columns = ['y']

            tree = DecisionTree()
            tree.build_tree(x, dx_df)
            y_pred += self.learning_rate * np.array(tree.predict(x))

            models.append(tree)
            mae.append(DecisionTree.score(y, y_pred))

        self.models = models
        self.mae = mae

    def predict(self, x):
        y_pred = self.initial_model
        for i in range(self.nr_trees):
            tree = self.models[i]
            y_pred += self.learning_rate * np.array(tree.predict(x))
        return y_pred
