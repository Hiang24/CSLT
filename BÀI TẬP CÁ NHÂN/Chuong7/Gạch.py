vanban = "--Người---đâu-gặp---gỡ-làm-chi---\nTrăm----năm-biết-có---duyên---gì--hay--không.\nNgổn-ngang---trăm-mối---bên---lòng----\n----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình."
# loại bỏ dấu gạch ngang
vanban = vanban.replace('-',' ').strip() #strip: loại bỏ khoảng trắng ở đầu và cuối
cau = vanban.split('\n') #Tách đoạn văn thành các câu (ở dạng list)
for i in range(len(cau)):
    tu = cau[i].split() #Tách các câu thành các từ riêng biệt trong list, đồng thời xóa bỏ các dấu cách dư thừa
    cau[i] = ' '.join(tu) #Nối các từ lại với nhau -> đã xóa các dấu cách dư thừa
ketqua = '\n'.join(cau) #Xuống dòng sau mỗi kí tự \n
print(ketqua)