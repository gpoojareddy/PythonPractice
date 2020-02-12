# count function takes string and letter as arguments
def count(string, letter):
    counter = 0
    for i in string:
        if i == letter:
            counter = counter + 1
    return counter

# Converts both string and character to lower case
testString = input('Enter a string: ').lower()
character = input('Which letter count do you want to find : ').lower()
# Prints the count of specified character
print('The count of', character , 'in your string is :' , count(testString, character))
