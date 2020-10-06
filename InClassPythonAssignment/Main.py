
from Functions import PrintListOfNumbers, AddorSubTwoNumbers, PrintMyName

Numbers = [1, 2, 3, 4, 5, 6, 7, 8]

PrintListOfNumbers(Numbers)

Flag = raw_input("Please type something if you would like to add a flag, if not, just hit enter: ")

if(Flag == ''):
	AddorSubTwoNumbers(Number1 = 4, Number2 = 3)
else:
	AddorSubTwoNumbers(Flag = Flag, Number1 = 5, Number2 = 3)

PrintMyName()
	
