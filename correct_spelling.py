#!usr/bin/env python

#Author: Fred Franklin

## it is just an inverse of palindrom, although it is not
## it is used to check the spelling of two words
## then correct the incorrect one.
## the programm assumes that the first word is correct while,
## the second is incorrect.

import random
import time

correct_word = input('enter the correct word> ')
wrong_word = input('enter the incorrect one> ')


def correct_spelling(word1, word2):
    ## word1 for the real word then word2 for the incorrect word
    ## please help me check, if it is correct


    if len(word1) != len(word2): # the length most be equal
        # if the length for both words are
        # not equal it exits the code
        # you can use the print key-word if you like
        
        return False
    
    if len(word1) == 1 and len(word2) == 1: # the lenght most be greater than one
        return 'Can\'t check speeling'
    
    con_list1 = list(word1) # convert to list(that is split string)
    con_list2 = list(word2) # convert to list
    #print(con_list1) # you can uncomment this, it is used for testing the programme
    #print(''.join(con_list1)) # also used for testing

    print('checking......')
    while con_list1 != con_list2:  
           
          i = random.randint(-1, 1) # randomly pick number between -1 to 1
          j = random.randint(0, i + 1) # randomly pick number, from 0 to the sum of either -1 + 1 or 1 + 1
          
          con_list1[i], con_list1[j] = con_list1[j], con_list1[i] #shuffle  the list 
          print(con_list1)

          if con_list1 == con_list2:
              time.sleep(3)
              print('got it')
              print('the correct word is ' + ''.join(con_list1))
              break
                
       
correct_spelling(wrong_word, correct_word)
