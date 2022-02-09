from tkinter import*
from tkinter import messagebox
import time
import os, sys

root = Tk()
##root.iconbitmap('Book.ico')

class Widgets(Frame):
    def __init__(self, master=None):
        root.destroy()
        
        super().__init__()
        
        self.master.geometry('500x140')
        self.master.title('Openme..')
        self.master.maxsize(500,150)
      
        
        self.label = Label(text='Type the file/app name', font=('Impact', 30, 'bold'))
        self.label.pack()
 
        self.label2 = Label(text='Open..', font=('text', 19, 'underline'))
        self.label2.place(x=4,y=58)

        self.ent = Entry(font=('Courier New', 20, 'italic'))
        self.ent.pack()

        
        self.btn = Button(text='Press Enter or Click', command= (lambda:py_file(self.ent.get())
                                                or doc_file(self.ent.get())))
        self.btn.pack(side=BOTTOM)


        self.master.bind('<Key-Return>', lambda event:py_file(self.ent.get())
                         or doc_file(self.ent.get()))
        


def py_file(name):
    """

        This function checks for python file or text files,
        in the python directory and if there is no such file it
        skip this function to the document function(doc_file).....
    
    """
    
    _open = ('%s'%name)

    
    if str(_open).endswith('.py') and _open is  not None:return os.system(_open) # check if name ends-with .py
    
    # else if no name with the extension  but name ends-with .txt open then read
    elif str(_open).endswith('.txt') and _open is not None:return os.popen(_open).read()

    # else if name does'nt ends-with .py or .txt go to or search in doc_file()
    elif _open not in os.path.basename(os.getcwd()):return doc_file('')
    
    else:
        messagebox.showinfo(title="Can't find", message=("Can't find %s"%name))


def doc_file(name):
    """
      doc_file() checks for pdf or text file in the document folder.
      If there is such file it opens it.
      
    """
    
    user = os.environ['USERNAME'] # get the current computer user name

    # This variable holds the document folder derectory
    _open = (r'C:\Users\{}\Documents\%s'.format(user)%name) 

    # if the file is a pdf or text file it opens it.
    if str(_open).endswith('.txt') or str(_open).endswith('.pdf') and _open is not None:
        return os.popen(_open).read()
    
    else: # If no such file send a message saying 'no such file'.
        messagebox.showinfo(title="Can't find", message=("Can't find %s"%name))   



def frontEnd():
    ##################################################################
    ##This function act as the front-end widget for OpenMe
    ##################################################################

    
    root.title('Openme')
    
    label = Label(text='Welcome To OPenMe.', font=('courier',20,'bold'))
    label.pack()
    
    label1 = Label(text='Loading.......',font=('courier',20,'bold'))
    label1.pack()

    content = StringVar(root)
    content.set('fff')

    
    
      
    btn = Button(root, text='click to continue', command=Widgets)
    btn.pack()
    
    root.bind('<Key-Return>', lambda event:Widgets())
    root.maxsize(300,500)
    root.mainloop()



def main():
    frontEnd()






if __name__ == '__main__':
    main()




