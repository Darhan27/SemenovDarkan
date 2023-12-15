import numpy as np


def prod_non_zero_diag(x):
    return np.prod(np.diag(x,0)[np.diag(x)!=0])

    pass


def are_multisets_equal(x, y):
    np.sort(x)
    np.sort(y)
    return x==y

    pass


def max_after_zero(x):
    return np.max(x[1:][np.nonzero(x[:-1] == 0)])

    pass


def convert_image(img, coefs):
    return np.dot(img,coefs)
    pass


def run_length_encoding(x):
    dif=np.diff(x)
    h=np.array([-1])
    h=np.append(h, np.nonzero(dif))
    h+=1
    a=x[h]
    h=np.append(h,len(x))
    b=np.diff(h)
    return (a,b)
    pass


def pairwise_distance(x, y):
    a1=np.arange(1,len(x)*len(y)+1)
    a1 = np.reshape(a1,(len(x),len(y)))
    a1[np.nonzero(a1)]=((x[np.nonzero(a1)[0]][0]-y[np.nonzero(a1)[1]][0])**2+(x[np.nonzero(a1)[0]][1]-y[np.nonzero(a1)[1]][1])**2)**0.5
    return a1
    pass
