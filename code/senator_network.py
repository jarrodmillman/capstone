from __future__ import division, print_function

from operator import itemgetter

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')
plt.style.use('seaborn-talk')

input_data = pd.read_csv('followersmatrix.csv', index_col=0)
n = len(input_data)
num_of_followers = input_data.values.sum(axis=1)

# get party affiliation
df = pd.read_csv("senators.csv")
last_names = df['last_name']
party = list()
for x in df["party"]:
    if x == "R":
        party.append("red")
    elif x == "D":
        party.append("blue")
    else:
        party.append("purple")


G = nx.DiGraph(input_data.values)

# check that McCain has 69 followers
last_names[83]
mccain = 83
G.in_degree(mccain)
G.out_degree(mccain)

# fix it and double-check
G = nx.DiGraph(input_data.values.T)
G.in_degree(mccain)
G.out_degree(mccain)

# look at various summaries
G.nodes()
G.edges()
G.size()
G.order()
G.number_of_edges()
G.number_of_nodes()
G.number_of_selfloops()
nx.number_strongly_connected_components(G)
nx.number_weakly_connected_components(G)

# some require look at the undirected graph
U = G.to_undirected()
U.size() / G.size()
nx.radius(U)
nx.diameter(U)
nx.eccentricity(U)
nx.center(U)
nx.periphery(U)
nx.density(U)
nx.density(G)

# closer look at the degree information
G.degree()

last_names[10]
cruz = 10
last_names[40]
rubio = 40
last_names[74]
sanders = 74

G[cruz]
len(G[cruz])
G.degree()[cruz]
G.in_degree()[cruz]
G.out_degree()[cruz]

max(G.degree().values())

# average degree = 2 * #(edges) / #(nodes)
2 * G.size() / G.order()

G.adjacency_list()
G.adjacency_list()[mccain]
[v for u, v in G.edges() if u == mccain]

max(G.out_degree().values())

G.out_degree().values().index(99)
[v for v in G.nodes() if (4, v) not in set(G.edges())]
last_names[4]

# most followed
max(G.in_degree().values())
[i for i, d in enumerate(G.in_degree().values()) if d == 69]
[last_names[i] for i, d in enumerate(G.in_degree().values()) if d == 69]

# least followed
min(G.in_degree().values())
[i for i, d in enumerate(G.in_degree().values()) if d == 5]
[last_names[i] for i, d in enumerate(G.in_degree().values()) if d == 5]
last_names[53]
franken = 53

# least following
min(G.out_degree().values())
[last_names[i] for i, d in enumerate(G.out_degree().values()) if d == 0]
[df["party"][i] for i, d in enumerate(G.out_degree().values()) if d == 0]


sorted(G.out_degree().iteritems(), key=itemgetter(1))[:4]
sorted(G.out_degree().iteritems(), key=itemgetter(1))[-4:]

G.neighbors(1)
G.neighbors(4)

# set names?

# plot graph
nx.draw_spring(G)
plt.show()

# 1. color code and weight nodes
# 2. remove arrowheads and make edges gray
node_size = num_of_followers / num_of_followers.mean() * 200
pos = nx.spring_layout(G, iterations=2000)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=party)
nx.draw_networkx_edges(G, pos, alpha=0.3, edge_color="grey", arrows=False)
plt.show()


# plot spectral graph
pos = nx.spectral_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=50, node_color=party)
nx.draw_networkx_edges(G, pos, alpha=0.3, edge_color="grey", arrows=False)
plt.show()


# Degree histogram
# probably will want plt.loglog normally

degree_sequence = sorted(nx.degree(G).values(), reverse=True)
in_degrees = sorted(G.in_degree().values(), reverse=True)
out_degrees = sorted(G.out_degree().values(), reverse=True)

plt.plot(degree_sequence, 'b-', marker='o', label="Total-degree")
plt.plot(in_degrees, 'r-', marker='o', label="In-degree")
plt.plot(out_degrees, 'g-', marker='o', label="Out-degree")
plt.title("Degree rank plot")
plt.ylabel("degree")
plt.xlabel("rank")
plt.legend(loc='lower left')

plt.axes([0.47, 0.47, 0.45, 0.45])
pos = nx.spring_layout(G, iterations=1000, k=1 / 9)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=node_size / 4, node_color=party)
nx.draw_networkx_edges(G, pos, alpha=0.3, edge_color="grey", arrows=False)

plt.show()

##

bins = np.arange(0, 100, 5)
plt.hist(in_degrees, bins=bins, alpha=0.3, label='In-degree')
plt.hist(out_degrees, bins=bins, alpha=0.3, label='Out-degree')
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.legend(loc='upper right')
plt.title('Degree distribution')
plt.show()

# small plot
min_out = 40
max_out = 60
# keep = [1 if (v >= min_out and v <= max_out) else 0 for
#         v in G.out_degree().itervalues()]
keep = [k for k, v in G.out_degree().iteritems() if
        v >= min_out and v <= max_out]
