from algs_handler import get_recommend_algs


class System():
    def __init__(self, name, s_type, limit, weight, input_type, output_type,
            components=None, next_sys=None):
        self.name = name
        self.s_type = s_type
        self.limit = limit
        self.weight = weight
        self.next_sys = next_sys
        self.input_type = input_type
        self.output_type = output_type
        self.components = components

    def __repr__(self):
        return '<System %r>' % (self.name)

    def recommend(self, objids):
        '''Given a system and a ids of recordings or artist,
        computes de recommendation following the system specification.

        '''
        algs, errors = get_recommend_algs()
        recs = []
        for c in self.components:
            if c.s_type == 'sys':
                rec = c.recommend(objids)
            elif c.s_type == 'alg':
                rec = getattr(algs[c.name], self.get_io_type())(objids)
            if len(rec) > c.limit:
                rec = rec[:c.limit]

            recs.append((rec, c.weight))

        all_recs = []
        last_len = -1
        while len(all_recs) < self.limit and len(all_recs)>last_len:
            remains = self.limit - len(all_recs)
            last_len = len(all_recs)
            for r in recs:
                for i in r[0][:int(round(r[1] * remains))]:
                    if i not in all_recs:
                        all_recs.append(i)

        all_recs = list(all_recs)[:self.limit]
        ret = all_recs
        if self.next_sys:
            ret = self.next_sys.recommend(list(all_recs)[:self.limit])
        return ret

    def get_io_type(self):
        input_type = ""
        output_type = ""
        if self.input_type == "artist":
            input_type = "a"
        elif self.input_type == "recording":
            input_type = "r"
        elif self.input_type == "user":
            input_type = "u"
        if self.output_type == "artist":
            output_type = "a"
        elif self.output_type == "recording":
            output_type = "r"
        elif self.output_type == "user":
            output_type = "u"
        return "recommend_%s2%s" % (input_type, output_type)
