import numpy as np
import pandas as pd
#import random


class DecisionTree:
    def __init__(self, max_depth=3, min_samples=5):
        self.max_depth = max_depth
        self.min_samples = min_samples
        self._tree = {}

    @staticmethod
    def score(y, y_pred, metric='MAE'):
        # Only supports MAE for now

        if metric == 'MAE':
            return np.sum(abs(y - y_pred))/len(y)

    @staticmethod
    def _find_split(feature, x, y):
        best_sse = None
        best_split = None
        for value in feature:
            left_y = y[feature < value]
            right_y = y[~(feature < value)]
            sse = np.sum((left_y.mean() - left_y)**2) + \
                  np.sum((right_y.mean() - right_y)**2)

            if (best_sse is None) or (sse[0] < best_sse):
                best_sse = sse[0]
                best_split = {
                    'feature': feature.name,
                    'SSE': best_sse,
                    'split_point': value,
                    'left_x': x[feature < value],
                    'left_y': left_y,
                    'right_x': x[~(feature < value)],
                    'right_y': right_y,
                }
        return best_split

    def _iterate(self, x, y, node, depth=1):
        if depth >= self.max_depth:
            node['value'] = y.mean()[0]
            return
        if len(x) <= self.min_samples:
            node['value'] = y.mean()[0]
            return

        best_split = None
        for feature in x:
            potential_split = self._find_split(x[feature], x, y)
            if (best_split is None) or \
                (potential_split['SSE'] < best_split['SSE']):
                best_split = potential_split

        if len(best_split['left_y']) == 0 or len(best_split['right_y']) == 0:
            node['value'] = y.mean()[0]
            return

        node['feature'] = best_split['feature']
        node['split_point'] = best_split['split_point']
        node['split_SSE'] = best_split['SSE']
        node['depth'] = depth
        node['left'] = {}
        node['right'] = {}

        self._iterate(best_split['left_x'], best_split['left_y'],
                      node['left'], depth + 1)
        self._iterate(best_split['right_x'], best_split['right_y'],
                      node['right'], depth + 1)
        return node

    def build_tree(self, x, y):
        self._tree = self._iterate(x, y, {})

    def _predict(self, row, node):
        if 'value' in node:
            return node['value']
        feature = node['feature']
        if row[feature] < node['split_point']:
            return self._predict(row, node['left'])
        else:
            return self._predict(row, node['right'])

    def predict(self, rows):
        y = list()
        if type(rows) == pd.core.series.Series:
            return self._predict(rows, self._tree)
        for index, row in rows.iterrows():
            y.append(self._predict(row, self._tree))
        return y


class RandomForestTree(DecisionTree):
    # Changing the feature selection process to only look at a random subset
    # of features available

    def __init__(self, nr_features=4, max_depth=15, min_samples=2, **kwargs):
        super(RandomForestTree, self).__init__(max_depth, min_samples, **kwargs)
        self.nr_features = nr_features

    def _iterate(self, x, y, node, depth=1):
        if depth >= self.max_depth:
            node['value'] = y.mean()[0]
            return
        if len(x) <= self.min_samples:
            node['value'] = y.mean()[0]
            return

        best_split = None
        # Randomly choose features for tree
        x_subset = np.random.choice(list(x.columns),
                                    self.nr_features,
                                    replace=False)
        for feature in x_subset:
            potential_split = self._find_split(x[feature], x, y)
            if (best_split is None) or \
                    (potential_split['SSE'] < best_split['SSE']):
                best_split = potential_split

        # If a branch turned out empty, convert node into leaf
        if len(best_split['left_y']) == 0 or len(best_split['right_y']) == 0:
            node['value'] = y.mean()[0]
            return

        node['feature'] = best_split['feature']
        node['split_point'] = best_split['split_point']
        node['split_SSE'] = best_split['SSE']
        node['depth'] = depth
        node['left'] = {}
        node['right'] = {}

        self._iterate(best_split['left_x'], best_split['left_y'],
                      node['left'], depth + 1)
        self._iterate(best_split['right_x'], best_split['right_y'],
                      node['right'], depth + 1)
        return node
