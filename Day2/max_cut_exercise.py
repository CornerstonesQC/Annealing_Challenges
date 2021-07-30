# Copyright 2021 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
Problem: Partition the set from the Maximum Cut exercise slides so that the partition cuts through a maximum number
of edges
'''

# 1. Import packages
from dwave.system import DWaveSampler, EmbeddingComposite
from collections import defaultdict
import networkx as nx
import dwave.inspector as inspector

# 2. Set up the problem
# Create empty graph
G = nx.Graph()

# Add edges to the graph (also adds nodes)
G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('c', 'd'), ('c', 'f'), ('d', 'f'), ('d', 'e'), ('e', 'f')])

# ------- Set up our QUBO dictionary -------
# Initialize our Q matrix
Q = defaultdict(int)

for i, j in G.edges:
    # TODO: Update Q matrix for every edge in the graph

# 3. TODO: Instantiate a QPU solver

# 4. TODO: Solve the problem on the QPU solver
sampleset =

# TODO: Bonus - examine the results with the inspector

# 5. Interpret the results
print(sampleset)