n = 50
a = 0
b = 0
sumf = 1
if n<=0:
  sumf = 0
curr = 1
for i in range(1,n):
  a = b
  b = curr
  curr = a+b
  sumf += curr
print("The sum of fibonocci numbers is:",sumf)