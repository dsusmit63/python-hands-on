num1 = 10
num2 = "20"
text = "hello"
status = True

# int --> float,str,bool
print(float(num1))
print(str(num1))
print(bool(num1))

# numeric str ---> int,float,bool
print(int(num2))
print(float(num2))
print(bool(num2))

# str ---> int,float,bool
# print(int(text))       # Error
# print(float(text))     # Error
print(bool(text))

# bool -> int,float,str
print(int(status))
print(float(status))
print(str(status))