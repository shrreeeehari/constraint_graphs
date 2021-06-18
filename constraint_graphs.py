import numpy as np
import networkx as nx

Vnum = int(input("Enter the number of variables(N): "))
ConsNum = int(input("Enter the number of constraints: "))
constraints=[]
constraintDigits=[]
adj_matrix = []
Range = []

for i in range(0,Vnum):
    Range.append(i)
    
for i in range(Vnum):
    x=[]
    for j in range(Vnum):
        x.append(0)
    adj_matrix.append(x)
    
for i in range(1,ConsNum+1):
    cons = input("Enter constraint "+str(i)+" ( Format: v(i)<v(j) OR v(i)>v(j) ) : " +"\n")
    constraints.append(cons)
    
    split = np.array_split(constraints, len(constraints))
    for array in split:
        for i in array:
            for j in i:
                if j.isdigit() == True:
                    constraintDigits.append(int(j))
    #print(constraintDigits)           
    m = constraintDigits[0]
    n = constraintDigits[1]
    adj_matrix[m-1][n-1] = 1
    adj_matrix[n-1][m-1] = 1
    constraints.clear()
    constraintDigits.clear()

print("\nFinal Adjacency Mtrix : \n")
for i in range(Vnum):
    for j in range(Vnum):
        print(adj_matrix[i][j], end=" ")
    print()

b= np.matrix(adj_matrix)
k=nx.from_numpy_matrix(b)
nx.draw(k)