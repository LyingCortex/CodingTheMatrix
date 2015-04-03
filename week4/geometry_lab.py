# version code 77ed2409f40d+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# version code 05f5a0d767f0+
# Please fill out this stencil and submit using the provided submission script.

from mat import Mat
from vec import Vec
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    it defines the default value of labels to be {'x','y','u'}.
    You should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  If you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  

    >>> identity()==Mat(({'x','y','u'},{'x','y','u'}), {('x','x'):1, ('y','y'):1, ('u','u'):1})
    True
    >>> identity({'r','g','b'})==Mat(({'r','g','b'},{'r','g','b'}), {('r','r'):1, ('g','g'):1, ('b','b'):1})
    True
    '''
    M=Mat((labels,labels),{})
    for i in labels:
        M[i,i]=1
    return M
## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.

    >>> translation(9,10)==Mat(({'x','y','u'},{'x','y','u'}), {('x','x'):1, ('y','y'):1, ('u','u'):1, ('y','u'):10, ('x','u'):9})
    True
    '''
    M=identity()
    M['x','u']=x
    M['y','u']=y
    return M
## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.

    >>> scale(3,4)*Vec({'x','y','u'}, {'x':1,'y':1,'u':1}) == Vec({'x','y','u'}, {'x':3, 'y':4, 'u':1})
    True
    >>> scale(0,0)*Vec({'x','y','u'}, {'x':1,'y':1,'u':1}) == Vec({'x','y','u'}, {'u':1})
    True
    '''
    M=identity()
    M['x','x']=a
    M['y','y']=b
    return M
## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.

    >>> def normsq(v): return v*v
    >>> normsq(rotation(math.pi) * Vec({'u', 'x', 'y'},{'x':1,'y':2,'u':1}) - Vec({'u', 'x', 'y'},{'u': 1, 'x': -1, 'y': -2})) < 1e-15
    True
    >>> normsq(rotation(math.pi/2) * Vec({'u', 'x', 'y'},{'x':3,'y':1,'u':1}) - Vec({'u', 'x', 'y'},{'u': 1, 'x': -1, 'y': 3.0})) < 1e-15
    True
    '''
    M=identity()
    M['x','x']=math.cos(angle)
    M['x','y']=-math.sin(angle)
    M['y','x']=math.sin(angle)
    M['y','y']=math.cos(angle)
    return M
## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y)*rotation(angle)*translation(-x,-y)
## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.

    >>> v = Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1})
    >>> reflect_y()*v == Vec({'x','y','u'}, {'x':-1, 'y':1, 'u':1})
    True
    >>> w = Vec({'x','y','u'}, {'u':1})
    >>> reflect_y()*w == Vec({'x','y','u'},{'u':1})
    True
    '''
    M=identity()
    M['x','x']=-M['x','x']
    return M
## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.

    >>> v = Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1})
    >>> reflect_x()*v == Vec({'x','y','u'}, {'x':1, 'y':-1, 'u':1})
    True
    >>> w = Vec({'x','y','u'}, {'u':1})
    >>> reflect_x()*w == Vec({'x','y','u'},{'u':1})
    True
    '''
    M=identity()
    M['y','y']=-M['y','y']
    return M
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.

    >>> scale_color(1,2,3)*Vec({'r','g','b'},{'r':1,'g':2,'b':3}) == Vec({'r','g','b'},{'r':1,'g':4,'b':9})
    True
    '''
    M=identity({'r','g','b'})
    M['r','r']=scale_r
    M['g','g']=scale_g
    M['b','b']=scale_b
    return M
## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    '''
    label={'r','g','b'}
    M=identity(label)
    k=0
    for i in label:
        for j in label:
            if k%3==0:
                M[i,j]=77/256
            if k%3==1:
                M[i,j]=151/256
            if k%3==2:
                M[i,j]=28/256
            k=k+1
            if k==3:
                k=0
     '''
    return Mat(({'r','g','b'},{'r','g','b'}),{('r','r'):77/256.0,('r','g'):151/256.0,('r','b'):28/256.0,('g','r'):77/256.0,('g','g'):151/256.0,('g','b'):28/256.0,('b','r'):77/256.0,('b','g'):151/256.0,('b','b'):28/256.0})
## Task 10
def reflect_about(x1, y1, x2, y2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.

    >>> def normsq(v): return v*v
    >>> normsq(reflect_about(0,1,1,1) * Vec({'x','y','u'}, {'u':1}) - Vec({'x', 'u', 'y'},{'x': 0.0, 'u': 1, 'y': 2.0})) < 10e-15
    True
    >>> normsq(reflect_about(0,0,1,1) * Vec({'x','y','u'}, {'x':1, 'u':1}) - Vec({'x', 'u', 'y'},{'u': 1, 'y': 1})) < 1e-15
    True
    '''

    theta = math.atan2(y2 - y1, x2 - x1)
    return translation(x2,y2)*rotation(theta)*reflect_x()*rotation(-theta)*translation(-x2,-y2)
