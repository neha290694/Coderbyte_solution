
def sort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    
    return a

def f_max(x):
    f_max = a[len(x)-1]
    return f_max

def s_max(x):
    s_max = x[-2]
    return s_max

def duplicate(x):
    res = []
    for i in x:
        if i not in res:
            res.append(i)
                
    return res

a = [5,3,6,8,5,7,2,2,3]
print("Given Array - ",a)
x=sort(a)
print("Sorted Array - ",x)
y=f_max(x)
print("First maximum in Array - ",y)
z=s_max(x)
print("Second maximum in Array - ",z)

o= duplicate(x)
print("After removing duplicate - ",o)


