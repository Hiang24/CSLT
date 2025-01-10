def Input():
    n=int(input('n=')) #Nhập n
    L=[] #Tạo list L
    for i in range(n): #Cú pháp thêm số nguyên vào List
        x=int(input())
        L+=[x]
    x=int(input("x="))
    return x,L
def FirstAndLast(L):
    daucuoi=[L[0],L[-1]]
    print(daucuoi)
def Search(L,x):
    if x in L:
        return True
    else:
        return False
n,L=Input()
FirstAndLast(L)
print(Search(L,n))