vanban = '''--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.'''
vanban_new= ' '.join(vanban.split('-')) #Tiến hành xóa dấu '-' và thay bằng khoảng trắng
cau = vanban_new.split('\n') #Tách đoạn văn thành các câu (ở dạng list)
for i in range(len(cau)):
    tu = cau[i].split() #Tách các câu thành các từ riêng biệt trong list, đồng thời xóa bỏ các dấu cách dư thừa
    cau[i] = ' '.join(tu) #Nối các từ lại với nhau -> đã xóa các dấu cách dư thừa
ketqua = '\n'.join(cau) #Xuống dòng sau mỗi kí tự \n
print(ketqua)