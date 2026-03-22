a,b,c = input ("enter three integer numbers :").split()
lar = a
if a < b:
   lar = b
if lar < c:
   lar = c
print("largest of the numbers:",lar)
