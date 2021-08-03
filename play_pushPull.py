from typing import List
from push_pull import push_pull

def play(original_items=[]) -> List:
    
    counter = 0
    choices = ["y", "n"]
    
    # copy original list and make use of it.
    copy_items = original_items.copy()
    
    while counter <= 5:
        
        user_input = input("put an item: ")
        
        original_items.append(user_input)
        
        copy_items = original_items.copy()
        
        counter += 1
        
    print("Ok! The play start here", end="\n")
    
    # a loop stopper
    stopper = True
    while stopper:
        
        user_input = str(input("The play start. type 'y' to start or \
        'n' to stop "))
        if user_input == choices[0]:
            print(push_pull(copy_items))
        
        elif user_input == choices[1]:
            print("we did't touch your list")
            print(f"here it is: {original_items=}. supprised?")
            stopper = False
            

play()