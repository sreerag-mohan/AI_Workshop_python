# Assigning elements to different lists
list0 = []
list1 = []
list2 = []
lists = [list0, list1, list2]

def assign():

    global lists
    userInput = input("Enter elements[space as delimiter]: ")
    inputList = userInput.split(' ')
    for x in range(len(lists)):
        lists[x] += inputList
        print("List", x, "-->", lists[x])

    print("Assigning done.", end='\n')

#------------------------------------------------------------------
# Accessing elements from a tuple

def access():
    aTupple = ('a', 'b', 'c')
    for x in range(len(aTupple)):
        print("Accessing element from tuples:", x, "-->", aTupple[x],)
# -----------------------------------------------------------------
# Deleting different dictionary elements

def popFromDict():
    dictionary = {'a':1, 'b':2, 'c':3, 'd':4}
    print("current dictionary entries:", dictionary)
    userInput = input("Enter key for poping ?[space as delimiter]> ")
    inputList = userInput.split(' ')
    for x in range(len(inputList)):
        dictionary.pop(inputList[x])
    print("Dictionary after deleting: ", dictionary)
# ------------------------------------------------------------------
select = {'1' : assign,
        '2' : access,
        '3' : popFromDict,
        '4' : "Exiting"
        }

print("1. Assigning elements to different lists")
print("2. Assigning elements to different lists")
print("3. Deleting different dictionary elements")
print("4. exit")

while(1):
    option = input("choose one > ")
    if (option == '4'):
        exit()
    select[option]()
