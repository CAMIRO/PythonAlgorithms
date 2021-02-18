# Get the Middle Character:
# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.
#Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"

def get_middle(s):
    # Checking if it's even or Odd
    is_even = False
    if len(s) % 2 == 0:
       is_even = True 
    # Calculating the middle position and middle charater(s)
    middle_position = (0 + len(s)) // 2
    middle_charater = s[middle_position]
    middle_charaters = s[middle_position - 1] + s[middle_position]
    # Filtering result if its even or Odd
    if is_even:
        return  middle_charaters 
    else: 
        return  middle_charater

if __name__ == '__main__':
    print(get_middle('middle'))


# another approaches:
# def get_middle(s):
#    return s[(len(s)-1)/2:len(s)/2+1]


# NOTE: using the python method： divmod()
# def get_middle(s):
#     index, odd = divmod(len(s), 2)
#     return s[index] if odd else s[index - 1:index + 1]