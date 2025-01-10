#So thu tu bang tieng anh co "Hậu tố vd:st,nd,rd và th"
def Nhap():
    n = int(input("Import ordinal number: "))
    return n

def ordinal(n):
    if 0< n < 13:
    #Chuyen thanh string tu int, vd. 1, 2, 3 thanh 1st, 2nd, 3rd, etc.
        if n == 1 :
            suffix = 'st'
        elif n == 2 :
            suffix = 'nd'
        elif n == 3 :
            suffix = 'rd'
        else:
            suffix = 'th'
        ord_num = str(n) + suffix
    else: ord_num = None
    return ord_num
    
def In_ket_qua(ord_num):
    print("The appropriate English ordinal number:",ord_num)
    
if __name__ == "__main__": #Giai thich cho cau "Your main program should only run when your file has not been imported into another program."
    n=Nhap()               #                   "Chương trình chính của bạn chỉ nên chạy khi tệp của bạn chưa được nhập vào chương trình khác."
    ord_num = ordinal(n)   # Tham khao link de biet cach dung: https://www.youtube.com/watch?v=Mauq4qCgsOk&t=1s
    In_ket_qua(ord_num)