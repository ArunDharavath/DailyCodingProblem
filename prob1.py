my_list = map(int, input().split())
sum = int(input())
count = 0

for i in my_list:
  for j in my_list:
    if i+j == sum:
      print("True")
      count = 0
      break
    else:
      count+=1
  break
if(count):
  print("False")
