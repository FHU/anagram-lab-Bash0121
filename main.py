#REMOVE PASS AND FIX THIS FUNCTION
def anagram(test1, test2):
    final1=test1.lower()
    final2=test2.lower()
    for i in final1:
        if i.isalpha():
            if i in final2:
                   continue
            else: 
                 return False
        else:
             continue
    return True
         
    
if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
   
    u_input1=input()
    u_input2=input()
    if u_input1.isspace()==True:
          print("False")
    else:
         print(anagram(u_input1, u_input2))

#Remove capital letters, and compare both strings ACII values.
#make strings and get the value of every index
#I needs to iterate through the string, make them lowercase, then find their ASCII values.