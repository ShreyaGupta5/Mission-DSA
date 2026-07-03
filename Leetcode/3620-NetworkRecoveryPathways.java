import java.util.*;

class Solution {

    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        int n = online.length;

        List<int[]>[] graph = new ArrayList[n];
        int[] indegree = new int[n];

        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        int maxCost = 0;

        for (int[] e : edges) {
            graph[e[0]].add(new int[]{e[1], e[2]});
            indegree[e[1]]++;
            maxCost = Math.max(maxCost, e[2]);
        }

        int low = 0;
        int high = maxCost;
        int ans = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (check(graph, indegree, online, k, mid, n)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }

    private boolean check(List<int[]>[] graph, int[] indegreeOrig,
                          boolean[] online, long k, int limit, int n) {

        int[] indegree = indegreeOrig.clone();

        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.offer(i);
            }
        }

        long INF = Long.MAX_VALUE / 4;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[0] = 0;

        while (!q.isEmpty()) {
            int u = q.poll();

            for (int[] edge : graph[u]) {
                int v = edge[0];
                int w = edge[1];

                if (--indegree[v] == 0) {
                    q.offer(v);
                }

                if (w < limit) {
                    continue;
                }

                if (v != n - 1 && !online[v]) {
                    continue;
                }

                if (dist[u] != INF && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
            }
        }

        return dist[n - 1] <= k;
    }
}
