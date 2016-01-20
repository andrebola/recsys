import os
import networkx as nx

from similarityalgs.basic_similarity import BasicRelations

class MakamRecommend(AbstractRecommendAlgorithm, Artist2ArtistMixin):
    def process(self):
        rels = {"perfComposition": "digraph", "samePerformance": "graph"}
        out_graphs = {"perfComposition": ["country", "born"], "samePerformance": ["country", "born"]}
        out_stats = {"perfComposition": {"type": "popularity", "fields": ["country", "born"]}}
        if not os.is_file('out/makam.graphml'): 
            rels = BasicRelations(rels, out_graphs, out_stats)
            data = json.load(open('/tmp/rels.json')) 
            out = rels.process(data)
            self.graph = out['graphs']['perfComposer']
            nx.write_graphml(self.graph, 'out/makam.graphml', encoding='utf-8')
        else:
            self.graph = nx.read_graphml(self.graph, 'out/makam.graphml')

    def recommend(self, artists_ids=None):
        nodes = self.graph.nodes()
        if artist_id in nodes:
            nodes = self.graph.neighbors(nodes[artist_id])
            return [i for i in nodes]
        return []
        
