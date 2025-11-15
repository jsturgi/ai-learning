
from matrix3D import Matrix3D
from Vector3D import Vector3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation


def lerp_matrix(start: Matrix3D, end: Matrix3D, t: float):
    """
    Linearly interpolate between two matrices.

    Args:
        start: Matrix3D
        end: Matrix3D
        t: float
    
    Return:
        interpol: Matrix3D
    """
    if (start.rows != end.rows or start.cols != end.cols): raise ValueError("Dimensions don't match")
    if (t < 0 or t > 1): raise ValueError("T must be a value between 0 and 1")

    interpol = [[(start.data[i][j] + (end.data[i][j]-start.data[i][j])*t) 
                 for j in range(start.cols)] for i in range(start.rows)]
    
    return Matrix3D(interpol)



# Create 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#Define Basis Vectors
i_hat = Vector3D([1,0,0])
j_hat = Vector3D([0,1,0])
k_hat = Vector3D([0,0,1])
t_mat = Matrix3D.rotation(45, "z")

i_transformed = t_mat.multiply_vector(i_hat)
j_transformed = t_mat.multiply_vector(j_hat)
k_transformed = t_mat.multiply_vector(k_hat)
scale = 3

quiver_i = ax.quiver(0,0,0,i_transformed.components[0]*scale,i_transformed.components[1]*scale,i_transformed.components[2]*scale,
          color='orange', arrow_length_ratio=0.1, linewidth=3, label='i-hat')
quiver_j = ax.quiver(0,0,0,j_transformed.components[0]*scale, j_transformed.components[1]*scale, j_transformed.components[2]*scale,
          color='yellow', arrow_length_ratio=0.1, linewidth=3, label='j-hat')
quiver_k = ax.quiver(0,0,0,k_transformed.components[0]*scale, k_transformed.components[1]*scale, k_transformed.components[2]*scale,
          color='cyan', arrow_length_ratio=0.1, linewidth=3, label='k-hat')
quivers = {'i' : quiver_i, 'j' : quiver_j, 'k' : quiver_k}

x_points = np.linspace(-2,2,9)
x_vectors = [Vector3D([x,0,0]) for x in x_points]
transformed_x = [t_mat.multiply_vector(x) for x in x_vectors]
x_coords = [vector.components[0] for vector in transformed_x]
y_coords = [vector.components[1] for vector in transformed_x]
z_coords = [vector.components[2] for vector in transformed_x]

 # Y-axis line
y_points = np.linspace(-2, 2, 9)
y_vectors = [Vector3D([0, y, 0]) for y in y_points]
transformed_y = [t_mat.multiply_vector(y) for y in y_vectors]
"""
y_coords_t = [v.components[0] for v in transformed_y]
y_coords_t_y = [v.components[1] for v in transformed_y]
y_coords_t_z = [v.components[2] for v in transformed_y]
ax.plot(y_coords_t, y_coords_t_y, y_coords_t_z, color='magenta', label='y-axis line')
"""
# Z-axis line
z_points = np.linspace(-2, 2, 9)
z_vectors = [Vector3D([0, 0, z]) for z in z_points]
transformed_z = [t_mat.multiply_vector(z) for z in z_vectors]
"""
z_coords_t = [v.components[0] for v in transformed_z]
z_coords_t_y = [v.components[1] for v in transformed_z]
z_coords_t_z = [v.components[2] for v in transformed_z]
ax.plot(z_coords_t, z_coords_t_y, z_coords_t_z, color='lime', label='z-axis line')

ax.plot(x_coords, y_coords, z_coords, color='magenta')
"""

"""
#plot as arrows from origin
#ax.quiver - (start_x, start_y, start_z, dir_x dir_y dir_z
ax.quiver(0,0,0,1,0,0, color='r', arrow_length_ratio=0.1, label='i-hat')
ax.quiver(0,0,0,0,1,0, color='g', arrow_length_ratio=0.1, label='j-hat')
ax.quiver(0,0,0,0,0,1, color='b', arrow_length_ratio=0.1, label='k-hat')
"""
x_lines = []
y_lines = []
z_lines = []
grid_positions = np.linspace(-2,2,9)
for y in grid_positions:
    for z in grid_positions:
        x_vectors = [Vector3D([x,y,z]) for x in x_points]
        transformed_x = [t_mat.multiply_vector(v) for v in x_vectors]
        grid_x = [x.components[0] for x in transformed_x]
        grid_y = [x.components[1] for x in transformed_x]
        grid_z = [x.components[2] for x in transformed_x]

        line = ax.plot(grid_x, grid_y, grid_z,color='green', alpha=.3)
        x_lines.append(line)
        

