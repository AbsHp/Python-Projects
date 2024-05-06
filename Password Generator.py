import random

pass_len = int(input("Enter the length of the password: "))

pass_data = "`1234567890-=~!@#$%^&*()_+qwertyuiop[]asdfghjkl;'|:zxcvbnm,./<>?{}"

password = "".join(random.sample(pass_data, pass_len))

print(password)
