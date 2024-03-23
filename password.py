import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "!@#$%^&*()"

string = upper + lower + num + symbol
length = 10
password = "".join(random.sample(string,length))

print("Your New Password =" + password)
