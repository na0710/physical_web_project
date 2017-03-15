

list1 = ['1 42','2','1 14','3','1 28','3','1 60','1 78','2','2']
temp = []

def Enqueue(x):
    x = x[2:]
    temp.insert(len(c),x)

def Dequeue():
    if(len(temp)):
        del(temp[0])

def Print():
    if(len(temp)):
        print(temp[0])

for d in list1:
    if d == '2':
        Dequeue()
    if d == '3':
        Print()
    if d[0] == '1':
        Enqueue(d)



