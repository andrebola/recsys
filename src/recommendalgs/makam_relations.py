import os
import json
import networkx as nx

from networkx.readwrite import json_graph
from src.similarityalgs.basic_relations import BasicRelations
from base_algorithm import AbstractRecommendAlgorithm
from recommend_mixins import Artist2ArtistMixin

class MakamRecommend(AbstractRecommendAlgorithm, Artist2ArtistMixin):
    _slug = 'makam_artists'
    def __init__(self):
        self.process()

    def process(self):
        rels = {"perfComposition": "digraph", "samePerformance": "graph"}
        out_graphs = {"perfComposition": ["country", "born"], "samePerformance": ["country", "born"]}
        out_stats = {"perfComposition": {"type": "popularity", "fields": ["country", "born"]}}

        data_location = self.get_out_location()
        if not os.path.isfile(data_location):
            rels = BasicRelations(rels, out_stats, out_graphs)
            data = json.load(open('/tmp/rels.json'))
            out = rels.process(data)
            self.graph = out['graphs']['perfComposition']
            nx.write_graphml(self.graph, data_location, encoding='utf-8')
        else:
            self.graph = nx.read_graphml(data_location)

    def recommend_a2a(self, artists_ids=None):
        ret = []
        nodes = self.graph.nodes()
        for a in artists_ids:
            for node in nodes:
                if a == node:
                    nodes = self.graph.neighbors(node)
                    ret += [i for i in nodes]
        return ret

    def get_out_location(self):
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(curr_dir, "out/makam.graphml")

    def get_graphs(self):
        d = json_graph.node_link_data(self.graph)
        return d
