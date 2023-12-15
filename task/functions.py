def prod_non_zero_diag(x):
    xi=len(x)-1
    yi=len(x[0])-1
    otv=1
    i=0
    j=0
    while (i<=xi and j<=yi):
        if(x[i][j]):
             otv=otv*x[i][j]
        i+=1
        j+=1
    return otv
    pass


def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    return x==y
    pass

    pass


def max_after_zero(x):
    max=-100000
    for i in range(len(x)):
        if(x[i]==0 and i+1!=len(x)):
            if(x[i+1]>max):
                max=x[i+1]
    return max

    pass


def convert_image(img, coefs):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j]=float(img[i][j][0])*coefs[0]+float(img[i][j][1])*coefs[1]+float(img[i][j][2])*coefs[2]
    return img
    pass

    pass


def run_length_encoding(x):
    x.sort()
    a=[x[0]]
    b=[]
    prom=1
    for i in range(1,len(x)):
        if(x[i]!=x[i-1]):
            b.append(prom)
            prom=1;
            a.append(x[i])
        else:
            prom+=1;
            
    pass


def pairwise_distance(x, y):
    a1=[[0 for _ in range(len(y))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y)):
            a1[i][j]=((x[i][0]-y[i][0])**2+(x[i][1]-y[i][1])**2)**0.5;
    return a1
    pass

    pass
