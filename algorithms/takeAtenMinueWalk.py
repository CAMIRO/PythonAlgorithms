# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, 
# so you decided to take the opportunity to go for a short walk. 
# The city provides its citizens with a Walk Generating App on their phones -- 
# everytime you press the button it sends you an array of one-letter strings 
# representing directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block for each letter (direction)
#  and you know it takes you one minute to traverse one city block, 
# so create a function that will return true if the walk the app 
# gives you will take you exactly ten minutes (you don't want to be early or late!) 
# and will, of course, return you to your starting point. Return false otherwise.

#some test cases for you...
# test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
# test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
# test.expect(not is_valid_walk(['w']), 'should return False');
# test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');

def is_valid_walk(walk):
    n = 0
    s = 0
    w = 0
    e = 0
    
    for x in walk:
        if x == 'n':
            n += 1
        elif x == 's':
            s += 1
        elif x == 'w':
            w += 1
        elif x == 'e':
            e += 1
    total_minutes = n + s + w + e

    if (n - s == 0) and (w - e == 0) and ( total_minutes > 9 and total_minutes < 11):
        return True
    else : return False



if __name__ == '__main__':
    print(is_valid_walk(['e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 's']))



# another approaches :

# approach 1: 
# NOTE: using the python method： count()

#     def is_valid_walk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


# approach 2 :

#     def is_valid_walk(walk):
#         if (walk.count('n') == walk.count('s') and 
#             walk.count('e') == walk.count('w') and
#             len(walk) == 10):
#                 return True
#         return False
