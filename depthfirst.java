package algorithms;
import java.util.*;


class Graph {
 
	private int V;
    private Map<Integer, List<Integer>> adj;
 
    public Graph(int v) {
        this.V = v;
        this.adj = new HashMap<>();
        for (int i = 0; i < v; i++)
            adj.put(i, new LinkedList<>());
    }
 
   public void addEdge(int v, int w) {
       adj.get(v).add(w);
   }
 
   	public void visit(int v, boolean[] visited) {
       System.out.println(v + " ");
       visited[v] = true;
 
       List<Integer> neighbours = adj.get(v);
       for (Integer i : neighbours) {
           if (!visited[i])
               visit(i, visited);
       }
   }
 
   public void dfs(int v) {
       boolean[] visited = new boolean[V];
       visit(v, visited);
   }
 
    public static void main(String[] args) {
        Graph g = new Graph(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);
 
        System.out.println("Following is Depth First Traversal "+
                           "(starting from vertex 2)");
 
        g.dfs(2);
    }
}

