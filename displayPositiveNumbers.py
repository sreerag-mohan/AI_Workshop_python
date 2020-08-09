'''
A python program to print all +ve numbers in a range
'''

# input section


inputs = input("Enter a list elements like this 1,2,3\n input: ") # get the input

print("\n")
inputList = inputs.split(',') #  set the input as list datastructures as python




# process section

outputList = [] # set outputList as empty

# code for creating a outputList
for input in inputList:
    if ( int(input) >= 0): # finding the +ve numbers and add it to outputList list datastructures
        outputList.append(input)




# ouput section

# formatted ouput
print("input :" + str(inputList))
print("output :" + str(outputList))
