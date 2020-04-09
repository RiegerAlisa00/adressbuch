from tkinter import *

class GUI:
    def __init__(self,surface):
        self.addressbook = Addressbook()
        """ GUI Fenster """
        self.surface = surface
        
        """ Hauptseit: Buttons """
        self.b_add = Button(self.surface)
        self.b_edit = Button(self.surface)
        self.b_delete = Button(self.surface)
        self.b_sort_name = Button(self.surface)
        self.b_sort_plz = Button(self.surface)
        
        """ Hauptseit: Listenbox """
        self.listbox = Listbox(self.surface)
        self.index = None
        self.inhalt = None
        self.scroll = Scrollbar(self.surface,orient=VERTICAL)
        """ Hauptseit: Label: Inhalt/Informationen der Person """
        self.label_info_person = Label(self.surface)
        
        """ Add_Seite: Labels """
        self.label_add_firstName = Label(self.surface)
        self.label_add_lastName = Label(self.surface)
        self.label_add_address = Label(self.surface)
        self.label_add_city = Label(self.surface)
        self.label_add_state = Label(self.surface)
        self.label_add_plz = Label(self.surface)
        self.label_add_phone = Label(self.surface)
        
        """ Add_Seite: Entrys """
        self.entry_add_firstName = Entry(self.surface)
        self.entry_add_lastName = Entry(self.surface)
        self.entry_add_address = Entry(self.surface)
        self.entry_add_city = Entry(self.surface)
        self.entry_add_state = Entry(self.surface)
        self.entry_add_plz = Entry(self.surface)
        self.entry_add_phone = Entry(self.surface)
        
        """ Add_Seite: Speicher Button """
        self.b_add_save = Button(self.surface)
        
        """ Edit_Seite: Labels """
        self.label_edit_firstName = Label(self.surface)
        self.label_edit_lastName = Label(self.surface)
        self.label_edit_address = Label(self.surface)
        self.label_edit_city = Label(self.surface)
        self.label_edit_state = Label(self.surface)
        self.label_edit_plz = Label(self.surface)
        self.label_edit_phone = Label(self.surface)
        
        """ Edit_Seite: Labels wo Vorname und Nachname von der Person schon steht """
        self.label_edit_info_firstName = Label(self.surface)
        self.label_edit_info_lastName = Label(self.surface)
        
        """ Edit_Seite: Entrys """
        self.entry_edit_address = Entry(self.surface)
        self.entry_edit_city = Entry(self.surface)
        self.entry_edit_state = Entry(self.surface)
        self.entry_edit_plz = Entry(self.surface)
        self.entry_edit_phone = Entry(self.surface)
        
        """ Edit_Seite: Speicher Button """
        self.b_edit_save = Button(self.surface)
        
    def clear_design(self):
        self.b_add.grid_forget()
        self.b_edit.grid_forget()
        self.b_delete.grid_forget()
        self.b_sort_name.grid_forget()
        self.b_sort_plz.grid_forget()

        self.listbox.grid_forget()
        self.scroll.grid_forget()

        self.label_info_person.grid_forget()

        self.label_add_firstName.grid_forget()
        self.label_add_lastName.grid_forget()
        self.label_add_address.grid_forget()
        self.label_add_city.grid_forget()
        self.label_add_state.grid_forget()
        self.label_add_plz.grid_forget()
        self.label_add_phone.grid_forget()

        self.entry_add_firstName.grid_forget()
        self.entry_add_lastName.grid_forget()
        self.entry_add_address.grid_forget()
        self.entry_add_city.grid_forget()
        self.entry_add_state.grid_forget()
        self.entry_add_plz.grid_forget()
        self.entry_add_phone.grid_forget()

        self.b_add_save.grid_forget()

        self.label_edit_firstName.grid_forget()
        self.label_edit_lastName.grid_forget()
        self.label_edit_address.grid_forget()
        self.label_edit_city.grid_forget()
        self.label_edit_state.grid_forget()
        self.label_edit_plz.grid_forget()
        self.label_edit_phone.grid_forget()

        self.label_edit_info_firstName.grid_forget()

        self.label_edit_info_lastName.grid_forget()


        self.entry_edit_address.grid_forget()
        self.entry_edit_city.grid_forget()
        self.entry_edit_state.grid_forget()
        self.entry_edit_plz.grid_forget()
        self.entry_edit_phone.grid_forget()

        self.b_edit_save .grid_forget()

        
    def menubar(self):
        menubar = Menu(self.surface)
        filemenu = Menu(self.surface, tearoff=0)
        filemenu.add_command(label="New",command=self.main)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.surface.destroy)
        menubar.add_cascade(label="File", menu=filemenu)


        self.surface.config(menu=menubar)
    def name_sort(self):
        self.addressbook.sort_name()
        self.main()
    def plz_sort(self):
        self.addressbook.sort_plz()
        self.main()
    def main(self):
        self.clear_design()
        self.listbox.delete(0,'end')
        self.b_add.config(text='Add',command=self.add_side)
        self.b_edit.config(text='Edit',command=self.edit_side)
        self.b_delete.config(text='Delete',command=self.delete_function)
        self.b_sort_name.config(text='Sort by name',command=self.name_sort)
        self.b_sort_plz.config(text='Sort by PLZ',command=self.plz_sort)

        
        self.listbox["yscrollcommand"]=self.scroll.set
        self.scroll["command"]=self.listbox.yview
        for i in self.addressbook.person_list:
            name = i.firstName, i.lastName
            self.listbox.insert(END, name)
        self.listbox.grid(row=1,column=1,columnspan=4,sticky=N+E+S+W)
        self.scroll.grid(row=1,column=4, sticky=E+N+S)
        self.listbox.bind("<<ListboxSelect>>",lambda x: self.listbox_active())
        
        
        self.label_info_person.grid(row=1,column=5,rowspan=4,columnspan=10)


        
        self.b_add.grid(row=5,column=1,padx=10,pady=50)
        self.b_edit.grid(row=5,column=2,padx=10,pady=50)
        self.b_delete.grid(row=5,column=3,padx=10,pady=50)
        self.b_sort_name.grid(row=5,column=4,padx=10,pady=50)
        self.b_sort_plz.grid(row=5,column=5,padx=10,pady=50)
    def delete_function(self):
        self.addressbook.person_del(self.index)
        self.main()
    def listbox_active(self):
        try:
            self.index = self.listbox.curselection()[0]
            self.inhalt = self.addressbook.person_list[self.index]
            self.edit_label_info_person_text()
        except IndexError:
            self.label_info_person.config(text='')
    def edit_label_info_person_text(self):
        text="Vorname: {}\nNachname: {}\nAdresse: {}\nStadt: {}\nBundesland: {}\nPLZ: {}\nTelefonnummer: {}\n".format(self.inhalt.firstName,self.inhalt.lastName,self.inhalt.address,self.inhalt.city,self.inhalt.state,self.inhalt.plz,self.inhalt.phone)
        self.label_info_person.config(text=text,justify=LEFT,font=13)
        #self.label_info_person["anchor"] = W
    def add_side(self):
        self.clear_design()
        self.label_add_firstName.config(text="Vorname")
        self.label_add_firstName.grid(row=1,column=1)

        self.label_add_lastName.config(text="Nachname")
        self.label_add_lastName.grid(row=2,column=1)

        self.label_add_address.config(text="Adresse")
        self.label_add_address.grid(row=3,column=1)

        self.label_add_city.config(text="Stadt")
        self.label_add_city.grid(row=4,column=1)

        self.label_add_state.config(text="Bundesland")
        self.label_add_state.grid(row=5,column=1)

        self.label_add_plz.config(text="PLZ")
        self.label_add_plz.grid(row=6,column=1)

        self.label_add_phone.config(text="Telefonnummer")
        self.label_add_phone.grid(row=7,column=1)

        self.entry_add_firstName.grid(row=1,column=2)

        self.entry_add_lastName.grid(row=2,column=2)

        self.entry_add_address.grid(row=3,column=2)

        self.entry_add_city.grid(row=4,column=2)

        self.entry_add_state.grid(row=5,column=2)

        self.entry_add_plz.grid(row=6,column=2)

        self.entry_add_phone.grid(row=7,column=2)

        self.b_add_save.config(text="Speichern",command=self.person_add)
        self.b_add_save.grid(row=8,column=3)
    def person_add(self):
        firstName = self.entry_add_firstName.get()
        lastName = self.entry_add_lastName.get()
        address = self.entry_add_address.get()
        city = self.entry_add_city.get()
        state = self.entry_add_state.get()
        plz = self.entry_add_plz.get()
        phone = self.entry_add_phone.get()
        self.addressbook.create_person(firstName,lastName,address,city,state,plz,phone)
        self.delete_entry_add_text()
        self.main()
    def delete_entry_add_text(self):
        self.entry_add_firstName.delete(0,'end')
        self.entry_add_lastName.delete(0,'end')
        self.entry_add_address.delete(0,'end')
        self.entry_add_city.delete(0,'end')
        self.entry_add_state.delete(0,'end')
        self.entry_add_plz.delete(0,'end')
        self.entry_add_phone.delete(0,'end')
    def delete_entry_edit_text(self):
        self.entry_edit_address.delete(0,'end')
        self.entry_edit_city.delete(0,'end')
        self.entry_edit_state.delete(0,'end')
        self.entry_edit_plz.delete(0,'end')
        self.entry_edit_phone.delete(0,'end')
    def edit_side(self):
        self.clear_design()
        self.label_edit_firstName.config(text="Vorname")
        self.label_edit_firstName.grid(row=1,column=1)

        self.label_edit_lastName.config(text="Nachname")
        self.label_edit_lastName.grid(row=2,column=1)

        self.label_edit_address.config(text="Adresse")
        self.label_edit_address.grid(row=3,column=1)

        self.label_edit_city.config(text="Stadt")
        self.label_edit_city.grid(row=4,column=1)

        self.label_edit_state.config(text="Bundesland")
        self.label_edit_state.grid(row=5,column=1)

        self.label_edit_plz.config(text="PLZ")
        self.label_edit_plz.grid(row=6,column=1)

        self.label_edit_phone.config(text="Telefonnummer")
        self.label_edit_phone.grid(row=7,column=1)


        self.label_edit_info_firstName.config(text=self.inhalt.firstName,justify=LEFT)
        self.label_edit_info_firstName.grid(row=1,column=2)

        self.label_edit_info_lastName.config(text=self.inhalt.lastName,justify=LEFT)
        self.label_edit_info_lastName.grid(row=2,column=2)

        self.entry_edit_address.insert(0,self.inhalt.address)
        self.entry_edit_address.grid(row=3,column=2)

        self.entry_edit_city.insert(0,self.inhalt.city)
        self.entry_edit_city.grid(row=4,column=2)

        self.entry_edit_state.insert(0,self.inhalt.state)
        self.entry_edit_state.grid(row=5,column=2)

        self.entry_edit_plz.insert(0,self.inhalt.plz)
        self.entry_edit_plz.grid(row=6,column=2)

        self.entry_edit_phone.insert(0,self.inhalt.phone)
        self.entry_edit_phone.grid(row=7,column=2)

        self.b_edit_save.config(text="Speichern",command=self.person_edit)
        self.b_edit_save.grid(row=8,column=3)
    def person_edit(self):
        address = self.entry_edit_address.get()
        city = self.entry_edit_city.get()
        state = self.entry_edit_state.get()
        plz = self.entry_edit_plz.get()
        phone = self.entry_edit_phone.get()
        self.inhalt.person_edit(address,city,state,plz,phone)
        self.delete_entry_edit_text()
        self.main()


class Person:
    def __init__(self,fname,lname,adr,city,state,plz,phone):
        self.firstName = fname
        self.lastName = lname
        self.address = adr
        self.city = city
        self.state = state
        self.plz = plz
        self.phone = phone

    def person_edit(self,adr,city,state,plz,phone):
        self.address = adr
        self.city = city
        self.state = state
        self.plz = plz
        self.phone = phone

    def person_print(self):
        print(self.firstName)
        print(self.lastName)
        print(self.address)
        print(self.city)
        print(self.state)
        print(self.plz)
        print(self.phone)

class Addressbook:
    def __init__(self):
        self.person_list = []
    def create_person(self,fname,lname,adr,city,state,plz,phone):
        self.person_list.append(Person(fname,lname,adr,city,state,plz,phone))
    def print_person(self):
        for i in self.person_list:
            i.person_print()
            print('')
    def sort_plz(self):
        self.person_list.sort(key=lambda person: person.plz)
    def sort_name(self):
        self.person_list.sort(key=lambda person: person.lastName)
    def person_del(self,pos):
        del self.person_list[pos]

surface = Tk()

Addressbook = GUI(surface)
Addressbook.menubar()
