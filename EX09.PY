s1 = 0
s2 = 0
for i in range (100):
   r = i % 2
   if r != 0:
      s1 = s1 + i
   else :
      s2 = s2 + i
print("sum of odd nos. from 1 - 100 :", s1)  
print("sum of even nos. from 1 - 100 :", s2)   