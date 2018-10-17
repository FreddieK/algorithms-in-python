import numpy as np
import pandas as pd
from algorithms.decisiontree import RandomForestTree


class RandomForest:
    training_sets = None
    trees = None
    nr_features = None
    max_depth = None
    min_samples = None

    def __init__(self, nr_trees=15, nr_features=4, max_depth=15, min_samples=5):
        self.nr_trees = nr_trees
        self.nr_features = nr_features
        self.max_depth = max_depth
        self.min_samples = min_samples

    def train(self, x, y):
        df_train = x
        df_train['y'] = y

        self.training_sets = []
        self.trees = []

        for i in range(self.nr_trees):
            bootstrapped_set = df_train.sample(frac=1.0,
                                               replace=True)

            y = pd.DataFrame(bootstrapped_set['y'])
            x = pd.DataFrame(bootstrapped_set.drop('y', axis=1))

            self.training_sets.append({
                'x': x,
                'y': y,
            })
            tree = RandomForestTree(self.nr_features,
                                    self.max_depth,
                                    self.min_samples)
            tree.build_tree(x, y)
            self.trees.append(tree)

    def predict(self, x):
        predictions = [tree.predict(x) for tree in self.trees]
        predictions = np.asarray(predictions)
        return np.mean(predictions, axis=0)
