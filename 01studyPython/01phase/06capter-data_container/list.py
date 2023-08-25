'''
  same as  javascript array
'''


array_function = list(range(0,9,3))

#* list API
print(array_function)
print(array_function.insert(1,"sadfasdf"))
print(array_function.append("6666"))
print(array_function.append(list(range(6))))
print(array_function.extend(list(range(6))))
print(array_function.pop(1))

print(array_function)

print(array_function.count(3))
print(len(array_function))

# print(array_function.clear())  clear list

def my_len(a):
   
    return a.__len__()

print(my_len(array_function))


#* loop list element

def my_loop_list(a):
    index=0
    length = len(a)

    while index < length:
        print(a[index])
        index += 1 

my_loop_list(array_function)

def my_for_list(a):
    for i in a:
        print(i)
my_for_list(array_function)