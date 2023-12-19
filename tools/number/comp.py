def sumofdigits(y):  #gets a number and returns sum of digits (for example 234 =>  9)
    summ = 0 # empty container for my func
    y = str(y) # converts y to str (arry of seperate string)
    for i in y : #loop thats taking every seperate string and converting to int and adding to my summ continter
        i = int(i)
        summ += i
    return (summ) 



def ispal (num):# return True if the number is palindrome (1221 , 34543, ....)
    num_str = str(num) #converts num to str (arry of seperate string)
    if num_str == num_str[::-1]:#using slicers ability to run arrys backwards
        return True #if num is palindrome then return true
    else: return False #if not return false









    



