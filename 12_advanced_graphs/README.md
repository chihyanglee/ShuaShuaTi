# 12 - Advanced Graphs

Weighted graphs, shortest paths, and minimum spanning trees.

## Core Patterns

1. **Dijkstra's**: Shortest path in weighted graph (no negative edges)
2. **Bellman-Ford**: Shortest path with negative edges / limited stops
3. **Prim's / Kruskal's**: Minimum spanning tree
4. **Topological sort + DP**: Shortest/longest path in DAG

## NeetCode 150 Problems

| # | Problem | Difficulty | Status | Key Pattern |
|---|---------|-----------|--------|-------------|
| 1 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | ⬜ | Prim's MST |
| 2 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | ⬜ | Dijkstra's |
| 3 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | ⬜ | Bellman-Ford / BFS |
| 4 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard | ⬜ | Eulerian path (Hierholzer's) |
| 5 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | ⬜ | Dijkstra on grid |
| 6 | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Hard | ⬜ | Topological sort |

## Common Mistakes
- Dijkstra's: using with negative edges (use Bellman-Ford instead)
- Forgetting to skip already-finalized nodes in Dijkstra's
- Prim's: not using a visited set, processing same node twice
