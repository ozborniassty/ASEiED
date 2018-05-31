import math


graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}

graph = {'a':{'b':4,'c':2},'b':{'c':3,'d':2,'e':3},'c':{'b':1,'d':4,'e':5},'d':{},'e':{'d':1}}

graph = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

class node:

    def __init__(self,name):

        self.name = name
        self.previous = []

class Dijkstra:

    def __init__(self,graph,startingNode):

        self.graph = graph
        self.currentNode = startingNode
        self.distances = dict.fromkeys(self.graph, math.inf)
        self.distances2 = dict.fromkeys(self.graph, "")
        self.distanceToCurrentNode = 0
        self.path = {}

        self.allTabeles = []
        self.allTabeles2 = []



        # print(self.distances)
        # print(self.distances2)


    def getGraph(self):
        return self.graph

    def setNewDistances(self):

        self.distances[self.currentNode] = self.distanceToCurrentNode


        self.allTabeles.append(dict(self.distances))
        self.allTabeles2.append(dict(self.distances2))


        del self.distances[self.currentNode]
        del self.distances2[self.currentNode]

        neighbours = self.graph[self.currentNode]

        for key, value in neighbours.items():
            try:
                # print("node: ", key, "value: ", value)
                # self.distances2[key] = key



                if value < self.distances[key]:
                    self.distances[key] = value + self.distanceToCurrentNode
                    self.distances2[key] = self.currentNode

            except:
                pass






        # print(self.distances)

    def smallestNode(self):
        distances = self.distances



    def getMinimalDistance(self):
        minValue =min(self.distances, key=self.distances.get)
        # print(minValue)
        return minValue


    def setNewCurrentNode(self):

        self.currentNode = self.getMinimalDistance()
        self.distanceToCurrentNode = self.distances[self.currentNode]

        # print(self.currentNode,self.distanceToCurrentNode)

    def getClosestNode(self):
        neighbours = self.graph[self.currentNode]
        return min(neighbours, key=neighbours.get)


    def findPathFromNodeToNode(self,start,end):

        for x in range(len(self.allTabeles)-1,-1,-1):
            print(self.allTabeles[x],self.allTabeles2[x])




Dj = Dijkstra(graph,'B')
while Dj.distances != {}:
    try:
        Dj.setNewDistances()
        Dj.setNewCurrentNode()
    except:
        pass


Dj.findPathFromNodeToNode('E','A')

# print(Dj.path)

# for x in range(len(Dj.allTabeles2)):
#
#     print(Dj.allTabeles[x])
#     print(Dj.allTabeles2[x])










#
# {'B':  0,  'A': inf,  'D': inf,   'G': inf,  'C': inf,  'E': inf,  'F': inf}
# {'B': '',  'A': '',   'D': '',    'G': '',   'C': '',   'E': '',   'F': ''}

# {'A':  5,             'D':  1,    'G':  2,   'C': inf,  'E': inf,  'F': inf}
# {'A': 'B',            'D': 'B',   'G': 'B',  'C': '',   'E': '',    F': ''}

# {'A':  4,                         'G':  2,   'C': inf,  'E': 2,    'F': inf}
# {'A': 'D',                        'G': 'D',  'C': '',   'E': 'D',  'F': ''}

# {'A':  4,                                    'C':  4, '  E':  2,   'F': inf}
# {'A': 'D',                                   'C': 'G',  'E': 'D',  'F': ''}

# {'A':  4,                                    'C':  3,              'F':  4}
# {'A': 'D',                                   'C': 'E',             'F': 'E'}

# {'A':  4,                                                          'F':  4}
# {'A': 'D',                                                         'F': 'E'}

# {'F':  4}
# {'F': 'E'}