for x in grid_positions:
    for z in grid_positions:
        y_vectors = [Vector3D([x,y,z]) for y in y_points]
        transformed_y = [t_mat.multiply_vector(v) for v in y_vectors]
        grid_x = [y.components[0] for y in transformed_y]
        grid_y = [y.components[1] for y in transformed_y]
        grid_z = [y.components[2] for y in transformed_y]

        line = ax.plot(grid_x, grid_y, grid_z, color='blue', alpha=.3)
        y_lines.append(line)
        

for x in grid_positions:
    for y in grid_positions:
        z_vectors = [Vector3D([x,y,z]) for z in z_points]
        transformed_z = [t_mat.multiply_vector(v) for v in z_vectors]
        grid_x = [z.components[0] for z in transformed_z]
        grid_y = [z.components[1] for z in transformed_z]
        grid_z = [z.components[2] for z in transformed_z]

        line = ax.plot(grid_x, grid_y, grid_z, color='red', alpha=.3)
        z_lines.append(line)

# set axis limits and labels
ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
ax.set_zlim([-2,2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

def update(frame):
    t = frame/max_frames
    quivers['i'].remove()
    quivers['j'].remove()
    quivers['k'].remove()

    start = Matrix3D.identity()
    current_matrix = lerp_matrix(start,t_mat, t)

    idx = 0
    idy = 0
    idz = 0
    #update x parallel lines
    for y in grid_positions:
        for z in grid_positions:
            x_vectors = [Vector3D([x,y,z]) for x in x_points]
            transformed = [current_matrix.multiply_vector(v) for v in x_vectors]
            xs = [v.components[0] for v in transformed]
            ys = [v.components[1] for v in transformed]
            zs = [v.components[2] for v in transformed]

            x_lines[idx][0].set_data_3d(xs,ys,zs)
            idx+=1
    #update y parallel lines
    for x in grid_positions:
        for z in grid_positions:
            y_vectors = [Vector3D([x,y,z]) for y in y_points]
            transformed = [current_matrix.multiply_vector(v) for v in y_vectors]
            xs = [v.components[0] for v in transformed]
            ys = [v.components[1] for v in transformed]
            zs = [v.components[2] for v in transformed]

            y_lines[idy][0].set_data_3d(xs,ys,zs)
            idy+=1
    #update z parallel lines
    for x in grid_positions:
        for y in grid_positions:
            z_vectors = [Vector3D([x,y,z]) for z in z_points]
            transformed = [current_matrix.multiply_vector(v) for v in z_vectors]
            xs = [v.components[0] for v in transformed]
            ys = [v.components[1] for v in transformed]
            zs = [v.components[2] for v in transformed]

            z_lines[idz][0].set_data_3d(xs,ys,zs)
            idz+=1
    #update basis vectors
    i_transformed = current_matrix.multiply_vector(i_hat)
    j_transformed = current_matrix.multiply_vector(j_hat)
    k_transformed = current_matrix.multiply_vector(k_hat)

    quivers['i'] = ax.quiver(0,0,0,i_transformed.components[0]*scale,i_transformed.components[1]*scale,i_transformed.components[2]*scale,
          color='orange', arrow_length_ratio=0.1, linewidth=3, label='i-hat')
    quivers['j'] = ax.quiver(0,0,0,j_transformed.components[0]*scale, j_transformed.components[1]*scale, j_transformed.components[2]*scale,
              color='yellow', arrow_length_ratio=0.1, linewidth=3, label='j-hat')
    quivers['k'] = ax.quiver(0,0,0,k_transformed.components[0]*scale, k_transformed.components[1]*scale, k_transformed.components[2]*scale,
              color='cyan', arrow_length_ratio=0.1, linewidth=3, label='k-hat')

    

    return []
max_frames = 60
anim = FuncAnimation(fig, update, frames=max_frames, interval=50, blit=False)
anim.save('transformation_animation.gif', writer='pillow', fps=20)
print("Animation saved!")

plt.show()
start = Matrix3D([[1,1,1],[1,1,1],[1,1,1]])
end = Matrix3D([[2,2,2],[2,2,2],[2,2,2]])
inter = lerp_matrix(start,end,.5)
print(inter)