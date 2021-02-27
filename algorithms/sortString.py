import re

def order(sentence):

    X = sentence.split() #1. make a list from a string
    Y = re.findall("\d+", sentence) #2. Getting the number from string's words 
    Z = [x for _,x in sorted(zip(Y,X))] #3 using a list comprehension extract the first elements of each pair from the sorted, zipped list.
    print(X)
    print(Y)
    print(Z)
    return ' '.join(Z)
    

if __name__ == '__main__':
    print(order('is2 Thi1s T4est 3a'))


# diff approach:

# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))