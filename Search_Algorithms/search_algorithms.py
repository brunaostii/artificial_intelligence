
class search_algorithm(object):

    def __init__(self, adj_matrix):
        self.graph = adj_matrix


    def bfs(self, start):  
            queue = []
            visited = [0]*(len(self.graph))
            visited[start] = 1
            i = start   

            while(True):
        
                for j in range(len(self.graph)):
                    if((self.graph[i][j] != 0) and (visited[j] is 0)):
                        queue.append(j)
                        visited[j] = 1
                        print(j+1)
                        
                if(len(queue) != 0):
                    i = queue.pop(0)
                
                elif(len(queue)== 0):
                    break
            
            return i