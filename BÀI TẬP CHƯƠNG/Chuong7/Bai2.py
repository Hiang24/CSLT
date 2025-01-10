vanban = input()
vanban = vanban.strip()
tu = vanban.lower().split()
kitu_dau=tu[0]
ihoa = kitu_dau.title()
vanban_new = ' '.join(tu)
input_str = vanban_new.replace(kitu_dau,ihoa).replace(" , ", ", ").replace(" ; ", "; ").replace(" : ", ": ").replace(" . ", ". ")    
print(input_str)