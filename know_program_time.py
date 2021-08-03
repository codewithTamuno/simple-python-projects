""" a programme that tells you when last you
     ran that programme
     
     """

import datetime as dt


time_db = "time_db" # name of file

# hold the time
date = dt.datetime.now()

get_date = f"{date:%I:%M:%p}"
get_date2 = f"{date:%I:%M:%p}" # remove this

with open(time_db + ".tm", "a") as time_database:
        
    file_content = time_database.write((get_date) + "\n")
       
    try:
      print()   
      with open(time_db + ".tm") as time_database:
            
        file_content = time_database.readlines()
        # get the last time when run
        get_last = file_content[-1]
        # show 
        print(f" This {get_last} was the last time you ran this program")
           
    except IndexError as e:
      pass
            



