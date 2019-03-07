"""
Simple graph implementation
"""


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return (len(self.stack))


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")
    #BREADTH-FIRST TRAVERSAL
    def bft(self, starting_vertex_id):   
        q = Queue()
        visited = []
        q.enqueue(starting_vertex_id)

        while q.size() > 0:
            
            v = q.dequeue()
        
            if v not in visited:
               
                visited.append(v)
                
                for neighbor in self.vertices[v]:
                    print('bft neighbor', neighbor)
                    q.enqueue(neighbor)
                    
    #BREADTH-FIRST SEARCH
    def bfs(self, starting_vertex_id, endpoint):
        print(f"start: {starting_vertex_id} end: {endpoint}")
        q = Queue()
        visited = []
        q.enqueue(starting_vertex_id)

        print('bfs queue outer:', q.queue)

        while q.size() > 0:
            print('bfs before queue:', q.queue)
            v = q.dequeue()
            print('bfs after queue:', q.queue)
            if v == endpoint:
                visited.append(v)
                break
            if v not in visited:
                print('bfs not visited', v)
                visited.append(v)
                print('bfs visited arr:', visited)
                for neighbor in self.vertices[v]:
                    # makes sure the shortest possible route is found
                    if endpoint in self.vertices[neighbor]:
                        visited.append(neighbor)
                        visited.append(endpoint)
                        break
                    else:
                        q.enqueue(neighbor)

        print("BFS", visited)
        return visited
    #DEPTH-FIRST TRAVERSAL RECURSIVE FUNCTION
    def dftr(self, start, stack, visited):
        print(
            f"FIRST: node:{start},neighbors {self.vertices[start]} visited: {visited} \n Stack:{stack.stack}")

        if visited == None:
            print(f"VISITED NONE: node:{start}, visited: {visited}")
            return
        if start in visited:
            print('start in visited')
            if not stack.stack:
                print('no stack')
                return visited

            node = stack.pop()
            print(
                f"node: {node} neighbors {self.vertices[start]} \n stack: {stack.stack}")
            for neighbor in self.vertices[start]:
                if neighbor not in visited:
                    stack.push(neighbor)
                    visited = self.dftr(neighbor, stack, visited)
                    return visited
            visited = self.dftr(node, stack, visited)
            return visited

        stack.push(start)
        visited.append(start)
        for neighbor in self.vertices[start]:
            print(
                f"POST-PUSH -- node:{start}: neighbors {self.vertices[start]} nextNode: {neighbor}, visited: {visited} \n Stack:{stack.stack}")
            visited = self.dftr(neighbor, stack, visited)
            print("other", visited)
    #DEPTH-FIRST TRAVERSAL
    def dft(self, starting_vertex_id):
        print('DFT')

        s = Stack()

        visited = []

        """ self.dftr(starting_vertex_id, s, visited) """
        s.push(starting_vertex_id)

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                for neighbor in self.vertices[v]:
                    print('neighbor: ', neighbor)
                    s.push(neighbor)
        print("OUTER VISITED", visited)
        print("OUTER stack", s.stack)
        return visited
    #DEPTH-FIRST SEARCH RECURSIVE FUNCTION
    def dfsr(self, start, stack, visited, endpoint):

        if start == endpoint:
            print('ENFOUND')
            visited.append(endpoint)
            return visited
        print(
            f"FIRST: node:{start},neighbors {self.vertices[start]} visited: {visited} \n Stack:{stack.stack}")

        if visited == None:
            print(f"VISITED NONE: node:{start}, visited: {visited}")
            return
        if start in visited:
            print('start in visited')
            if not stack.stack:
                print('no stack')
                return visited

            node = stack.pop()
            print(
                f"node: {node} neighbors {self.vertices[start]} \n stack: {stack.stack}")
            for neighbor in self.vertices[start]:
                if neighbor not in visited:
                    stack.push(neighbor)
                    visited = self.dfsr(neighbor, stack, visited, endpoint)
                    return visited
            visited = self.dfsr(node, stack, visited, endpoint)
            return visited

        stack.push(start)
        visited.append(start)
        for neighbor in self.vertices[start]:
            print(
                f"POST-PUSH -- node:{start}: neighbors {self.vertices[start]} nextNode: {neighbor}, visited: {visited} \n Stack:{stack.stack}")
            visited = self.dfsr(neighbor, stack, visited, endpoint)
            print("other", visited)
    #DEPTH-FIRST SEARCH
    def dfs(self, start, endpoint):
        s = Stack()

        visited = []

        self.dfsr(start, s, visited, endpoint)
        print("DFS TOTAL RETURN", visited)
        return visited
