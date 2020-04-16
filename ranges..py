#
# # list = list(range(10))
# #
# # print(list)
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)
#
# string = "abcdefghijklmnopqrstuvwxyz"
#
# print(string.index("e"))
# print(range(0,5,2) == range(0,6,2))

o = range(0, 100, 4)
print(o)

for num in o:
    print(num)

p = o[::5]
print(p)
for i in p:
    print(i)