# """graph task"""
# def get_graph_from_file(file_name):
#     """ 
#     (str) -> (list)
    
#     Read graph from file and return a list of edges.
    
#     >>> get_graph_from_file("data1.txt")
#     [[1, 2], [3, 4], [1, 5]]
#     """

#     graph_list = []
#     with open(file_name, 'r', encoding='utf-8-sig') as file:
#         for line in file:
#             line = line.strip().split(",")
#             line[0] = int(line[0])
#             line[1] = int(line[1])
#             graph_list.append(line)

#     return graph_list
    
# print(get_graph_from_file("data1.txt"))
    

# def to_edge_dict(edge_list):
#     """ 
#     (list) -> (dict)

#     Convert a graph from list of edges to dictionary of vertices.
    
#     >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
#     {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
#     """

#     lst = []
#     graph_dict = {}
#     for x in edge_list:
#         for y in x:
#             if y not in lst:
#                 lst.append(y)
#                 lst.append([])

#     for i in edge_list:
#         inx = lst.index(i[0])
#         lst[inx+1].append(i[1])
#         ind = lst.index(i[1])

#         lst[ind+1].append(i[0])
#     for i in lst:
#         if isinstance(i, list):
#             i = i.sort()

#     for i in range(0, len(lst), 2):
#         key = lst[i]
#         value = lst[i+1]
#         graph_dict[key] = value

#     return graph_dict

# print(to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]]))

def is_edge_in_graph(graph, edge):
    """ 
    (dict, tuple) -> bool
    
    Return True if graph contains a given edge and False otherwise.
    
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """

    general_list = []
    for k, v in graph.items():
        general_list.append([k,v])

    for med_list in general_list:
        for i in med_list:
            if edge[0] == i:
                inx = med_list.index(i)
                if edge[1] in med_list[inx+1]:
                    return True
                else:
                    return False
            if edge[1] == i:
                inx = med_list.index(i)
                if edge[0] in med_list[inx+1]:
                    return True
                else:
                    return False
print(is_edge_in_graph({1: [2], 2: [1]}, (2, 1)))

import copy
def add_edge(graph, edge):
    """ 
    (dict, tuple) -> dict
    
    Add a new edge to the graph and return new graph. 
    
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    graph_dict = copy.deepcopy(graph)
    for key in graph:
        if key == edge[0] and edge[1] not in graph[key]:
            graph_dict.update({key: graph[key] + [edge[1]]})
        if key == edge[1] and edge[0] not in graph[key]:
            graph_dict.update({key:graph[key] + [edge[0]]})    
        if edge[0] not in graph.keys():
            graph_dict.update({edge[0]: [edge[1]]})
        if edge[1] not in graph.keys():
            graph_dict.update({edge[1]: [edge[0]]})    


    return graph_dict


print(add_edge({1: [2], 2: [1]}, (3, 1)))

def del_edge(graph, edge):
    """ 
    (dict, tuple) -> (dict)
    
    Delete an edge from the graph and return a new graph.
    
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    graph_dict = {}
    general_list = []

    for k, v in graph.items():
        general_list.append([k,v])

    num1 = edge[0]
    num2 = edge[1]

    for med_list in general_list:
        if med_list[0] == num1:
            if num2 in med_list[1]:
                inx = med_list[1].index(num2)
                del med_list[1][inx]
        if med_list[0] == num2:
            if num1 in med_list[1]:
                inx = med_list[1].index(num1)
                del med_list[1][inx]

    for medium_lst in general_list:
        for i in range(0, len(medium_lst), 2):
            key = medium_lst[i]
            value = medium_lst[i+1]
            graph_dict[key] = value

    return graph_dict

print(del_edge({1: [2], 2: [1]}, (1, 3)))

def add_node(graph, node):
    """ 
    (dict, int) -> (dict)
    
    Add a new node to the graph and return a new graph.
    
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph:
        graph_dict = {}
        general_list = []

        for k, v in graph.items():
            general_list.append([k,v])

        general_list.append([node, []])

        for medium_lst in general_list:
            for i in range(0, len(medium_lst), 2):
                key = medium_lst[i]
                value = medium_lst[i+1]
                graph_dict[key] = value

        return graph_dict

    else:
        return graph

add_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))

def del_node(graph, node):
    """ 
    (dict, int) -> (dict)
    
    Delete a node and all incident edges from the graph.
    
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """

    if node in graph:
        graph_dict = {}
        general_list = []

        for k, v in graph.items():
                general_list.append([k,v])

        i = 0
        while i != len(general_list):
            if node in general_list[i][1]:
                inx = general_list[i][1].index(node)
                del general_list[i][1][inx]
            if general_list[i][0] == node:
                del general_list[i]
            else:
                i += 1

        for medium_lst in general_list:
            for i in range(0, len(medium_lst), 2):
                key = medium_lst[i]
                value = medium_lst[i+1]
                graph_dict[key] = value

        return graph_dict

    else:
        return graph

del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 5)

def convert_to_dot(graph):
    """ 
    (dict) -> (None)
    
    Save the graph to a file in a DOT format.
    """

    with open('graph.dot', 'w') as graph_file:
        graph_d = graph_file.write("graph {" + "\n")
        for key in graph:
            for value in graph[key]:
                graph_str = "          " + str(key) + " -- " + str(value) + "\n"
                graph_d = graph_file.write(graph_str)
        graph_d = graph_file.write("      }")

convert_to_dot({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]})