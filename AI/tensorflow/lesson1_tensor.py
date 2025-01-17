import tensorflow as tf 

# ================ initialization Tensors ===================
x = tf.constant(4, shape= (1,1), dtype= tf.float32)
x = tf.constant([[1,2,3], [4,5,6]])

x = tf.ones((3,3))
x = tf.zeros((2,3))
x = tf.eye(3)   # eyes (I) for the identity matrix 
x = tf.random.normal((3,3), mean= 0, stddev= 1)
x = tf.random.uniform((3,3), minval= 0, maxval= 1)

x = tf.cast(x, dtype= tf.float64)   # convert to different type 
print(x)


# ================ mathematical operations ===================
x = tf.constant([1, 2, 3])
y = tf.constant([9, 8, 7])
z = tf.add(x, y)     # sum x + y 
z = x + y            # sum x + y

s = tf.subtract(y, x) # subtract y - x  
s = y - x

d = tf.divide(y, x)   # y / x 
d = y / x 

m = tf.multiply(x, y)  # x * y 
m = x * y

z = tf.tensordot(x, y, axes= 1)   # dot-product

z = x ** 5   

x = tf.random.normal((2,3))
y = tf.random.normal((3,4))
z = tf.matmul(x, y)             # multiply two matrix
z = x @ y                       # multiply two matrix 


# ================ Indexing ===================
x = tf.constant([0, 1, 1, 2, 4, 1, 4, 2, 14])
print(x[:]) 
print(x[1:])
print(x[4: 6])
print(x[::-1])    # reverse tensor

y = tf.constant([
    [1, 2], 
    [3, 4],
    [5, 6]
])
print(y[0, :])
print(y[0:2, :])

# ================ Reshaping ===================
x = tf.range(9)
x = tf.reshape(x, (3, 3))
x = tf.transpose(x, perm=[1,0])
x = tf.linalg.inv(x)                # create inverse matrix of x  
print(x)

