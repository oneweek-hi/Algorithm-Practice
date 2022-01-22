N, M = map(int, input().split())
graph = [[] for _ in range(N)]
indegree = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    indegree[b - 1] += 1

q = []
for node in range(N):
    if indegree[node] == 0:
        q.append(node)

while q:
    cur = q.pop(0)
    print(cur + 1, end=" ")

    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)
print()

# https://computer-choco.tistory.com/476
# https://sungmin-joo.tistory.com/83