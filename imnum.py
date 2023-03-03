import numpy as np
# important numpy functions
a = np.array([1,2,3,4,5])
print(a)
print("2d array")
b = np.array([[1,2,3],[3,4,5]])
print(b)
print("second 2d array")
c = np.array([[3,4,5],[1,2,3]])
print(c)
z =np.zeros((2,2))
print(z)
o = np.ones((2,2))
print(o)
a = np.random.rand(2,2)
print(a)
a = np.random.randn(2,2)
print(a)
v = np.random.randint(5,20,5)
print(v)
v1 = np.arange(10)
print(v1)
# s1 = [1,2,3,4,5,6]
np.random.shuffle(v1)
print(v1)
print(a.dtype)
a1 = np.array([[1,4,6],[2,5,7]]) 
a2 = np.array([[1,5,8],[9,5,1]])
print(np.add(a1,a2)) 
print(np.subtract(a1,a2))  
print(np.multiply(a1,a2))  
print(np.divide(a1,a2))  
print(np.mod(a1,a2)) 
print(np.power(a1,a2))
print(np.reciprocal(a1)) 
print(np.min(a1))
print(np.max(a1))
print(np.max(a1,axis=1))  
# axis =1 meaning is row and axis = 0 meaning is column 
print(np.argmax(a1)) 
# argmax give us index of maximum value
print(np.cumsum(a1))
num = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(num[1,1:])
# iterating
var = np.array([1,2,3,4,5,6,7,8])
print(var)
for i in var:
    print(i)
print("for 2d array")    
var1 = np.array([[1,2,3],[3,4,5]]) 
# for i in var1:
#     for j in i:
#         print(j)
for i in np.nditer(var1):
           print(i)
for i in np.ndenumerate(var1):
           print(i)           
print(np.ndim(var1))
print(np.size(var1))
print(np.shape(var1))
print(var.copy())
print(var.view())
var[1] = 455  
print(var.view())
print(var.copy())
a = np.array([1,4])
b = np.array([5,8])
ar = np.concatenate((a,b))
print(ar)
a = np.array([[4,5,7],[6,2,8]])
b = np.array([[4,5,7],[6,2,8]])
ar = np.concatenate((a,b),axis=1)
print(ar)
# stack
a = np.array([[4,5,7],[6,2,8]])
b = np.array([[4,5,7],[6,2,8]])
ar = np.stack((a,b),axis=0)
print(ar)
pp = np.array([3,6,1,2,8])
print(np.sort(pp))
print(np.where(pp==3))
pk = np.array([3,6,1,2,8,3,4,5,5,3,2,3,4,5,76,8])
print(np.unique(pk))
a = np.array([[4,5,7],[6,2,8]])
print(np.resize(a,(1,6)))
print(np.resize(a,(3,2)))
print(a.flatten())
vip = np.array([11,22,33,44,55])
print(np.insert(vip,(2,4),40))
ar = np.array([[4,5,7],[6,2,8]])
print(np.insert(ar,2,6,axis=0))
print(np.delete(ar,2))
print(np.transpose(ar))
a10 = np.matrix([[1,2],[3,4]])
print(np.swapaxes(a10,0,1))
arrr = np.matrix([[3,5],[6,1]])

print(np.linalg.det(arrr))
print(np.linalg.inv(arrr))
print(np.linalg.matrix_power(arrr,2))
print(np.linalg.matrix_rank(arrr))
l = []
for i in range(0,5):
    f = int(input("enter the number: "))
    l.append(f)
print(np.array(l)) 










   
           

 

     
 
 


    







