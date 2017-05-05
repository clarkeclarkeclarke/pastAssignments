from collections import defaultdict
from heapq import *

def prim( nodes, edges ):
    conn = defaultdict( list )
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )

    mst = []
    used = set( nodes[ 0 ] )
    usable_edges = conn[ nodes[0] ][:]
    heapify( usable_edges )

    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )
        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )

            for e in conn[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e )
    return mst


nodes = list("ABCDEFGHI")
edges = [ ("A", "B", 4), ("B", "C", 8),
("C", "D", 7),
("D", "E", 9),
("E", "f", 10),
("F", "G", 2),
("G", "H", 1),
("H", "A", 8),
("B", "H", 11),
("C", "I", 2),
("C", "F", 4),
("I", "G", 6),
("D", "F", 14),
("H", "I", 7)]

print "prim:", prim( nodes, edges )
