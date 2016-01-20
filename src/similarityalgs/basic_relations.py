class BasicRelations(AbstractSimAlgorithm):
    def __init__(self, rels, out_stats, out_graph):
        self.rels = rels
        self.out_stats = out_stats
        self.out_graph = out_graph

    def process(self, data):
        self.graphs = {}
        for rec in data.keys():
            l.append(rec)
            for r in self.rels:
                if r in data[rec]: 
                    for p in  data[rec][r].keys():
                        if r not in self.graphs:
                            if self.rels[r] == 'digraph':
                                self.graphs[r] = nx.DiGraph()
                            else:
                                self.graphs[r] = nx.Graph()
                        l.append(p)
                        self.graphs[r].add_edge(rec, p, attr_dict={'weight': data[rec][r][p]})
        
        return {
                "stats": get_stats(data),
                "graphs": get_graphs(data)
               }
    def get_stats(self, data):
        stats = {}
        for r in self.rels.keys():
            if self.rels[r] == "digraph":
                if r in self.out_stats and self.out_stats[r]["type"] == "popularity":
                    if r not in stats:
                        stats[r] = {}
                    for b, count in self.graphs[r].in_degree().items():
                        for f in self.out_stats[r]["fields"]:
                            if f not in stats[r]:
                                stats[r][f] = {}
                            if b in data and f in data[b]:
                                c = data[b][f]
                                if c in stats[r][f].keys():
                                    stats[r][f][c] += count
                                else:
                                    stats[r][f][c] = count
                        if 'combined' not in stats[r]:
                            stats[r]['combined'] = {}
                        c = []
                        for f in self.out_stats[r]["fields"]:
                            if b in data and f in data[b]:
                                c.append(a[b][f])
                        if c in stats[r][f].keys():
                            stats[r][f]["-".join(c)] += count
                        else:
                            stats[r][f]["-".join(c)] = count
        return stats

    def get_graphs(self, data):
        graphs_fields = {}
        for r in self.rels.keys():
            if r not in graphs_fields:
                graphs_fields[r] = {}
                
            for edge in self.graphs[r].edges(data=True):
                i = edge[0]
                j = edge[1]

                for f in out_graphs[r]:
                    elems_i = []
                    elems_j = []
                    if f not in graphs_fields[r]:
                        if self.rels[r] == "digraph":
                            graphs_fields[r][f] = nx.DiGraph()
                        else:
                            graphs_fields[r][f] = nx.Graph()
                    if f in data[i]:
                        elems_i = data[i][f]
                    if j in data and f in data[j]:
                        elems_j = data[j][f]
                    for ci in elems_i:
                        for cj in elems_j:
                            if ci in graphs_fields[r][f].nodes():
                                if cj in graphs_fields[r][f][ci].keys():
                                    graphs_fields[r][f][ci][cj]['weight'] += edge[2]['weight']
                                else:
                                    graphs_fields[r][f].add_edge(ci, cj, attr_dict=edge[2])
                            else:
                                graphs_fields[r][f].add_edge(ci, cj, attr_dict=edge[2]) 
        return graphs_fields.update(self.graphs)
