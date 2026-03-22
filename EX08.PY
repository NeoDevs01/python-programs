num = int (input("enter an integer number:"))
sum = 0
while num != 0:
    rem = int(num) % 10
    sum = int(sum) + rem
    num = int(num) / 10
print ("sum of digits of given integer no. :", sum)
    