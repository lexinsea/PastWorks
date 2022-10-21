import matplotlib.pyplot as plt

import numpy as np
 
import math

p=[1,3,5,7]
p3=[4,6,8,10] 
lamb=[5.22e-07, 6.02e-7, 7.01e-7, 8.03e-7]
c = 3e8
m = 9.109e-31
h=6.626e-34
result=[]
for i in range(0, len(lamb)):
    result.append(math.sqrt(lamb[i] * (p[i]+4))/math.sqrt(8*c*m/h))
print(result)
plt.scatter(p3, result, c ="blue")
  
# naming the x axis
plt.xlabel('p+3')
# naming the y axis
plt.ylabel(r'$\sqrt{λ(p+4)}/\sqrt{\frac{8cm_e}{h}}}$') # doing some latex magic
  
# giving a title to my graph
z = np.polyfit(p3, result, 1)
p = np.poly1d(z)

#add trendline to plot
plt.plot(p3, p(p3),"r--")
# function to show the plot
plt.title("y={:0.3e}x+{:0.3e}".format(z[0],z[1])) 
#plt.title("y=%.10fx+%.10f"%(z[0],z[1])) 
#print({z[0]:.3e})
print('{:0.3e}'.format(z[0]))
plt.show()
