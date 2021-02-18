# Your task is to convert strings to how they would be written by Jaden Smith. 
# The strings are actual quotes from Jaden Smith, but they are not capitalized
# in the same way he originally typed them.

# Example:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"


def to_jaden_case(string):
    list = []

    for word in string.split():
       list.append(word.capitalize()) 

    return " ".join(list)

if __name__ == '__main__':
    print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


# another approaches:

# approach 1: 
# def to_jaden_case(string):        
#     return " ".join(word.capitalize() for word in string.split())

# approach 2: 
# import string

# def to_jaden_case(NonJadenStrings):
#     return string.capwords(NonJadenStrings)
