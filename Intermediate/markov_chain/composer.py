import random
from graph import Graph, Vertex
import string

def get_words(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        text = ' '.join(text.split()) # this is saying turn whitespace into spaces
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split() #split spaces again
    return words

def make_graph(words):
    g = Graph()
    previous_word = None

    # for each word check if it's in graph, if not add it
    # if there was a previous word, add an edge if it's not already there

    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex


    # otherwise increment the edge by 1
    # set word to previous word, iterate
        
    # in order to get next word, set probability map
    g.generate_probability_map()
    return g

def compose(g, words, length = 50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition

def main():
    words = get_words('texts/book_of_witches.txt')
    g = make_graph(words)
    composition = compose(g, words, 100)
    return ' '.join(composition) # returns a string where all the words in composition are separated by spaces

"""step 1: get words from text
step 2: create graph using those words
step 3: get the next word for x number of words as defined by user input
step 4: show user results"""


if __name__ == '__main__':
    print(main())