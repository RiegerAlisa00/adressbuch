from tkinter import *
import pickle
from tkinter import filedialog

class GUI:
    def __init__(self,surface):
        self.addressbook = Addressbook()
        """ GUI Fenster """
        self.surface = surface
        self.title = ''
        """ Object save """
        self.object_file_path = None
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

        """Eingabe Informationen: Labels"""
        self.label_info_firstName = Label(self.surface)
        self.label_info_lastName = Label(self.surface)
        self.label_info_address = Label(self.surface)
        self.label_info_city = Label(self.surface)
        self.label_info_state = Label(self.surface)
        self.label_info_plz = Label(self.surface)
        self.label_info_phone = Label(self.surface)
        
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
    #Alle inhalte werden im Fenster ausgeblendet
    def clear_design(self):
        """ Hauptseit: Buttons """
        self.b_add.grid_forget()
        self.b_edit.grid_forget()
        self.b_delete.grid_forget()
        self.b_sort_name.grid_forget()
        self.b_sort_plz.grid_forget()
        """ Hauptseit: Listenbox """
        self.listbox.grid_forget()
        self.scroll.grid_forget()
        """ Hauptseit: Label: Inhalt/Informationen der Person """
        self.label_info_person.grid_forget()
        """Eingabe Informationen: Labels"""
        self.label_info_firstName.grid_forget()
        self.label_info_lastName.grid_forget()
        self.label_info_address.grid_forget()
        self.label_info_city.grid_forget()
        self.label_info_state.grid_forget()
        self.label_info_plz.grid_forget()
        self.label_info_phone.grid_forget()
        """ Add_Seite: Labels """
        self.label_add_firstName.grid_forget()
        self.label_add_lastName.grid_forget()
        self.label_add_address.grid_forget()
        self.label_add_city.grid_forget()
        self.label_add_state.grid_forget()
        self.label_add_plz.grid_forget()
        self.label_add_phone.grid_forget()
        """ Add_Seite: Entrys """
        self.entry_add_firstName.grid_forget()
        self.entry_add_lastName.grid_forget()
        self.entry_add_address.grid_forget()
        self.entry_add_city.grid_forget()
        self.entry_add_state.grid_forget()
        self.entry_add_plz.grid_forget()
        self.entry_add_phone.grid_forget()
        """ Add_Seite: Speicher Button """
        self.b_add_save.grid_forget()
        """ Edit_Seite: Labels """
        self.label_edit_firstName.grid_forget()
        self.label_edit_lastName.grid_forget()
        self.label_edit_address.grid_forget()
        self.label_edit_city.grid_forget()
        self.label_edit_state.grid_forget()
        self.label_edit_plz.grid_forget()
        self.label_edit_phone.grid_forget()
        """ Edit_Seite: Labels wo Vorname und Nachname von der Person schon steht """
        self.label_edit_info_firstName.grid_forget()
        self.label_edit_info_lastName.grid_forget()

        """ Edit_Seite: Entrys """
        self.entry_edit_address.grid_forget()
        self.entry_edit_city.grid_forget()
        self.entry_edit_state.grid_forget()
        self.entry_edit_plz.grid_forget()
        self.entry_edit_phone.grid_forget()
        """ Edit_Seite: Speicher Button """
        self.b_edit_save .grid_forget()

   #Methode: wo die Menubar erstellt wird    
    def menubar(self):
        menubar = Menu(self.surface)
        filemenu = Menu(self.surface, tearoff=0)
        filemenu.add_command(label="New",command=self.object_new)
        filemenu.add_command(label="Save",command=self.object_save)
        filemenu.add_command(label="Save As",command=self.object_save_as)
        filemenu.add_command(label="Open",command=self.object_open)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.surface.destroy)
        menubar.add_cascade(label="File", menu=filemenu)


        self.surface.config(menu=menubar)
    #Hier wird die Methode aufgerufen, die Name in der Liste nach Nachnamen sortiert wird
    def name_sort(self):
        self.addressbook.sort_name()
        self.main()
    #Hier wird die Methode aufgerufen, die Name in der Liste nach PLZ sortiert wird
    def plz_sort(self):
        self.addressbook.sort_plz()
        self.main()
    #Hier werden die Bedingungen für die Eingaben erstellt
    def lable_info_text(self):
        info_text = " muss mit einem Großbuchstaben anfangen"
        info_zahl = " darf nur aus Zahlen bestehen"
        self.label_info_firstName.config(text="Vorname"+info_text,fg = "black")
        self.label_info_lastName.config(text="Nachname"+info_text,fg = "black")
        self.label_info_address.config(text="Adresse"+info_text,fg = "black")
        self.label_info_city.config(text="Stadt"+info_text,fg = "black")
        self.label_info_state.config(text="Bundesland"+info_text,fg = "black")
        self.label_info_plz.config(text="PLZ"+info_zahl,fg = "black")
        self.label_info_phone.config(text="Telefonnummer"+info_zahl,fg = "black")
    #Hier ist das Hauptfenster, also die Buttons um Personen hinzuzufügen, bearbeiten und löschen, sowie die Listenbox nach Nachname oder Plz zu sortieren. Auch die Listenbox und den Inhalt der ausgewählten Person werden angezeigt
    def main(self):
        self.listbox_active()#es wird geschaut ob eine Person in der Listenbox makiert ist
        self.surface.title(self.title)#der Fenstertitel wird aktualisiert
        self.clear_design()#alles wird ausgeblendet
        self.delete_entry_add_text()#die Inhalte der Eingabenfelder der Seite Person Add werden gelöscht, dass das Feld wider leer ist
        self.delete_entry_edit_text()#die Inhalte der Eingabenfelder der Seite Person Add werden gelöscht, dass das Feld wider leer ist
        self.lable_info_text()
        if len(self.addressbook.person_list) < 1:#ist die Listbox leer kann man die Buttons Edit und Delete nicht verwenden
            self.b_edit.config(text='Edit',command=self.main)
            self.b_delete.config(text='Delete',command=self.main)
        else:
            self.b_edit.config(text='Edit',command=self.edit_side)
            self.b_delete.config(text='Delete',command=self.delete_function)
        self.listbox.delete(0,'end')#alter Listbox stand wird gelöscht
        self.b_add.config(text='Add',command=self.add_side)
        self.b_sort_name.config(text='Sort by name',command=self.name_sort)
        self.b_sort_plz.config(text='Sort by PLZ',command=self.plz_sort)

        """Scrollbar wird zur Listbox hinzugefügt"""
        self.listbox["yscrollcommand"]=self.scroll.set
        self.scroll["command"]=self.listbox.yview
        for i in self.addressbook.person_list:#die aktuelle Liste wird in der Listbox angezeigt
            name = i.firstName, i.lastName
            self.listbox.insert(END, name)
        #positionierung der Listbox und Scrollbar
        self.listbox.grid(row=1,column=1,columnspan=4,sticky=N+E+S+W)
        self.scroll.grid(row=1,column=4, sticky=E+N+S)
        self.listbox.bind("<<ListboxSelect>>",lambda x: self.listbox_active())#wenn man auf Person in der Listbox wählt etwas passiert
        
        """Hier gebe ich die Positionen der Buttons und das Lable an"""
        self.label_info_person.grid(row=1,column=5,rowspan=4,columnspan=10)


        
        self.b_add.grid(row=5,column=1,padx=10,pady=50)
        self.b_edit.grid(row=5,column=2,padx=10,pady=50)
        self.b_delete.grid(row=5,column=3,padx=10,pady=50)
        self.b_sort_name.grid(row=5,column=4,padx=10,pady=50)
        self.b_sort_plz.grid(row=5,column=5,padx=10,pady=50)
    #Hier wird die Methode aufgerufen um die Person zu löschen
    def delete_function(self):
        self.addressbook.person_del(self.index)
        self.main()
   #Hier wird herrausgefunden welche Person ausgewählt wurde
    def listbox_active(self):
        try:
            self.index = self.listbox.curselection()[0]#gibt den Index der ausgewählten Person in der Liste an
            self.inhalt = self.addressbook.person_list[self.index]#gibt die Informationen der ausgewählten Person in der Liste an
            self.edit_label_info_person_text()
        except IndexError:
            self.label_info_person.config(text='')
   #Hier werden die ganzen Informatione der jeweiligen ausgewählten Person auf der Hauptseite an der Seite angezeigt
    def edit_label_info_person_text(self):
        text="Vorname: {}\nNachname: {}\nAdresse: {}\nStadt: {}\nBundesland: {}\nPLZ: {}\nTelefonnummer: {}\n".format(self.inhalt.firstName,self.inhalt.lastName,self.inhalt.address,self.inhalt.city,self.inhalt.state,self.inhalt.plz,self.inhalt.phone)
        self.label_info_person.config(text=text,justify=LEFT,font=13)
        #self.label_info_person["anchor"] = W
   #Hier wird die Seite wo ich Personen hinzufügen kann erstellt
    def add_side(self):
        self.clear_design()
        self.label_add_firstName.config(text="Vorname")#hier wird der Textinhalt des Lables festgelegt
        self.label_add_firstName.grid(row=1,column=1)#hier wird die Position des Lables festgelegt

        self.label_add_lastName.config(text="Nachname")#hier wird der Textinhalt des Lables festgelegt
        self.label_add_lastName.grid(row=2,column=1)#hier wird die Position des Lables festgelegt

        self.label_add_address.config(text="Adresse")#hier wird der Textinhalt des Lables festgelegt
        self.label_add_address.grid(row=3,column=1)

        self.label_add_city.config(text="Stadt")#hier wird der Textinhalt des Lables festgelegt
        self.label_add_city.grid(row=4,column=1)#hier wird die Position des Lables festgelegt

        self.label_add_state.config(text="Bundesland")#hier wird der Textinhalt des Lables festgelegt
        self.label_add_state.grid(row=5,column=1)

        self.label_add_plz.config(text="PLZ")#hier wird der Textinhalt des Lables festgelegt
        self.label_add_plz.grid(row=6,column=1)#hier wird die Position des Lables festgelegt

        self.label_add_phone.config(text="Telefonnummer")#hier wird der Textinhalt des Lables festgelegt
        self.label_add_phone.grid(row=7,column=1)#hier wird die Position des Lables festgelegt
        
        """Hier werden die Positionen der Eingabefelder festgelegt"""
        self.entry_add_firstName.grid(row=1,column=2)

        self.entry_add_lastName.grid(row=2,column=2)

        self.entry_add_address.grid(row=3,column=2)

        self.entry_add_city.grid(row=4,column=2)

        self.entry_add_state.grid(row=5,column=2)

        self.entry_add_plz.grid(row=6,column=2)

        self.entry_add_phone.grid(row=7,column=2)
        
        info_text = " muss mit einem Großbuchstaben anfangen"
        info_zahl = " darf nur aus Zahlen bestehen"
        self.label_info_firstName.config(text="Vorname"+info_text)
        self.label_info_firstName.grid(row=1,column=3)

        self.label_info_lastName.config(text="Nachname"+info_text)
        self.label_info_lastName.grid(row=2,column=3)

        self.label_info_address.config(text="Adresse"+info_text)
        self.label_info_address.grid(row=3,column=3)

        self.label_info_city.config(text="Stadt"+info_text)
        self.label_info_city.grid(row=4,column=3)

        self.label_info_state.config(text="Bundesland"+info_text)
        self.label_info_state.grid(row=5,column=3)

        self.label_info_plz.config(text="PLZ"+info_zahl)
        self.label_info_plz.grid(row=6,column=3)

        self.label_info_phone.config(text="Telefonnummer"+info_zahl)
        self.label_info_phone.grid(row=7,column=3)

        self.b_add_save.config(text="Speichern",command=self.person_add)
        self.b_add_save.grid(row=8,column=3)
   #Hier werden die Eingaben geprüft ob sie passen
    def check_entry(self,var,typ,entry,info):
        info_text ="Fängt nicht mit einem Großbuchstaben an oder das Feld ist leer"
        info_zahl = "Besteht nicht nur aus Zahlen oder das Feld ist leer oder im Feld befindet sich ein Leerzeichen"
        if typ == "state" or typ == "firstname" or typ == "lastname" or typ == "city":
            if var.replace(' ','').isalpha():#alle Leerzeichen werden entfernt und es wird geschaut ob nur Buchstaben in der Eingabe sind
                if var[0] == var[0].upper():#wird geschaut ob der 1. Buchstabe Großgeschrieben ist
                    entry.config(background = "white")
                    info.config(fg = "black")
                    return True
                else:
                    entry.config(background = "red")
                    info.config(fg = "red",text=info_text)
                    return False
            else:
                entry.config(background = "red")
                info.config(fg = "red",text=info_text)
                return False
        elif typ == "address":
            if var.replace(' ','').isalnum():#alle Leerzeichen werden entfernt und es wird geschaut ob Buchstaben und/oder Zahlen in der Eingabe sind
                if var[0] == var[0].upper():
                    entry.config(background = "white")
                    info.config(fg = "black")
                    return True
                else:
                    entry.config(background = "red")
                    info.config(fg = "red",text=info_text)
                    return False
            else:
                entry.config(background = "red")
                info.config(fg = "red",text=info_text)
                return False
        elif typ == "plz":
            if var.isnumeric():#wird geschaut ob nur Zahlen in der Eingabe sind
                entry.config(background = "white")
                info.config(fg = "black")
                return var.isnumeric()
            else:
                entry.config(background = "red")
                info.config(fg = "red",text=info_zahl)
                return var.isnumeric()
            
        elif typ == "phone":
            if var.isnumeric():
                entry.config(background = "white")
                info.config(fg = "black")
                return True
            elif var.isalnum():
                entry.config(background = "red")
                info.config(fg = "red",text=info_zahl)
                return False
            else:
                entry.config(background = "red")
                info.config(fg = "red",text=info_zahl)
                return False
   #Hier werden die Eingaben von der Seite wo man Personen erstellen kann bearbeiten bzw. in die Person wird erstellt          
    def person_add(self):
        firstName = self.entry_add_firstName.get()
        lastName = self.entry_add_lastName.get()
        address = self.entry_add_address.get()
        city = self.entry_add_city.get()
        state = self.entry_add_state.get()
        plz = self.entry_add_plz.get()
        phone = self.entry_add_phone.get()
        
        if firstName =="" and lastName == "" and address == "" and city == "" and state == "" and plz == "" and phone == "":
            #sind alle Engabefelder leer kommt man wieder zur Hauptseite und nichts wurde gespeichert
            self.main()
        else:
            check_firstName = self.check_entry(firstName,"firstname",self.entry_add_firstName,self.label_info_firstName)
            check_lastName = self.check_entry(lastName,"lastname",self.entry_add_lastName,self.label_info_lastName)
            check_address = self.check_entry(address,"address",self.entry_add_address,self.label_info_address)
            check_city = self.check_entry(city,"city",self.entry_add_city,self.label_info_city)
            check_state = self.check_entry(state,"state",self.entry_add_state,self.label_info_state)
            check_plz = self.check_entry(plz,"plz",self.entry_add_plz,self.label_info_plz)
            check_phone = self.check_entry(phone,"phone",self.entry_add_phone,self.label_info_phone)
            
            if check_firstName == True and check_lastName == True and check_address == True and check_city == True and check_state == True and check_plz == True and check_phone == True:
                firstName = firstName.replace(' ','')
                lastName = lastName.replace(' ','')
                self.addressbook.create_person(firstName,lastName,address,city,state,plz,phone)
                self.delete_entry_add_text()
                self.main()
            else:
                self.person_add()
    #Hier werden die Inhalte der Eingabenfelder der Seite Person hinzufügen gelöscht, so das die Eingabenfelder wierder leer sind
    def delete_entry_add_text(self):
        self.entry_add_firstName.delete(0,'end')
        self.entry_add_firstName.config(background = "white")
        
        self.entry_add_lastName.delete(0,'end')
        self.entry_add_lastName.config(background = "white")
        
        self.entry_add_address.delete(0,'end')
        self.entry_add_address.config(background = "white")
        
        self.entry_add_city.delete(0,'end')
        self.entry_add_city.config(background = "white")
        
        self.entry_add_state.delete(0,'end')
        self.entry_add_state.config(background = "white")
        
        self.entry_add_plz.delete(0,'end')
        self.entry_add_plz.config(background = "white")
        
        self.entry_add_phone.delete(0,'end')
        self.entry_add_phone.config(background = "white")
   #Hier werden die Inhalte der Eingabenfelder der Seite Person bearbeiten gelöscht, so das die Eingabenfelder wierder leer sind
    def delete_entry_edit_text(self):
        self.entry_edit_address.delete(0,'end')
        self.entry_edit_address.config(background = "white")
        
        self.entry_edit_city.delete(0,'end')
        self.entry_edit_city.config(background = "white")
        
        self.entry_edit_state.delete(0,'end')
        self.entry_edit_state.config(background = "white")
        
        self.entry_edit_plz.delete(0,'end')
        self.entry_edit_plz.config(background = "white")
        
        self.entry_edit_phone.delete(0,'end')
        self.entry_edit_phone.config(background = "white")
    #Hier wird die Seite wo ich Personen bearbieten kann erstellt
    def edit_side(self):
        self.clear_design()
        if len(self.addressbook.person_list) < 1:
            self.index = None
            self.inhalt = None
        try:
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

            info_text = " muss mit einem Großbuchstaben anfangen"
            info_zahl = " darf nur aus Zahlen bestehen"
            

            self.label_info_address.config(text="Adresse"+info_text)
            self.label_info_address.grid(row=3,column=3)

            self.label_info_city.config(text="Stadt"+info_text)
            self.label_info_city.grid(row=4,column=3)

            self.label_info_state.config(text="Bundesland"+info_text)
            self.label_info_state.grid(row=5,column=3)

            self.label_info_plz.config(text="PLZ"+info_zahl)
            self.label_info_plz.grid(row=6,column=3)

            self.label_info_phone.config(text="Telefonnummer"+info_zahl)
            self.label_info_phone.grid(row=7,column=3)

            self.b_edit_save.config(text="Speichern",command=self.person_edit)
            self.b_edit_save.grid(row=8,column=3)
        except AttributeError:
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


            self.label_edit_info_firstName.config(text='',justify=LEFT)
            self.label_edit_info_firstName.grid(row=1,column=2)

            self.label_edit_info_lastName.config(text='',justify=LEFT)
            self.label_edit_info_lastName.grid(row=2,column=2)

            self.entry_edit_address.insert(0,'')
            self.entry_edit_address.grid(row=3,column=2)

            self.entry_edit_city.insert(0,'')
            self.entry_edit_city.grid(row=4,column=2)

            self.entry_edit_state.insert(0,'')
            self.entry_edit_state.grid(row=5,column=2)

            self.entry_edit_plz.insert(0,'')
            self.entry_edit_plz.grid(row=6,column=2)

            self.entry_edit_phone.insert(0,'')
            self.entry_edit_phone.grid(row=7,column=2)

            info_text = " muss mit einem Großbuchstaben anfangen"
            info_zahl = " darf nur aus Zahlen bestehen"
            

            self.label_info_address.config(text="Adresse"+info_text)
            self.label_info_address.grid(row=3,column=3)

            self.label_info_city.config(text="Stadt"+info_text)
            self.label_info_city.grid(row=4,column=3)

            self.label_info_state.config(text="Bundesland"+info_text)
            self.label_info_state.grid(row=5,column=3)

            self.label_info_plz.config(text="PLZ"+info_zahl)
            self.label_info_plz.grid(row=6,column=3)

            self.label_info_phone.config(text="Telefonnummer"+info_zahl)
            self.label_info_phone.grid(row=7,column=3)

            self.b_edit_save.config(text="Speichern",command=self.main)
            self.b_edit_save.grid(row=8,column=3)
    #Hier werden die Eingaben von der Seite wo man Personen bearbeiten kann bearbeiten
    def person_edit(self):
        address = self.entry_edit_address.get()
        check_address = self.check_entry(address,"address",self.entry_edit_address,self.label_info_address)
        
        city = self.entry_edit_city.get()
        check_city = self.check_entry(city,"city",self.entry_edit_city,self.label_info_city)
        
        state = self.entry_edit_state.get()
        check_state = self.check_entry(state,"state",self.entry_edit_state,self.label_info_state)
        
        plz = self.entry_edit_plz.get()
        check_plz = self.check_entry(plz,"plz",self.entry_edit_plz,self.label_info_plz)
        
        phone = self.entry_edit_phone.get()
        check_phone = self.check_entry(phone,"phone",self.entry_edit_phone,self.label_info_phone)
        
        if check_address == True and check_city == True and check_state == True and check_plz == True and check_phone == True:
            self.inhalt.person_edit(address,city,state,plz,phone)
            self.delete_entry_edit_text()
            self.main()
        else:
            self.person_edit()
    #Hier wird das Objekt/Adressbuch als pickle Datei gespeichert
    def object_save_as(self):
        self.surface.filename =  filedialog.asksaveasfile(title = "Save file",defaultextension = '.pickle',filetypes = (("pickle files","*.pickle"),("all files","*.*")))
        self.object_file_path = self.surface.filename.name
        filehandler = open(self.object_file_path, 'wb') 
        pickle.dump(self.addressbook.person_list, filehandler)
        self.title_name(self.object_file_path)
        filehandler.close()
        self.main()
    #Hier wird das Objekt/Adressbuch als pickle Datei gespeichert oder die Datei wird aktualisiert
    def object_save(self):
        try:
            filehandler = open(self.object_file_path, 'wb') 
            pickle.dump(self.addressbook.person_list, filehandler)
            self.title_name(self.object_file_path)
            filehandler.close()
            self.main()
        except TypeError:
            self.object_save_as()
    #Hier wird ein schon exentiertes Objekt/Adressbuch geöffnet
    def object_open(self):
        self.surface.filename =  filedialog.askopenfilename(title = "Select file",filetypes = (("pickle files","*.pickle"),("all files","*.*")))
        self.object_file_path = self.surface.filename
        read_file = open(self.object_file_path, 'rb')
        self.addressbook.person_list = pickle.load(read_file)
        self.title_name(self.surface.filename)
        self.main()
    #Hier wird ein neues Objekt/Adressbuch erstellt
    def object_new(self):
        self.object_file_path = None
        self.title = ''
        self.addressbook.person_list = []
        #self.label_info_person.config(text="")
        self.listbox_active()
        #self.index = None
        #self.inhalt = None
        self.main()
    #Hier wird der Titel vom Fenster bearbeit, also umgändert in den Namen der Datei/Adressbuch
    def title_name(self,string):
        end = string.find(".pickle")
        start = string.rfind("/")
        self.title = string[start+1:end]

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
        #adress, city, state ,plz, phone werden bearbeitet
        self.address = adr
        self.city = city
        self.state = state
        self.plz = plz
        self.phone = phone

    def person_print(self):
        #alle informationen der Person werden ausgegeben
        print(self.firstName)
        print(self.lastName)
        print(self.address)
        print(self.city)
        print(self.state)
        print(self.plz)
        print(self.phone)

class Addressbook:
    def __init__(self):
        self.person_list = []#eine Liste wird erstellt
    def create_person(self,fname,lname,adr,city,state,plz,phone):
        #die neu erstellte Person wird zur Liste hinzugefügt
        self.person_list.append(Person(fname,lname,adr,city,state,plz,phone))
    def print_person(self):
        #die ganze Liste wird ausgegeben
        for i in self.person_list:
            i.person_print()
            print('')
    def sort_plz(self):
        #die Liste wird nach der PLZ sortiert
        self.person_list.sort(key=lambda person: person.plz)
    def sort_name(self):
        #die Liste wird nach dem Nachnamen sortiert
        self.person_list.sort(key=lambda person: person.lastName)
    def person_del(self,pos):
        #eine Person wird aus der Liste gelöscht
        del self.person_list[pos]

surface = Tk()#es wird ein Fenster erstellt

Addressbook = GUI(surface)#ein Objekt wird erstellt
Addressbook.menubar()#es wird das Menubar aufgerufen
