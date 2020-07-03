#1:creation of tuples¶
In [1]:
t=(1,2,3,4)
print(t)
(1, 2, 3, 4)

#2:creation of tuple with different data types
In [2]:
t=(1,4.5,"chai")
print(t)
(1, 4.5, 'chai')

#3:tuple to a string
In [9]:
def con(tup):
    str="".join(tup)
    return str
tup=("micky","mouse","chota","bheem")
k=con(tup)
print(k)
mickymousechotabheem

#4:slice a tuple
In [14]:
tup=("micky","mouse","chota","bheem","tom","jerry")
print(tup[2:])
print(tup[:2])
print(tup[:3])
('chota', 'bheem', 'tom', 'jerry')
('micky', 'mouse')
('micky', 'mouse', 'chota')

#5:length of tuple
In [15]:
tup=("micky","mouse","chota","bheem","tom","jerry")
print(len(tup))
6

#6:converting a tuple to a dictionary
In [19]:
tup=("micky","mouse","chota","bheem","tom","jerry")
d={}
n=(1,2,3,4,5,6)
for i in range(len(n)):
    d[tup[i]]=n[i]
for fn in d:
    print(fn,d[fn])
micky 1
mouse 2
chota 3
bheem 4
tom 5
jerry 6

#7:reversing a tuple
In [51]:
tup=("mickey","mouse","chota","bheem","tom","jerry")
for i in range(1,7):
    k=tup[-i]
    print(k)
jerry
tom
bheem
chota
mouse
mickey

#8:list of tuples to a dictionary
In [22]:
tup=(("rama","sita"),("motu","patlu"),("chota","bheem")) 
num=(4,5,6)                                   
t={}                                        
for i in range(len(num)):
    t[tup[i]]=num[i]
for fn,ln in t:
    print(fn,ln,t[fn,ln])
rama sita 4
motu patlu 5
chota bheem 6
In [ ]:
	
# 9:list to a tuple
In [21]:
l=[1,2,3,4]
f=tuple(l)
print(f)
(1, 2, 3, 4)
In [ ]:
