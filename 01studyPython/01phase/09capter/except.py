
# catch execption
f

try:
 f = open("/exception.txt","r",encoding="utf-8")
except:
 print("found a exception")
 f = open("/exception.txt","w",encoding="utf-8")
 
f.close()
# catch all exception (��ʽ���������쳣)
try:
   f = open("/exception.txt","r",encoding="utf-8")     
except Exception as e:
   f = open("/exception.txt","w",encoding="utf-8")
    # (��ʽ���������쳣)

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