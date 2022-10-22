#Using List to Create name with *

#list
Letters = {
        'N': ['*   *', '**  *', '* * *', '*  **', '*   *'],
        'I': ['*****', '  *  ', '  *  ', '  *  ', '*****'],
        'K': ['*   *', '*  * ', '**   ', '*  * ', '*   *'],
        'Z': ['*****', '   * ', '  *  ', ' *   ', '*****'],
       }  

#nickname to be used
name = "NIKZ"


#lenghh & spacing
def print_big(newList):
   for i in range(5): #range of characters
       for j,_ in enumerate(newList):
           print(Letters[newList[j]][i]+"   ",end = " ")
       print()

#final output
print_big(list(name))