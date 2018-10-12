import numpy as np


class DecisionTree:

    def __init__(self, max_depth=3, min_samples=5):
        self.max_depth = max_depth
        self.min_samples = min_samples
        self._tree = {}

    @staticmethod
    def _find_split(_set):
        best_sse = None
        best_split = None
        for index, row in set_.iterrows():
            sse = 0
            branches = [set_[set_['x'] < row['x']],
                        set_[~(set_['x'] < row['x'])]]
            for branch in branches:
                y_pred = branch['y'].mean()
                sse += np.sum((y_pred - branch['y'])**2)
            if (best_sse is None) or (sse < best_sse):
                best_sse = sse
                best_split = {
                    'SSE': sse,
                    'split_point': row['x'],
                    'left': branches[0],
                    'right': branches[1]
                }
        return best_split

    @staticmethod
    def _find_split_v2(feature, y):
        best_sse = None
        best_split = None
        for value in feature:
            sse = 0

            left_x = feature[feature < value]
            left_y = y[feature < value]
            right_x = feature[~(feature < value)]
            right_y = y[~(feature < value)]

            sse += np.sum((left_y.mean() - left_y) ** 2)
            sse += np.sum((right_y.mean() - right_y) ** 2)

            print('here', sse)

            if (best_split is None) | (sse < best_sse):
                print('here too', sse)
                best_sse = sse
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
            node['value'] = y.mean()
            return
        if len(x) <= self.min_samples:
            node['value'] = y.mean()
            return

        features = list()
        for feature in x:
            features.append(self._find_split_v2(x[feature], y))

        # best feature chosen as split, for now fake it...
        split = features[0]

        node['split_point'] = split['split_point']
        node['split_SSE'] = split['SSE']
        node['left'] = {'depth': depth}
        node['right'] = {'depth': depth}
        self._iterate(split['x_left'], split['y_left'], node['left'], depth + 1)
        self._iterate(split['x_right'], split['y_right'], node['right'], depth + 1)
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
