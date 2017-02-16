from apyori import apriori
from collections import defaultdict

itensCompras = list()
itensComprasDict = defaultdict(list)
with open("amostra.csv", "r") as f:
    for line in f:
        content = f.readline().replace("\n", "").split("\t")
        if(content[0] != ""):
            itensComprasDict[content[0]].append(content[1])

itensCompras = [itensComprasDict[k] for k in itensComprasDict]

results = list(apriori(itensCompras, min_support = 0.6, min_confidence = 0.7))
"""
    Executes Apriori algorithm and returns a RelationRecord generator.
    Arguments:
        transactions -- A transaction iterable object
                        (eg. [['A', 'B'], ['B', 'C']]).
    Keyword arguments:
        min_support -- The minimum support of relations (float).
        min_confidence -- The minimum confidence of relations (float).
        min_lift -- The minimum lift of relations (float).
        max_length -- The maximum length of the relation (integer).
"""
