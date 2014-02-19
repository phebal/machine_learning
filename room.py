#!/usr/bin/python3
"""
Machine Learning example
http://mnemstudio.org/path-finding-q-learning-tutorial.htm
"""
import networkx as nx
import random
import operator

class ExploreGraph:
    def __init__(self, DG=None, goal=5, reward=100, gamma=.8):
        self.DG = DG
        if not DG:
            self.DG = DG=nx.DiGraph()
            self._make_default_graph()
        self.goal = goal
        self.reward = reward
        self.gamma = gamma
        self._add_rewards()

    def shortest_path(self, state, nodes=[]):
        nodes.append(state)
        if state == self.goal:
            return nodes
        #import pdb; pdb.set_trace()
        max_state = max(
            [(x, y['weight']) for (x, y) in self.DG[state].items()],
            key=operator.itemgetter(1))[0]
        return self.shortest_path(max_state, nodes=nodes)

    def run(self, times=1):
        for x in range(times):
            self._explore_node(random.choice(self.DG.nodes()))

    def _explore_node(self, state):
        if state == self.goal:
            return

        # Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]
        next_state = random.choice(self.DG.neighbors(state))
        max_next_state_weight = max(
                [x['weight'] for x in self.DG[next_state].values()])
        self.DG[state][next_state]['weight'] = int(
            self.DG[state][next_state]['reward'] + self.gamma *
            max_next_state_weight)

        self._explore_node(state=next_state)

    def _add_rewards(self):
        for node in self.DG[self.goal]:
            self.DG[node][self.goal]["reward"] = self.reward

    def _make_default_graph(self):
        weight_reward = {"weight": 0, "reward": 0}
        self.DG.add_edges_from([
            (0, 4, weight_reward,),
            (4, 0, weight_reward,),
            (1, 3, weight_reward,),
            (3, 1, weight_reward,),
            (1, 5, weight_reward,),
            (5, 1, weight_reward,),
            (2, 3, weight_reward,),
            (3, 2, weight_reward,),
            (3, 4, weight_reward,),
            (4, 3, weight_reward,),
            (4, 5, weight_reward,),
            (5, 4, weight_reward,),
            (5, 5, weight_reward,)
        ])

if __name__ == "__main__":
    EG = ExploreGraph()
    EG.run(times=1000)
    for x, y in EG.DG.adjacency_iter(): print("Node: {}: {}".format(x, y))
    nodes = EG.shortest_path(random.choice(EG.DG.nodes()), nodes=[])
    print("Shortest paht: {}".format(nodes))
