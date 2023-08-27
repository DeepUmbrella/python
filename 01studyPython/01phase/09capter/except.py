
# catch execption
f = None

try:
 f = open("/exception.txt","r",encoding="utf-8")
except:
 print("found a exception")
 f = open("/exception.txt","w",encoding="utf-8")
 
f.close()
# catch all exception (显示捕获异常)
try:
   f = open("/exception.txt","r",encoding="utf-8")     
except Exception as e:
   f = open("/exception.txt","w",encoding="utf-8")
    # (隐式捕获所有异常)

'''
except:
 # todo
'''
'''
# catch single exception

try:
   f = open("/exception.txt","r",encoding="utf-8")     
except FileNotFoundError as exceptError:
   f = open("/exception.txt","w",encoding="utf-8") 


# try catch else finally


try:
   f = open("/exception.txt","r",encoding="utf-8")    
except:
   f = open("/exception.txt","w",encoding="utf-8") 
else:
   print("no exception found")
finally:
   print("finally i will run this")
   '''