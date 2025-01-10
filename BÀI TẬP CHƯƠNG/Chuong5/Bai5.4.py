A=[]
n=int(input('n='))
for i in range(n):
    x=int(input())
    A.append(x)
    B=A[::-1] #cú pháp đảo thứ tự và lưu vào list mới
print(B)
B.sort()
print(B)
'''Dòng code B = A[::-1] có nghĩa là tạo ra một List B mới,
chứa các phần tử của List A được đảo ngược thứ tự.
Cụ thể, [::-1] được gọi là slicing syntax (cú pháp cắt) trong Python,
và nó có ý nghĩa lấy tất cả các phần tử của List,
bắt đầu từ phần tử đầu tiên đến phần tử cuối cùng,
với bước cắt (step) bằng -1.
Bước cắt bằng -1 có nghĩa là lấy các phần tử theo thứ tự đảo ngược của List ban đầu.
Vì vậy, khi gán giá trị B = A[::-1], chương trình sẽ tạo ra một List B mới,
chứa các phần tử của List A được đảo ngược thứ tự.'''