# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:22:06 2022

@author: yijae
"""

# 각 단계별 코드를 작성하시오

## 1) create array
#A 
# 0 0 1 1 0 0 
# 0 1 0 0 1 0 
# 1 1 1 1 1 
# 1 0 0 0 0 1 
# 1 0 0 0 0 1  

#B 
# 0 1 1 1 1 0 
# 0 1 0 0 1 0 
# 0 1 1 1 1 0 
# 0 1 0 0 1 0 
# 0 1 1 1 1 0 

#C 
# 0 1 1 1 1 0
# 0 1 0 0 0 0
# 0 1 0 0 0 0
# 0 1 0 0 0 0
# 0 1 1 1 1 0

# Creating labels
# y =[[1, 0, 0],
#    [0, 1, 0],
#    [0, 0, 1]]
a = [0, 0, 1, 1, 0, 0,
     0, 1, 0, 0, 1, 0,
     1, 1, 1, 1, 1, 1,
     1, 0, 0, 0, 0, 1,
     1, 0, 0, 0, 0, 1]

b = [0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 1, 0,
     0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 1, 0,
     0, 1, 1, 1, 1, 0]

c = [0, 1, 1, 1, 1, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 0, 0, 0, 0,
     0, 1, 1, 1, 1, 0]

y = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# 2) Data Visulal lization 
import numpy as np
import matplotlib.pyplot as plt

# visualizing the data, ploting A.
plt.imshow(np.array(a).reshape(5, 6))
plt.show()

# 3) As the data set is in the form of list we will convert it into numpy array
 
# converting data and labels into numpy array

"""
Convert the matrix of 0 and 1 into one hot vector
so that we can directly feed it to the neural network,
these vectors are then stored in a list x.
"""
#data transform 
x =[np.array(a).reshape(1, 30), np.array(b).reshape(1, 30),
								np.array(c).reshape(1, 30)]

# Labels are also converted into NumPy array
y = np.array(y)


print(x, "\n\n", y)


# 4) Defining the architecture or structure of the deep neural network. 
# This includes deciding the number of layers and the number of nodes in each layer. 
# Our neural network is going to have the following structure. 

# 1st layer: Input layer(1, 30)
# 2nd layer: Hidden layer (1, 5)
# 3rd layer: Output layer(3, 3)


# 5) Declaring and defining all the function to build deep neural network. 
# activation function
def sigmoid(x):
	return(1/(1 + np.exp(-x)))

# Creating the Feed forward neural network
# 1 Input layer(1, 30)
# 1 hidden layer (1, 5)
# 1 output layer(3, 3)
def f_forward(x, w1, w2):
	# hidden
	'''1'''# input from layer 1
	z1 = x.dot(w1)
	'''2'''# out put of layer 2 using sigmoid
	a1 = sigmoid(z1)
	'''3'''# Output layer
	z2 = a1.dot(w2)
	'''4'''# input of out layer
	a2 = sigmoid(z2)
	# output of out layer using simoid
	return(a2)

# initializing the weights randomly
def generate_wt(x, y):
	l =[]
	for i in range(x * y):
		l.append(np.random.randn())
	return(np.array(l).reshape(x, y))
	
# for loss we will be using mean square error(MSE)
def loss(out, Y):
	s =(np.square(out-Y))
	s = np.sum(s)/len(y)
	return(s)

# Back propagation of error
def back_prop(x, y, w1, w2, alpha):	
	# hidden layer
	# input from layer 1
	z1 = x.dot(w1)
	# output of layer 2
	a1 = sigmoid(z1)
	
	# Output layer
	# input of out layer
	z2 = a1.dot(w2)
	# output of out layer
	a2 = sigmoid(z2)
	# error in output layer
	d2 =(a2-y)
	d1 = np.multiply((w2.dot((d2.transpose()))).transpose(),
								(np.multiply(a1, 1-a1)))

	# Gradient for w1 and w2
	w1_adj = x.transpose().dot(d1)
	w2_adj = a1.transpose().dot(d2)
	
	# Updating parameters
	w1 = w1-(alpha*(w1_adj))
	w2 = w2-(alpha*(w2_adj))
	
	return(w1, w2)

def train(x, Y, w1, w2, alpha = 0.01, epoch = 10):
	acc =[]
	losss =[]
	for j in range(epoch):
		l =[]
		for i in range(len(x)):
			out = f_forward(x[i], w1, w2)
			l.append((loss(out, Y[i])))
			w1, w2 = back_prop(x[i], y[i], w1, w2, alpha)
		print("epochs:", j + 1, "======== acc:", (1-(sum(l)/len(x)))*100)
		acc.append((1-(sum(l)/len(x)))*100)
		losss.append(sum(l)/len(x))
	return(acc, losss, w1, w2)

def predict(x, w1, w2):
	Out = f_forward(x, w1, w2)
	maxm = 0
	k = 0
	for i in range(len(Out[0])):
		if(maxm<Out[0][i]):
			maxm = Out[0][i]
			k = i
	if(k == 0):
		print("Image is of letter A.")
	elif(k == 1):
		print("Image is of letter B.")
	else:
		print("Image is of letter C.")
	plt.imshow(x.reshape(5, 6))
	plt.show()

#6) Initializing the weights, as the neural network is having 3 layers, 
#so there will be 2 weight matrix associate with it. 
#The size of each matrix depends on the number of nodes in two connecting layers. 
w1 = generate_wt(30, 5)
w2 = generate_wt(5, 3)
print(w1, "\n\n", w2)


#7) Training Model
"""The arguments of train function are data set list x,
correct labels y, weights w1, w2, learning rate = 0.1,
no of epochs or iteration.The function will return the
matrix of accuracy and loss and also the matrix of
trained weights w1, w2"""

acc, losss, w1, w2 = train(x, y, w1, w2, 0.1, 100)

#Result plotting
import matplotlib.pyplot as plt1

# ploting accuracy
plt1.plot(acc)
plt1.ylabel('Accuracy')
plt1.xlabel("Epochs:")
plt1.show()

# plotting Loss
plt1.plot(losss)
plt1.ylabel('Loss')
plt1.xlabel("Epochs:")
plt1.show()

#9) Making prediction
"""
The predict function will take the following arguments:
1) image matrix
2) w1 trained weights
3) w2 trained weights
"""
predict(x[1], w1, w2)

