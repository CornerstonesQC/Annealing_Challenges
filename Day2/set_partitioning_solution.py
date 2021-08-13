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
Problem: Partition the set [-5, 9, 4] such that the sum of the subsets are equal
'''

# 1. Import packages
from dwave.system import DWaveSampler, EmbeddingComposite

# 2. Define the problem
Q = {('x0', 'x0'): 260, ('x1', 'x1'): 36, ('x2', 'x2'): -64,
     ('x0', 'x1'): -360, ('x1', 'x2'): 288, ('x0', 'x2'): -160}

# 3. Instantiate a solver
solver = EmbeddingComposite(DWaveSampler())

# 4. Solve the problem
sampleset = solver.sample_qubo(Q, num_reads=100)

# 5. Interpret results
print(sampleset)