import numpy as np


class DecisionTree:

    def __init__(self, max_depth=3, min_samples=5):
        self.max_depth = max_depth
        self.min_samples = min_samples
        self._tree = {}

    @staticmethod
    def _find_split(set_):
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

    def _iterate(self, set_, node, depth=1):
        if depth >= self.max_depth:
            # Return value
            node['value'] = set_['y'].mean()
            return
        if len(set_) <= self.min_samples:
            node['value'] = set_['y'].mean()
            return

        # Calculate best split and get groups
        split = self._find_split(set_)
        node['split_point'] = split['split_point']
        node['split_SSE'] = split['SSE']

        node['left'] = {'depth': depth}
        self._iterate(split['left'], node['left'], depth + 1)

        node['right'] = {'depth': depth}
        self._iterate(split['right'], node['right'], depth + 1)
        return node

    def build_tree(self, set_):
        self._tree = self._iterate(set_, {})

    def predict(self, row, node=None):
        if node is None:
            node = self._tree

        if 'value' in node:
            return node['value']

        if row < node['split_point']:
            return self.predict(row, node['left'])
        else:
            return self.predict(row, node['right'])
