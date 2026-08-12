import Tools.memory as m

def is_odd_bitwise(number):
    return number & 1

def is_odd(number):
    return number % 2 != 0

def bitwise_test():
    list = []
    for i in range(10000):
        list.append(is_odd_bitwise(i))
    return list

def odd_test():
    list = []
    for i in range(10000):
        list.append(is_odd(i))
    return list

#print(bitwise_test())
#print(odd_test())
m.compare_performance(bitwise_test)
print()
m.compare_performance(odd_test)

    