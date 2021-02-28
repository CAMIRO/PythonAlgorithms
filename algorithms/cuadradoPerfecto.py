# You might know some pretty large perfect squares. 
# But what about the NEXT one?

# Complete the findNextSquare method that finds 
# the next integral perfect square after the one passed as a parameter. 
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 
# should be returned. You may assume the parameter is positive.
import math

def find_next_square(sq):

    if math.sqrt(sq).is_integer():
        sq += 1
        while math.sqrt(sq).is_integer() == False:
            if math.sqrt(sq).is_integer():
                print('hell')
                break
            sq += 1
        return sq
    else: return -1
        


if __name__ == '__main__':
    print(find_next_square(625))