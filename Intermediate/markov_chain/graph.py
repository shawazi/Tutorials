# this is our markov chain representation. 
import random
# define the graph in terms of vertices

class Vertex:
    def __init__(self, value): # value will be the word
        self.value = value
        self.adjacent = {} # nodes that have an edge from this vertex
        self.neighbors = [] # vertices that have an edge to this vertex
        self.neighbors_weights = [] # weights of the edges to this vertex

    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        # return a map of the probabilities of the next word
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        #randomly select next word based on weights
        return random.choices(self.neighbors, weights = self.neighbors_weights)[0]




#graph

class Graph:
    def __init__(self):
        self.vertices = {} #maps string to Vertex
        
    def get_vertex_values(self):
        return set(self.vertices.keys())
    #what are the values of all the vertices? return all possible words

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        #what if the value isn't in the graph?
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_map(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()