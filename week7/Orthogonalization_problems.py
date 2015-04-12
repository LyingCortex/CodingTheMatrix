# version code 7f08c507c12c+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec
from vecutil import list2vec
from matutil import *
from orthogonalization import *
from math import sqrt
from triangular import triangular_solve



## 1: (Problem 1) Generators for orthogonal complement
U_vecs_1 = [list2vec([0,0,3,2])]
W_vecs_1 = [list2vec(v) for v in [[1,2,-3,-1],[1,2,0,1],[3,1,0,-1],[-1,-2,3,1]]]
# Give a list of Vecs

ortho_compl_generators_1 =[project_orthogonal(b,U_vecs_1) for b in W_vecs_1]

U_vecs_2 = [list2vec([3,0,1])]
W_vecs_2 = [list2vec(v) for v in [[1,0,0],[1,0,1]]]

# Give a list of Vecs
ortho_compl_generators_2 = [project_orthogonal(b,U_vecs_2) for b in W_vecs_2]

U_vecs_3 = [list2vec(v) for v in [[-4,3,1,-2],[-2,2,3,-1]]]
W_vecs_3 = [list2vec(v) for v in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]]

# Give a list of Vecs
ortho_compl_generators_3 =[project_orthogonal(b,U_vecs_3) for b in W_vecs_3]



## 2: (Problem 2) Basis for null space
# Your solution should be a list of Vecs

null_space_basis =[ project_orthogonal(b, [list2vec(v) for v in [[-4,-1,-3,-1],[0,4,0,-1]]]) for b in [list2vec(i) for i in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]] ]

## 3: (Problem 3) Orthonormalize(L)
def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list Lstar of len(L) orthonormal Vecs such that, for all i in range(len(L)),
            Span L[:i+1] == Span Lstar[:i+1]

    >>> from vec import Vec
    >>> D = {'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> for v in orthonormalize(L): print(v)
    ... 
    <BLANKLINE>
        a     b     c     d
    -----------------------
     0.73 0.548 0.183 0.365
    <BLANKLINE>
         a     b      c      d
    --------------------------
     0.187 0.403 -0.566 -0.695
    <BLANKLINE>
         a      b      c     d
    --------------------------
     0.528 -0.653 -0.512 0.181
    '''
    V=orthogonalize(L)
    return [1/sqrt(sum([v[i]**2 for i in range(len(v.D))]))*v for v in V] 



## 4: (Problem 4) aug_orthonormalize(L)
def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
            
    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> Qlist, Rlist = aug_orthonormalize(L)
    '''
    Ql, Rl = aug_orthogonalize(L)
    l=len(Ql)
    Qlist=[]
    Am=[]
    for v in Ql:
        A=sqrt(sum([v[i]**2 for i in range(len(v.D))])) 
        Am.append(A)
        Qlist.append(1/A*v)
    
    D=set(range(l))
    AmV=[Vec(D,{i:Am[i]}) for i in range(l)]
    AmM=coldict2mat(AmV)
    Rlist=AmM*coldict2mat(Rl)
    return Qlist, Rlist


    



## 5: (Problem 5) QR factorization of small matrices
#Compute the QR factorization

#Please represent your solution as a list of rows, such as [[1,0,0],[0,1,0],[0,0,1]]

part_1_Q =[[-0.8571,0.2556,-0.4472],[-0.2857,-0.9583,0],[-0.4286,0.1278,0.8944]] 
part_1_R =[[-7,-6.4284],[0,1.9166],[0,0]] 

part_2_Q =[[-2/3,sqrt(2)/2,-1/3/sqrt(2)],[-2/3,-sqrt(2)/2,-1/3/sqrt(2)],[-1/3,0,4/3/sqrt(2)]] 
part_2_R =[[-3,-3],[0,sqrt(2)],[0,0]] 



## 6: (Problem 6) QR Solve
from matutil import mat2coldict, coldict2mat
from python_lab import dict2list, list2dict

def QR_factor(A):
    col_labels = sorted(A.D[1], key=repr)
    Acols = dict2list(mat2coldict(A),col_labels)
    Qlist, Rlist = aug_orthonormalize(Acols)
    #Now make Mats
    Q = coldict2mat(Qlist)
    R = coldict2mat(list2dict(Rlist, col_labels))
    return Q,R


def QR_solve(A, b):
    '''
    Input:
        - A: a Mat with linearly independent columns
        - b: a Vec whose domain equals the set of row-labels of A
    Output:
        - vector x that minimizes norm(b - A*x)
    Note: This procedure uses the procedure QR_factor, which in turn uses dict2list and list2dict.
           You wrote these procedures long back in python_lab.  Make sure the completed python_lab.py
           is in your matrix directory.
    Example:
        >>> domain = ({'a','b','c'},{'A','B'})
        >>> A = Mat(domain,{('a','A'):-1, ('a','B'):2,('b','A'):5, ('b','B'):3,('c','A'):1,('c','B'):-2})
        >>> Q, R = QR_factor(A)
        >>> b = Vec(domain[0], {'a': 1, 'b': -1})
        >>> x = QR_solve(A, b)
        >>> result = A.transpose()*(b-A*x)
        >>> result.is_almost_zero()
        True
    '''
    Q, R = QR_factor(A)
    return triangular_solve(mat2rowdict(R), sorted(A.D[1],key=repr), Q.transpose()*b)




## 7: (Problem 7) Least Squares Problem
# Please give each solution as a Vec

least_squares_A1 = listlist2mat([[8, 1], [6, 2], [0, 6]])
least_squares_Q1 = listlist2mat([[.8,-0.099],[.6, 0.132],[0,0.986]])
least_squares_R1 = listlist2mat([[10,2],[0,6.08]])
least_squares_b1 = list2vec([10, 8, 6])

from solver import solve
x_hat_1 = solve(least_squares_R1, least_squares_Q1.transpose()*least_squares_b1)




least_squares_A2 = listlist2mat([[3, 1], [4, 1], [5, 1]])
least_squares_Q2 = listlist2mat([[.424, .808],[.566, .115],[.707, -.577]])
least_squares_R2 = listlist2mat([[7.07, 1.7],[0,.346]])
least_squares_b2 = list2vec([10,13,15])


x_hat_2 = solve(least_squares_R2, least_squares_Q2.transpose()*least_squares_b2)





## 8: (Problem 8) Small examples of least squares
#Find the vector minimizing (Ax-b)^2

#Please represent your solution as a list

your_answer_1 = ...
your_answer_2 = ...



## 9: (Problem 9) Linear regression example
#Find a and b for the y=ax+b line of best fit

a = ...
b = ...

