import numpy as np


class DecisionTree:

    def __init__(self, max_depth=3, min_samples=5):
        self.max_depth = max_depth
        self.min_samples = min_samples
        self._tree = {}

    @staticmethod
    def _find_split(feature, x, y):
        best_sse = None
        best_split = None
        for value in feature:
            left_y = y[feature < value]
            right_y = y[~(feature < value)]

            sse = np.sum((left_y.mean() - left_y)**2) + \
                   np.sum((right_y.mean() - right_y)**2)

            if (best_sse is None) or (sse[0] < best_sse[0]):
                best_sse = sse
                left_x = x[feature < value]
                right_x = x[~(feature < value)]
                best_split = {
                    'SSE': sse,
                    'split_point': value,
                    'left_x': left_x,
                    'left_y': left_y,
                    'right_x': right_x,
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

        features = list()
        for feature in x:
            features.append(self._find_split(x[feature], x, y))

        # best feature chosen as split, for now fake it...
        split = features[0]

        node['split_point'] = split['split_point']
        node['split_SSE'] = split['SSE']
        node['depth'] = depth

        node['left'] = {}
        node['right'] = {}
        self._iterate(split['left_x'], split['left_y'], node['left'], depth + 1)
        self._iterate(split['right_x'], split['right_y'], node['right'], depth + 1)
        return node

    def build_tree(self, x, y):
        self._tree = self._iterate(x, y, {})

    def predict(self, row, node=None):
        if node is None:
            node = self._tree

        if 'value' in node:
            return node['value']

        if row < node['split_point']:
            return self.predict(row, node['left'])
        else:
            return self.predict(row, node['right'])
