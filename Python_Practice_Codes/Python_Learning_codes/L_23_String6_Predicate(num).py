x = "12345"
y = "2²"
z = "Ⅱ二"
print("以下为isdecimal()的结果")
print(x.isdecimal())
print(y.isdecimal())
print(z.isdecimal())
print("以下为isdigit()的结果")
print(x.isdigit())
print(y.isdigit())
print(z.isdigit())
print("以下为isnumeric()的结果")
print(x.isnumeric())
print(y.isnumeric())
print(z.isnumeric())
# 发现，isdecimal()只返回True当字符串只包含十进制数字时，而isdigit()和isnumeric()则更宽松一些
# isnumeric()甚至可以识别中文数字和罗马数字，而isdigit()则不行
print("以下为isalnum()的结果")
print("ABC123一二三".isalnum())
# isalnum()只要包含isdecimal()、isdigit()、isnumeric()、isalpha()中任意一个返回True的字符，就会返回True
print()