while True:
    password = input("Nhập mật khẩu (phải chứa ít nhất 8 ký tự, gồm chữ cái, chữ số, chữ viết hoa và viết thường): ")
    if len(password) < 8:
        print("Mật khẩu phải có ít nhất 8 ký tự!")
    elif not any(char.isupper() for char in password):
        print("Mật khẩu phải chứa ít nhất một chữ cái viết hoa!")
    elif not any(char.islower() for char in password):
        print("Mật khẩu phải chứa ít nhất một chữ cái viết thường!")
    elif not any(char.isdigit() for char in password):
        print("Mật khẩu phải chứa ít nhất một chữ số!")
    elif not any(char.isalnum() for char in password):
        print("Mật khẩu chỉ có thể chứa các ký tự chữ cái và chữ số!")
    else:
        print("Mật khẩu hợp lệ!")
        break

