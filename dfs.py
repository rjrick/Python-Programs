#https://www.facebook.com/permalink.php?story_fbid=352432519431550&id=100039944148017
#Subscribed by Adarsh Tiwari

from collections import defaultdict 

class Graph: 


	def __init__(self): 


		self.graph = defaultdict(list) 


	def addEdge(self, u, v): 
		self.graph[u].append(v) 


	def DFSUtil(self, v, visited): 
		visited[v] = True
		print(v, end = ' ') 
	for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFSUtil(i, visited) 

	
	def DFS(self, v): 

	
		visited = [False] * (max(self.graph)+1) 

		self.DFSUtil(v, visited) 

# Driver code 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print("Following is DFS from (starting from vertex 2)") 
g.DFS(2) 

