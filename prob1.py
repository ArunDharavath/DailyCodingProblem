"""
Reading elements into the list.
"""

my_list = map(int, input().split())
sum = int(input())
count = 0

#NESTED FOR LOOP to determine if any two nums in the list give the sum.
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
