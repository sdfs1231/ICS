
def is_del(data):#判断是否有%
    if data==None:
        return True
    l=len(data)
    for i in range(l):
        if data[i]=='%':
            return False
        if data[i]=='=':
            return True
    if i==l-1:
        return True
