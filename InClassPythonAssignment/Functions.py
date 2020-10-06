def PrintListOfNumbers(temp):
    sum = 0
    for x in temp:
        sum = sum + x

    print(sum)


def AddorSubTwoNumbers(Flag = None, Number1 = None, Number2 = None):
	if (Flag == None):
		print(Number1 + Number2)
	
	else:
		print(Number1 - Number2) 
	

def PrintMyName(Name = 'Chase Geis', PrintName =  4):
	for x in range(PrintName):
		print(Name)
