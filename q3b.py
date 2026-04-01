def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a= a[2:]
    b= b[2:]
    ka=0
    kb=0
    p1=0
    p2=0
    for char in a[::-1]:
        
        if char=='1':
            ka+= 10**p1
        p1+=1    
    
    for char in b[::-1]:
        
        if char=='1':
            kb+= 10**p2
        p2+=1   
    
    qa=0
    num_a=0
    while ka>0:
        if ka%10==1:
           num_a+= 2 ** (qa)
        ka=ka//10
        qa+=1
    x = num_a
    
    qb=0
    num_b=0
    while kb>0:
        if kb%10==1:
            num_b+= 2**(qb)
        kb=kb//10
        qb+=1
    y= num_b
    
    z=x+y
    bin_xy=''
    while z>0:
        if z%2==1:
            bin_xy+= '1'
        else:
            bin_xy+= '0'
        z=z//2 
    
    return ('0b' + bin_xy[::-1])
            