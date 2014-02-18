#!/usr/bin/python3
"""
Machine Learning example
http://mnemstudio.org/path-finding-q-learning-tutorial.html
"""
import networkx as nx

class ExploreGraph:
    REWARD = 100
    def __init__(self, DG=None, goal=5):
        self.DG = DG
        if not DG:
            self.DG = DG=nx.DiGraph()
        self.goal = goal
        self._make_graph()
        self._add_rewards()

    def _add_rewards(self):
        for node in self.DG[self.goal]:
            self.DG[node][self.goal]["reward"] = 100

    def _make_graph(self):
        self.DG.add_edges_from([
            (0, 4, {"weight": 0, "reward": 0}),
            (4, 0, {"weight": 0, "reward": 0}),
            (1, 3, {"weight": 0, "reward": 0}),
            (3, 1, {"weight": 0, "reward": 0}),
            (1, 5, {"weight": 0, "reward": 0}),
            (5, 1, {"weight": 0, "reward": 0}),
            (2, 3, {"weight": 0, "reward": 0}),
            (3, 2, {"weight": 0, "reward": 0}),
            (3, 4, {"weight": 0, "reward": 0}),
            (4, 3, {"weight": 0, "reward": 0}),
            (4, 5, {"weight": 0, "reward": 0}),
            (5, 4, {"weight": 0, "reward": 0}),
            (5, 5, {"weight": 0, "reward": 0}),
        ])

if __name__ == "__main__":
    EG = ExploreGraph()
    import pdb; pdb.set_trace()
    print(EG.DG.nodes())
    print(EG.DG.edges())
    print(len(EG.DG.edges()))
