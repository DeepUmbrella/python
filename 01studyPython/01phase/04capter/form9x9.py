
'''
  9x9 multiplication table
'''

start = 1
end = 20
result = ""

for i in range(start, end + 1):
  single = ""

  for j in range(start, i + 1):

    single += f"{j} x {i} = {i * j} "
  
  print(single)