# ip_address = input("Please enter an ip address: ")
#
# print(ip_address.count("."))

parrot_list = ["non pinin'", "no more", "a stiff", "bereft of life"]

parrot_list.append("A Norwegian blue")

for state in parrot_list:
    print("this parrot is " + state)


even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

numbers = even + odd

sorted_numbers = sorted(numbers)

if numbers == sorted_numbers:
    print("The lists are equal")
else:
    print("They are not equal")


if sorted_numbers == sorted(numbers):
    print("The lists are equal")
else:
    print("They are not equal")
