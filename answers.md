# CMPS 2200 Recitation 10## Answers

**Name:** Benjamin Horowitz


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** The work of reachable is O(m + n). You visit each node and each edge exactly once using my method, which is why the work is n (nodes) + m (edges).

- **4)** My function only calls reachable once, so this is the worst case.

- **5)** Connected really just calls reachable and then makes a comparison, so the work is the same as reachable. That is O(m + n).

- **7)** For an adjacency matrix, we would have to go through every entry in the matrix to determine connectedness. Therefore, it would be O(n^2). That is because instead of going over existing edges, we would also have to go over non-existing edges to figure it out.
