import matplotlib.pyplot as plt 
import numpy as np
from mpl_toolkits.mplot3d import axes3d

a = np.array([[1, -2, 1], [3, 1, -2], [7, -6, -1]])
b = np.array([6, 4, 10])
c = np.linalg.solve(a,b)

print('Nilai x =', round(c[0]))
print('Nilai y =', round(c[1]))
print('Nilai z =', round(c[2]))

plt.figure('Tes 3D Plot', figsize=(15,5))
myplot1 = plt.subplot(131, projection = '3d')
myplot2 = plt.subplot(132, projection = '3d')
myplot3 = plt.subplot(133, projection = '3d')

a1 = np.array([[b[0]/a[0][0], 0, 0]])
a2 = np.array([[0, b[0]/a[0][1], 0]])
a3 = np.array([[0, 0, b[0]/a[0][2]]])

b1 = np.array([[b[1]/a[1][0], 0, 0]])
b2 = np.array([[0, b[1]/a[1][1], 0]])
b3 = np.array([[0, 0, b[1]/a[1][2]]])

c1 = np.array([[b[2]/a[2][0], 0, 0]])
c2 = np.array([[0, b[2]/a[2][1], 0]])
c3 = np.array([[0, 0, b[2]/a[2][2]]])

myplot1.plot_wireframe(a1, a2, a3, color = None, facecolor ='r', alpha = .3)
myplot1.scatter(a1, a2, a3, color = 'b')
myplot1.set_title('x - 2y + z = 6')
myplot2.plot_wireframe(b1, b2, b3, color = None, facecolor ='y', alpha = .3)
myplot2.scatter(b1, b2, b3, color = 'r')
myplot2.set_title('3x + y - 2z = 4')
myplot3.plot_wireframe(c1, c2, c3, color = None, facecolor ='b', alpha = .3)
myplot3.scatter(c1, c2, c3, color = 'b')
myplot3.set_title('7x - 6y - z = 10')


myplot1.set_xlabel('Nilai X')
myplot1.set_ylabel('Nilai Y')        
myplot1.set_zlabel('Nilai Z')    
myplot2.set_xlabel('Nilai X')
myplot2.set_ylabel('Nilai Y')        
myplot2.set_zlabel('Nilai Z')    
myplot3.set_xlabel('Nilai X')
myplot3.set_ylabel('Nilai Y')        
myplot3.set_zlabel('Nilai Z')    

plt.show()
