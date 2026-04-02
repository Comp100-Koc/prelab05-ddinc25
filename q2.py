def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    removed=''
    i=0
    while i < (len(s)-1):
        if (s[i-1]!=s[i]) and (s[i]!= s[i+1]):
            if s[i] not in removed:
                removed+= s[i]
            i+=1
        else:
            s= s[:i] + s[i+2:] 
            i=0
        
    return s