discard = [k for k, v in G.out_degree().iteritems() if
           v < min_out or v > max_out]

H = G.copy()
H.remove_nodes_from(discard)
party_subset = [party[i] for i in keep]
ns_subset = [node_size[i] for i in keep]

pos = nx.spring_layout(H, iterations=500)
plt.axis('off')
nx.draw_networkx_nodes(H, pos, node_size=ns_subset,
                       node_color=party_subset)
nx.draw_networkx_edges(H, pos, alpha=0.3, arrows=False)
plt.show()

# correlation plot
# plt.imshow(input_data.corr())
# plt.show()
# plt.imshow(input_data.corr(), interpolation="nearest")
# plt.show()
plt.imshow(input_data.corr(), interpolation="nearest", cmap='gray')
plt.show()
G.in_degree(2)
G.in_degree(80)

# label
labels = {}
labels[franken] = df['last_name'][franken]
pos = nx.spring_layout(G, iterations=500)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=party)
nx.draw_networkx_edges(G, pos, alpha=0.3, edge_color="grey", arrows=False)
nx.draw_networkx_labels(G, pos, labels, font_size=16, font_color="black")
plt.show()


# Dem graph
rep_nodes = [i for i in G.nodes() if df["party"][i] == "R"]
dem_nodes = [i for i in G.nodes() if df["party"][i] == "D"]
ind_nodes = [i for i in G.nodes() if df["party"][i] == "I"]
H = G.copy()
H.remove_nodes_from(ind_nodes)
rep_graph = H.copy()
rep_graph.remove_nodes_from(dem_nodes)
dem_graph = H.copy()
dem_graph.remove_nodes_from(rep_nodes)

pos = nx.spring_layout(rep_graph, iterations=500)
plt.axis('off')
nx.draw_networkx_nodes(rep_graph, pos, node_size=50)
nx.draw_networkx_edges(rep_graph, pos, alpha=0.3, arrows=False)
plt.show()

pos = nx.circular_layout(rep_graph)
plt.axis('off')
nx.draw_networkx_nodes(rep_graph, pos)
nx.draw_networkx_edges(rep_graph, pos, alpha=0.3,
                       edge_color="grey", arrows=False)
plt.show()


pos = nx.spring_layout(dem_graph, iterations=500)
plt.axis('off')
nx.draw_networkx_nodes(dem_graph, pos, node_size=50, node_color='blue')
nx.draw_networkx_edges(dem_graph, pos, alpha=0.3, arrows=False)
plt.show()


# Rep graph

def get_top_keys(dictionary, top):
    items = dictionary.items()
    items.sort(reverse=True, key=itemgetter(1))
    return [i for i, p in items[:top]]

bet_cen = nx.betweenness_centrality(U)
clo_cen = nx.closeness_centrality(U)
eig_cen = nx.eigenvector_centrality(U)

top_bet_cen = get_top_keys(bet_cen, 10)
top_clo_cen = get_top_keys(clo_cen, 10)
top_eig_cen = get_top_keys(eig_cen, 10)
set(top_bet_cen).intersection(top_clo_cen, top_eig_cent)
[last_names[i] for i in top_bet_cen]


def centrality_scatter(dict1, dict2, path="", ylab="", xlab="",
                       title="", line=False):

    # Create items and extract centralities
    items1 = sorted(dict1.items())
    items2 = sorted(dict2.items())
    to_plot = [(a[1], b[1], str(a[0])) for a, b in zip(items1, items2)]
    # Add each actor to the plot by ID
    for p in to_plot:
        plt.text(x=p[0], y=p[1], s=p[2], color="b")

    if line:
        # use NumPy to calculate the best fit
        slope, yint = plt.polyfit(xdata, ydata, 1)
        xline = plt.xticks()[0]
        yline = map(lambda x: slope * x + yint, xline)
        plt.plot(xline, yline, ls='--', color='b')
    # Set new x- and y-axis limits
    xmax = 1.15 * max(items1, key=itemgetter(1))[1]
    ymax = 1.15 * max(items2, key=itemgetter(1))[1]
    plt.xlim((0.0, xmax))
    plt.ylim((0.0, ymax))
    # Add labels and save
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.show()

centrality_scatter(bet_cen, clo_cen)
centrality_scatter(eig_cen, clo_cen)


# Cuts

nx.minimum_node_cut(G.to_directed(), 1, 50)

# Community
# http://perso.crans.org/aynaud/communities/
# http://www.cl.cam.ac.uk/teaching/1415/L109/l109-tutorial_2015.pdf
# http://blogger.ghostweather.com/2011/09/combing-through-infovis-twitter-network.html
# http://delivery.acm.org/10.1145/1780000/1772751/p591-kwak.pdf
