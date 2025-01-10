st='''--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''


def XuLyDong(xau):
    L=xau.split("-")    # Tách mỗi từ trong xâu bằng dấu -
    while "" in L:      # Xóa tất cả các ký tự rỗng trong list L
        L.remove("")
    return " ".join(L)  # Nối mỗi từ trong L thành một xâu st


def TienXuLy(st):
    L=st.split("\n")    # Tách mỗi dòng thành 1 phần tử của List L
    for dong in L:
        print(XuLyDong(dong))   #Xử lý từng dòng


TienXuLy(st)