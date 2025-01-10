# it nhat 8 ky tu
# it nhat 1 chu in hoa
# it nhat 1 chu thuong
# it nhat 1 so

def Nhap():
    pw = input()
    return pw

def check_pw(pw):
    if len(pw) >= 8:
        low = False
        up = False
        num = False
        for i in pw:
            if "a" <= i <= "z": low = True
            elif "A" <= i <= "Z": up = True
            elif "0" <= i <= "9": num = True
        if low == up == num == True: return True
        else: return False
    else:
        return False

def In_kq(n):
    if n == True: print("This is a good password")
    else: print("This is not a good password")

if __name__ == "__main__":
    pw = Nhap()
    n = check_pw(pw)
    In_kq(n)

# toi da 40 lines