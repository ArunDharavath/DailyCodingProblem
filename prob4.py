ls = list(map(int, input().split(" ")))
ls.sort()
x = ls[0]
for i in ls:
  if x == i:
    x+=1
    continue
  else:
    print(x, "\n")
    break
