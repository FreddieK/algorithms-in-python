from decisiontree.decisiontree import DecisionTree
import numpy as np
import pandas as pd


class GBM:

    def __init__(self, nr_trees=10, learning_rate=0.5):
        self.nr_trees = nr_trees
        self.learning_rate = learning_rate
        self.mae = None

    def train(self, X_df, y):
        y_pred = np.mean(y)
        mae = list()
        mae.append(DecisionTree.score(y, y_pred)) # initial model

        for i in range(self.nr_trees):
            dx = y - y_pred # L2 Loss
            dx_df = pd.DataFrame(dx) # refactor this
            dx_df.columns = ['y']

            tree = DecisionTree()
            tree.build_tree(X_df, dx_df)
            y_pred += self.learning_rate * np.array(tree.predict(X_df))

            mae.append(DecisionTree.score(y, y_pred))

        self.mae = mae

        # needs to store each tree in order to later make prediction