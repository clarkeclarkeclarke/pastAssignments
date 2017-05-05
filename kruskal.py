#
# This class implements union-find operations on disjoint sets.
# The constructor creates individual sets for the values 0..count-1.
#
# The other methods work the way you expect.
class UFset:

    def __init__(self, count):
        self.lst = []
        for i in range(0, count):
            self.lst.append(i)

    def findset(self, element):
        name = element
        while self.lst[name] != name:
            name = self.lst[name]

        return name

    def union(self, element1, element2):
        root1 = self.findset(element1)
        root2 = self.findset(element2)
        self.lst[root2] = root1


class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __repr__(self):
        return "Edge("+repr(self.v)+","+repr(self.w)+","+repr(self.weight)+")"

    def __str__(self):
        return "("+repr(self.v)+","+repr(self.w)+","+repr(self.weight)+")"


def kruskal_mst(edge_list, n):
    tree = []
    i = 1
    while n <= i:
        if findset(edge_list[i].v) != findset(edge_list[i].w):
            print edge_list[i].v+' '+edge_list[i].w
            i = i + 1
            union(edge_list[i].v,edge_list[i].w)
    return tree


print("-- Graph 1 --")
edge_list = [Edge(0, 4, 1), Edge(0, 1, 3), Edge(1, 4, 4), Edge(4, 2, 6), Edge(4, 3, 7), Edge(2, 3, 2), Edge(1, 2, 5)]
print("Edge list")
print(edge_list)
tree_edge_list = kruskal_mst(edge_list, 5)
tree_weight = 0
print("Tree edge list")
print(tree_edge_list)
for edge in tree_edge_list:
    tree_weight += edge.weight
print("Tree weight:", tree_weight) 
print()

print("-- Graph 2 --")
edge_list = [Edge(0, 1, 4), Edge(0, 7, 8), Edge(1, 2, 8), Edge(1, 7, 11), Edge(2, 3, 7), Edge(2, 5, 4), Edge(3, 4, 9), Edge(3, 5, 14), Edge(5, 4, 10), Edge(6, 5, 2), Edge(7, 6, 1), Edge(7, 8, 7), Edge(8, 2, 2), Edge(8, 6, 6)]
print("Edge list")
print(edge_list)
tree_edge_list = kruskal_mst(edge_list, 9)
tree_weight = 0
print("Tree edge list")
print(tree_edge_list)
for edge in tree_edge_list:
    tree_weight += edge.weight
print("Tree weight:", tree_weight)
