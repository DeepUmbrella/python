
# catch execption

try:
 f = open("/exception.txt","r",encoding="utf-8")
except:
 print("found a exception")
 f = open("/exception.txt","w",encoding="utf-8")
