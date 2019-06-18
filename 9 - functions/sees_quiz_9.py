def sum_two_numbers(a,b):
    return a + b
# think about what x equals, then y
x = sum_two_numbers(2,2)
# x = 4
y = sum_two_numbers(sum_two_numbers(x,4),-4)
# y = sum_two_numbers(sum_two_numbers(4,4),-4)
# y = sum_two_numbers(8,-4)
# y = 4
print(y)
print(y*x+x)
