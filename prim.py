class node:
	def __init__(self,name):
		self.name = name
		self.connections = {}
n,m = map(int,input().split())

graph = {}

for i in range(m):
	x,y,r = map(int,input().split())

	if x not in graph:
		graph[x] = node(x)
	if y not in graph:	
		graph[y] = node(y)

	graph[x].connections[graph[y]] = r	
	graph[y].connections[graph[x]] = r

s = int(input())
visited = {graph[s]:0}

while len(visited) != n:
	lowestCost = (None,float('inf'))
	for node in visited:
		for nextNode,weight in node.connections.items():
			if nextNode not in visited and weight < lowestCost[1]:
				lowestCost = (nextNode,weight)

	node, weight = lowestCost
	visited[node] = weight


print(sum(visited.values()))					
