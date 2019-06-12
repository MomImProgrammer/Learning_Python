'''
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
with and inserted before the last item.
'''

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


def ListToCommaString2(list):
    numOfElements = len(list)
    strings = []
    for i in range(numOfElements):
        limit = numOfElements - 2
        strings.append(list[i])
        if i < limit:
            strings.append(', ')
        elif i == limit:
            strings.append(' and ')
    return ''.join(strings)

def sample(num_of_strings, str_len):
    res = []
    for _ in range(num_of_strings):
        res.append(''.join(random.choices("abcd", k=str_len)))

    return res

def test(num_of_tests):
    for _ in range(num_of_tests):
        s = sample(5, 3)
        if ListToCommaString(s) == ListToCommaString2(s):
            print("[OK]:", s)
        else:
            print("[FAIL]:", s)

###############################################################
## Runs only when called as `python 'Ch4 - Comma Code.py'`
##

def main():
    print('hello')
    # run tests
    list = ['apples', 'bananas', 'tofu', 'cats']
    string = ListToCommaString(list)
    print (string)

if __name__ == "__main__":
    main()
