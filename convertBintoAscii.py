import binascii
x = input("input number of inputs\n")
asciiList=[]
for i in range(0, int(x)):
	binNum=input("input binary number\n")
	decimal=int(binNum,2)
	asciiList.append(binascii.unhexlify('%x' % decimal))
print("Solution: ")
for i in asciiList:
	print(i)
