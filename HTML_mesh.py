# Leitura do stl

from stl import mesh
import plotly.graph_objects as go # plotly
import numpy as np # numpy
import os

files = os.listdir()
stl = []
for f in files:
    if f[-4:] == '.stl':
        stl.append(f)

file = stl[0]
your_mesh = mesh.Mesh.from_file(file)

def stl2mesh3d(stl_mesh):
    p, q, r = stl_mesh.vectors.shape #(p, 3, 3)
    vertices, ixr = np.unique(stl_mesh.vectors.reshape(p*q, r), return_inverse=True, axis=0)
    I = np.take(ixr, [3*k for k in range(p)])
    J = np.take(ixr, [3*k+1 for k in range(p)])
    K = np.take(ixr, [3*k+2 for k in range(p)])
    return vertices, I, J, K

vertices, I, J, K = stl2mesh3d(your_mesh)
x, y, z = vertices.T

fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K)])
fig.update_layout(width=1500, height=800)
fig.write_html("mesh.html")
