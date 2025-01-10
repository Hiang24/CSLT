def nhap():
    input_str = input()
    return input_str
def split_and_print_mail(input_str):
    check_mail = (input_str.split(","))[1]
    if "@" in check_mail:
        email_index = str(check_mail).find(":")
        email = check_mail[email_index+2:]
        if email != "":
            print(email)
input_str = nhap()
split_and_print_mail(input_str)