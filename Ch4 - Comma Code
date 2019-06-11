#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, 
#with and inserted before the last item. 

def ListToCommaString(list):
    numOfElements = len(list)
    string = ''
    for i in range(numOfElements):
        if i < numOfElements - 2:
            string = string + list[i] + ', '
        elif i == numOfElements - 2:
            string = string + list[i] + ' and '
        else:
            string = string + list[i]
    return string

list = ['apples', 'bananas', 'tofu', 'cats']
string = ListToCommaString(list)
print (string)
