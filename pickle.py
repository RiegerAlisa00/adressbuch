import pickle
from tkinter import *
from tkinter import filedialog
class Object_save:
    def __init__(self,dic,root):
        self.dic = dic
        self.root = root

    def create_ordner(self):
        try:
            os.makedirs(self.ordner)
        except FileExistsError:
            pass

    def object_save_as(self):
  
        self.root.filename =  filedialog.asksaveasfile(title = "Save file",filetypes = (("pickle files","*.pickle"),("all files","*.*")))
        filehandler = open(self.root.filename.name, 'wb') 
        pickle.dump(self.dic, filehandler)
        filehandler.close()
        
        
    def object_open(self):
        self.root.filename =  filedialog.askopenfilename(title = "Select file",filetypes = (("pickle files","*.pickle"),("all files","*.*")))
        read_file = open(self.root.filename, 'rb')
        self.dic = pickle.load(read_file)
        print(self.dic)
root = Tk()       

dic = {1:"Hallo",2:"da",3:"draußen"}
eins = Object_save(dic,root)
eins.save()
eins.open()

