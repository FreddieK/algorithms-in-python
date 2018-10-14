import numpy as np
import pandas as pd


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
    def _find_split_categorical(feature, x, y):
        # Thinking: this should be a preprocessing step, and then the encoded
        # categorical features should just be compared as usual
        #
        # for value in feature: => unique value...
        #
        # The question becomes how to encode the variables. Probably:
        # unique permutations of feature
        #
        # https://medium.com/data-design/visiting-categorical-features-and-encoding-in-decision-trees-53400fa65931
        #
        # for each permutation, calculate sse and choose best
        # 'split point' will have array of values in left node (?)
        # When predicting, checking for type array and then 'in' check

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
