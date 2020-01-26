import sys


def Dijkstra(node):
    visited[node] = True
    costs[node] = (0, node)
    stacks = {node: node}  # Keeps track of paths from root_node to des_node
    last_visited_node = node

    # While there are still unvisited values,
    # update costs and find paths for node
    while False in visited.values():
        # Current least cost node, root node for the least cost node
        least_cost_node, root_node = findLeastCost(last_visited_node, costs[last_visited_node][0])
        visited[least_cost_node] = True

        # Concatenate root node path to current least_cost_node
        stacks[least_cost_node] = stacks[root_node] + least_cost_node
        last_visited_node = least_cost_node

    return stacks


def findLeastCost(node, prev_cost):
    least_cost_node = None
    for curr_node in nodes:
        if curr_node != node and distances[node, curr_node] != 9999 and not visited[curr_node]:
            # Updates costs of the nodes
            cost = prev_cost + distances[node, curr_node]
            if cost < costs[curr_node][0]:
                costs[curr_node] = (cost, node)

            # Finds least cost of nodes
            least_cost_node = curr_node if least_cost_node is None or \
                                           cost < costs[least_cost_node][0] else least_cost_node

    return least_cost_node, costs[least_cost_node][1]

f1 = open(sys.argv[1], "r")
file1 = f1.read()
nodes_line = file1[1:12]
file1 = file1[13:]

# nodes = list of all nodes in graph
# visited = visited nodes; default = false
# costs = node costs and roots; default = inf, None
nodes = nodes_line.split(',')
visited = dict(zip(nodes, [False] * len(nodes)))
costs = dict(zip(nodes, [(float('inf'), None)] * len(nodes)))  # node costs and roots; default = inf, None
distances = {}


i = 0
k = -1

# Uses file to create initial distance dictionary
# Distance dictionary represents the graph;
# (node1, node2) = cost between node1 and node2
for val in file1:
    if val != ',' and val != '\n' and val not in nodes:
        if (nodes[i], nodes[k]) not in distances:
            distances[(nodes[i], nodes[k])] = int(val)
        else:
            distances[(nodes[i], nodes[k])] = int(str(distances[(nodes[i], nodes[k])]) + val)

    if val not in nodes:
        if val == '\n':
            k = -1
            i += 1

        elif val == ',':
            k += 1

f1.close()

# Gets an input from the user for node they want to use
while True:
    nodeChosen = raw_input("Please, provide the node's name: ")
    if nodeChosen in nodes:
        break
    else:
        print('Not a Valid Node\n')

stacks = Dijkstra(nodeChosen)

print "\nShortest path tree for node " + nodeChosen + ":"
for val in stacks.values():
    print val + " ",

print "\n\nCosts of least-cost paths for node " + nodeChosen + ":"
for node in nodes:
    print "%s: %d " % (node, costs[node][0]),
