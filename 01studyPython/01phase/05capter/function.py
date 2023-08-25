
str1 = "hello"
str2 = "world"

count=0

for i in str1:
    count += 1
print(f"this string length is : {count}")


#* define function 

def calculator_string_length(a:str):
    count=0
    print(a.__len__())
    for i in a:
        count += 1
    def callback_function(a):
        return count * a
    return callback_function

print(calculator_string_length("3333")(2))



    