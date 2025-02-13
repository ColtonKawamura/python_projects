import numpy as np
import matplotlib.pyplot as plt

# Material Properties (Steel)
E = 200e9  # Young's modulus (Pa); the ratio of stress (force/area) and strain (porportional deformation)
#  another way: ratio of pressure to normalized deformation (length); P = kx, 

# Node Coordinates (x, y); really simple case of two triangles in the square
nodes = np.array([
    [0, 0],  # Node 0
    [1, 0],  # Node 1
    [1, 1],  # Node 2
    [0, 1]   # Node 3
])

# Create the elements (surfaces of the triangle in this example)
elements = np.array([
    [0, 1, 2],  # Triangle 1
    [0, 2, 3]   # Triangle 2
])

# Applied Force (at Node 2 in Y direction)
forces = np.zeros((len(nodes), 2))  # initialize force array with num_rows = number of nodes and 2 dimensions for each
forces[2, 1] = -1e6  # 1 MN force downwards at Node 2

# Fixed Boundary Conditions (Fix bottom edge: Nodes 0 and 1)
# fixed_nodes = [0, 1]

# Solve using Finite Element Method (Simplified)
# (Skipping stiffness matrix assembly for brevity)

# Assume simple displacement field for quick estimation
displacements = np.zeros((len(nodes), 2)) #initialize a 2D row for each node
displacements[2, 1] = -0.001  # Approximate downward displacement at Node 2 (3rd element)

# Compute Approximate Stress (σ = E * strain)
strain = displacements[2, 1] / (nodes[2, 1] - nodes[0, 1])  # Δy / L, aka how much the element's lenght get displaced normalized by the original length.
stress = E * strain  # Hooke's Law

# Plot Stress Visualization
plt.figure(figsize=(5,5))
plt.triplot(nodes[:,0], nodes[:,1], elements, color='k')
plt.scatter(nodes[:,0], nodes[:,1], color='red', label="Nodes")
plt.quiver(nodes[:,0], nodes[:,1], displacements[:,0], displacements[:,1], angles='xy', scale=1e-2)
plt.title(f"Stress Analysis: σ = {stress/1e6:.2f} MPa")
plt.legend()
plt.grid()
plt.show()
