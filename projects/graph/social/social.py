import random
from collections import defaultdict


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


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        """  """
        print(f"user: {userID} friend: {friendID}")
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """ Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships. 

        """

        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        random.seed(13)
        for userID in range(1, numUsers+1):
            self.users[userID] = User(userID)
            self.friendships[userID] = set()

        # Create friendships
        for userID in range(1, numUsers+1):
            print(userID)
            for num in range(random.randint(0, 3)):
                self.addFriendship(userID, random.randint(userID, numUsers))

    def bft(self, starting_vertex_id):
        print(f"start: {starting_vertex_id}")
        q = Queue()
        visited = {}
        q.enqueue(starting_vertex_id)
        path = [starting_vertex_id]
        indices = {}
        indices[starting_vertex_id] = 0
        index = 0
        while q.size() > 0:

            v = q.dequeue()
            print('node:', v)

            if v not in path:
                path.append(v)

            print("path:", path)
            print('indices', indices)

            if v not in visited:

                visited[v] = []

                for neighbor in self.friendships[v]:
                    if neighbor not in indices:
                        index += 1
                        indices[neighbor] = index
                    visited[v].append(neighbor)
                    q.enqueue(neighbor)

                if self.friendships[v] == None:
                    visited[v].append('No Connections')

        print("BFt", visited)
        return visited

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        visited = self.bft(userID)
        print(self.friendships)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
