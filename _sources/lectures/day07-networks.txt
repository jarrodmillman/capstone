***********************
Day 7: Network Analysis
***********************

Announcements
-------------

- No class on Monday (2/15)
- Twitter posters (2/22)
- Individual (wireless sensor network) project assigned (due 2/29)
- Team project 2 will involve machine learning in the context of
  financial data (assigned 2/29 and due 3/28)

Slide feedback
--------------

Each team will be responsible for providing detailed feedback to one of the
other teams.  At the start of class on Wednesday, each team will give
Johnny their written evaluation so that he can briefly review them before
giving the evaluations to the team being evaluated.

Johnny will be reviewing the evaluations to make sure that they are detailed
and helpful. We will be incorporating your evaluations in your team's grade for
this project.

Network Analysis
----------------

Examples
~~~~~~~~

- Social:  Friend networks in the real world as well as online 
- Infrastructure:  Networks of roads; electrical grids
- Biological: gene-gene networks, networks of nerves cells in the brain

Graphs
~~~~~~

Networks are often modeled as graphs.  A graph $G$ is an ordered pair of
(disjoint) sets $(V, E)$ where $E$ is a subset of $V \times V$.  We refer to
the elements of $V$ as *nodes* or *vertices* and the elements of $E$ as
*edges*.  A vertex $v \in V$ is *incident* to an edge $e \in E$ if $v \in e$.
Two nodes incident to the same edge are said to be joined by that edge.  We
also say that two such nodes are *adjacent*.  Edges can be directed or
undirected.  In an undirected graphs, an edge between nodes $u$ and $v$ may be
written as $uv$ or $vu$ (in such cases, we will not make any distinction
between the symbols $uv$ and $vu$).  We will only consider graphs without loops
(i.e., for all $v \in V$, we have $vv \notin V$).


The number of nodes $n = |V|$ is the *order* of $G$.  The *size* of $G$ is
the number of edges $m = |E|$.  The density of G is the proportion of actual
edges to possible edges.  For undirected graphs, the density is given by

.. math::

   \frac{2m}{n(n-1)}

and, for directed graphs, the density is

.. math::

   \frac{m}{n(n-1)}.

A *path* is a non-empty graph $P = (V, E)$ where

.. math::

   V &= (v_0, v_1, \dots, v_k) \text{      and} \\
   E &= (v_0v_1, v_1v_2, \dots, v_{k-1}v_k) \\

such that $i \neq j$ implies $v_i \neq v_j$.  A graph is *connected* if
there is a path between any two nodes.

For an undirected graph $G$, we have the following definitions:

.. math::
   eccentricity(v) &= \max_u (\text{shortest path }uv) \\
   radius(G) &= \min_v eccentricity(v) \\
   diameter(G) &= \max_v eccentricity(v) \\
   center(G) &= \{v \in G \; | \; eccentricity(v) = radius(G)\} \\
   periphery(G) &= \{v \in G \; | \; eccentricity(v) = diameter(G)\}

Social Network Analysis
~~~~~~~~~~~~~~~~~~~~~~~

To learn more about social network analysis take a look at Wikipedia::

  https://en.wikipedia.org/wiki/Social_network_analysis

Here is a simple example of using tools from social network analysis
to examine the follower network among US Sentators::

  http://jarrodmillman.com/capstone/code/fetch_senator_tweets3.py
  http://jarrodmillman.com/capstone/code/senator_network.py 

Here is some example code using R::

  http://jarrodmillman.com/capstone/code/senator_network.R
