# words = "It's thanksgiving day. It's my birthday,too!"
# print words.find("day")
# print words.replace("day", "month")

# x = [2,54,-2,7,12,98]
# print max(x)
# print min(x)

# y = ["hello",2,54,-2,7,12,98,"world"]
# print y[0]
# print y[len(y)-1]
# new_list = [y[0], y[len(y)-1]]
# print new_list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
# print x
y = x[:len(x)/2]
# print y
z = x[len(x)/2:]
# print z
a = [y, x[len(x)/2:] ]
print a