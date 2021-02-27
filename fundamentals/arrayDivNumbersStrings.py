# Given a mixed array of number and string representations of integers, 
# add up the string integers and subtract this from the total of the non-string integers.


# def div_con(x):
#     X = []
#     Y = []
#     sumX = 0
#     sumY = 0

#     for num in x:
#         if type(num) == int:
#             X.append(num)
#             sumX = sum(X)
#         else: 
#             MyInt = int(num)
#             Y.append(MyInt)
#             sumY = sum(Y)
        
#     return sumX - sumY



def div_con(x):
   return sum(n if isinstance(n, int) else -int(n) for n in x)

if __name__ == '__main__':
    print(div_con([9, 3, '7', '3']))


    

