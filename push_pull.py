  # an algorithm for the know_programm time.
# a push and pull algo.

""" use append to put in, use pop to remove,
    the last item. then use insert to put back that
    last removed at the front so the other item will
    became the last item.
    
    """


def push_pull(item=[]):
    """
        This function is a push and pull algorithm.
        
        The paremetre is a list, that contains any type(string, int,and  float)
        
        it is best used when the program allow the user to put an item or for short; it
        is like customer requesting for a food online.
        
       if the customer request for a food and press the send button,
       it push the request into the server then those at the backend or
       the cheff pull out the customer request.
       
       >>> items = ["item1", "item2", "item3"]
       >>> store_item = item.pop()
       >>> item.insert(0, store_item)
       .... ["item3", "item1", "item2"]
       
    """
   
    try: # if list is empty
         # store the last item here
         last_item = item.pop()
         print(f"this is the last item {last_item=}")
    except IndexError: # if list is empty
         print("list is empty")
           
    try:
         # insert the last item in the first place
         item.insert(0, last_item)
         print(f"{item[0]} is now the first item")
    except UnboundLocalError: # if list is empty
            #print("can't insert")
          pass
    return item
   

if __name__ == "__main__":
    
    print(push_pull([1,2,3]))