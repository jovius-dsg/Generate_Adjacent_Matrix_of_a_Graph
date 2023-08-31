import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

with open("grafo.txt", "r") as arquivo:
        lista_dados = [linha.strip() for linha in arquivo]
        # print(lista_dados, type(lista_dados[0]))

lista_de_tuplas = [tuple(map(int, lista_dados.split(','))) for lista_dados in lista_dados]

def generar_matriz_de_adjacencia(graph):
    num_nodes = len(graph.nodes())
    matriz_de_adjacencia = np.zeros((num_nodes, num_nodes), dtype=int)
    
    for edge in graph.edges():
        x = edge[0]
        y = edge[1]
        matriz_de_adjacencia[x][y] = 1
        matriz_de_adjacencia[y][x] = 1
    
    return matriz_de_adjacencia

G = nx.Graph()
G.add_edges_from(lista_de_tuplas)

adj_matrix = generar_matriz_de_adjacencia(G)

print("Grafo:")
print(lista_de_tuplas,"\n")
print("Matriz de Adjacência:")
print(adj_matrix)
# nx.draw(G, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_color='black')
# plt.show()