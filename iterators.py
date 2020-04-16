# string = "1234567890"
#
# # for char in string:
# #     print(char)
#
# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

list = [4, 2, 0, 6, 9]
my_iter = iter(list)

for i in range(0, len(list)):
    next_item = next(my_iter)
    print(next_item)

