#In lên màn hình bảng cửu chương 9x9
i=1
while i<=9:
    j=1
    while j<=9:
        print(str(i*j).rjust(3),end=" ")
        j=j+1
    print()
    i=i+1