import numpy as np
import time 
w=np.array([1,2,3,4,5,6,7])
x=np.array([300,150,100,90,700,50,60])
b=11
f1=0
t1=time.time()
for i in range(len(x)):
    f1=f1+(x[i]*w[i])
f1=f1+b 
print(f"The time taken is: {time.time()-t1}")
print(f"The value of f is: {f1}")   
t2=time.time()
f2=np.dot(w,x)+b
print(f"The time taken is: {time.time()-t2}")
print(f"The value of f is: {f2}")