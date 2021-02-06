l = list(map(int, input().split(" "))) #list to store input elements
prod = 1
new = [] #output list

#nested for loop to store product of all elements except the indexed element.
for i in range(0,len(l)):
  prod = 1
  for x in range(0,len(l)):
    if i == x:
      continue
    else:
      prod *= l[x]
  new.append(prod)
print(new)
