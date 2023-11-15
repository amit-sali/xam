from collections import deque

def bfs(s, n, a):
    q = deque()
    vis = [0] * 20
    q.append(s)
    vis[s] = 1
    while q:
        p = q.popleft()
        print(p, end=" ")
        for i in range(n):
            if a[p][i] == 1 and not vis[i]:
                q.append(i)
                vis[i] = 1

def dfs(v, n, a):
    vis = [0] * 20
    vis[v] = 1
    print(v, end="-->")
    for i in range(n):
        if a[v][i] == 1 and not vis[i]:
            dfs(i, n, a)

n = int(input("Enter number of vertices: "))
a = [[0] * 20 for _ in range(20)]

for i in range(n):
    for j in range(n):
        a[i][j] = int(input(f"Enter 1 if {i} has an edge with {j}: "))

print("THE ADJACENCY MATRIX IS")
for i in range(n):
    for j in range(n):
        print(a[i][j], end="")
    print("")

s = int(input("Enter the source vertex: "))

print("The bfs is: ", end="")
bfs(s, n, a)

print("\n\nThe dfs is: ", end="")
dfs(s, n, a)
