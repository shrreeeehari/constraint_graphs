# constraint_graphs

The program builds an adjacency matrix to determine a constraint graph from a given set of variables and a set of binary constraints.  

The program takes an input N – the number of variables. (This would be the number of nodes in the constraint graph .The user is free to add any number of variables they want) 

From this value of N, we assume that the variables are V(1), V(2) .... V(N) 

Then we input the value for the number of constraints (NoC), the program then asks to enter those many number of constraints. The constraints should be necessarily binary involving either '<' or '>' operators only.

For example, 

N = 4 

NoC = 3 

V(1) < V(2) 

V(1) > V(3) 

V(2) < V(3) 

The program is essentially a simple parser that checks each line of constraint and sees which variables are involved in that constraint. Based on the output of the parser the program decides which nodes have edges between them. 
