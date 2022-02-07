"""
5E D&D NPC Creator

Quickly create NPC's or Assign NPC stats 

Python Version 3.9.9
Coded in Sublime Text Editor 
"""

from tkinter import *
import time
import backend

###########
#Functions#
###########


### Hiding and Showing the List Vs Abilities

def hide_widgit(item):
    # This will remove the widget
    item.grid_remove()

def show_widgit(item):
    # This will remove the widget
	item.grid()

#getting text from the text box (e14)

def retrieve_input():
	result = e14.get("1.0","end")
	return str(e14.get("1.0","end"))


###Calling functions from the backend

def get_selected_row(event):
	try:
		global selected_tuple
		index=list1.curselection()[0]
		selected_tuple=list1.get(index)
		
		hide_widgit(list1)
		show_widgit(e14)

		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])
		e4.delete(0,END)
		e4.insert(END,selected_tuple[4])
		e5.delete(0,END)
		e5.insert(END,selected_tuple[5])
		e6.delete(0,END)
		e6.insert(END,selected_tuple[6])
		e7.delete(0,END)
		e7.insert(END,selected_tuple[7])
		e8.delete(0,END)
		e8.insert(END,selected_tuple[8])
		e9.delete(0,END)
		e9.insert(END,selected_tuple[9])
		e10.delete(0,END)
		e10.insert(END,selected_tuple[10])
		e11.delete(0,END)
		e11.insert(END,selected_tuple[11])
		e12.delete(0,END)
		e12.insert(END,selected_tuple[12])
		e13.delete(0,END)
		e13.insert(END,selected_tuple[13])
		e14.delete(1.0,END)
		e14.insert(1.0,selected_tuple[14])

	except IndexError:
		pass
		


def view_command():
	hide_widgit(e14)
	show_widgit(list1)
	list1.delete(0,END)
	for row in backend.view():
		list1.insert(END,row)


def search_command():
	list1.delete(0,END)
	for row in backend.search(name_text.get(),hp_text.get(),cr_text.get(),ac_text.get()):
		list1.insert(END,row)


def add_command():
	#blurb_text=retrieve_input()
	backend.insert(name_text.get(),hp_text.get(),info_text.get(),ac_text.get(),stre_text.get(),dex_text.get(),con_text.get(),inte_text.get(),wis_text.get(),cha_text.get(),saves_text.get(),cr_text.get(),skills_text.get(),retrieve_input())
	
	#list1.delete(0,END)

	hide_widgit(e14)
	show_widgit(list1)

	list1.delete(0,END)

	#list1.insert(END,name_text.get(),'the',info_text.get(),"Has Been Added to Database")

	time.sleep(1)
	view_command()

def delete_command():
	backend.delete(selected_tuple[0])
	time.sleep(1)
	list1.delete(0,END)
	view_command()




def update_command():
	backend.update(selected_tuple[0],name_text.get(),hp_text.get(),info_text.get(),ac_text.get(),stre_text.get(),dex_text.get(),con_text.get(),inte_text.get(),wis_text.get(),cha_text.get(),saves_text.get(),cr_text.get(),skills_text.get(),retrieve_input())



############################
#Layout and Button Controls#
############################

window = Tk()

window.wm_title("NPC Tracker")

#Top Information

l1=Label(window,text="Name",width=5)
l1.grid(row=0,column=0)

l2=Label(window,text="HP",width=5)
l2.grid(row=0,column=4)

l3=Label(window,text="Info")
l3.grid(row=1,column=0)

l4=Label(window,text="AC",width=5)
l4.grid(row=1,column=4)

#Stats

l5=Label(window,text="Str",width=5)
l5.grid(row=2,column=0)

l6=Label(window,text="Dex",width=5)
l6.grid(row=2,column=1)

l7=Label(window,text="Con",width=5)
l7.grid(row=2,column=2)

l8=Label(window,text="Int",width=5)
l8.grid(row=2,column=3)

l9=Label(window,text="Wis",width=5)
l9.grid(row=2,column=4)

l10=Label(window,text="Cha",width=5)
l10.grid(row=2,column=5)

l11=Label(window,text="Saves")
l11.grid(row=4,column=0)

l12=Label(window,text="C/R",width=5)
l12.grid(row=4,column=4)

l13=Label(window,text="Skills")
l13.grid(row=5,column=0)

l14=Label(window,text="Actions // Reactions // Spells //Equipment")
l14.grid(row=6,column=0,columnspan=5)

#Entries

name_text=StringVar()
e1=Entry(window,textvariable=name_text,width=30)
e1.grid(row=0,column=1,columnspan=3)

hp_text=StringVar()
e2=Entry(window,textvariable=hp_text,width=6)
e2.grid(row=0,column=5)

info_text=StringVar()
e3=Entry(window,textvariable=info_text,width=30)
e3.grid(row=1,column=1,columnspan=3)

ac_text=StringVar()
e4=Entry(window,textvariable=ac_text,width=6)
e4.grid(row=1,column=5)

stre_text=StringVar()
e5=Entry(window,textvariable=stre_text,width=6)
e5.grid(row=3,column=0)

dex_text=StringVar()
e6=Entry(window,textvariable=dex_text,width=6)
e6.grid(row=3,column=1)

con_text=StringVar()
e7=Entry(window,textvariable=con_text,width=6)
e7.grid(row=3,column=2)

inte_text=StringVar()
e8=Entry(window,textvariable=inte_text,width=6)
e8.grid(row=3,column=3)

wis_text=StringVar()
e9=Entry(window,textvariable=wis_text,width=6)
e9.grid(row=3,column=4)

cha_text=StringVar()
e10=Entry(window,textvariable=cha_text,width=6)
e10.grid(row=3,column=5)

saves_text=StringVar()
e11=Entry(window,textvariable=saves_text,width=30)
e11.grid(row=4,column=1,columnspan=3)

cr_text=StringVar()
e12=Entry(window,textvariable=cr_text,width=5)
e12.grid(row=4,column=5,columnspan=1)

skills_text=StringVar()
e13=Entry(window,textvariable=skills_text,width=48)
e13.grid(row=5,column=1,columnspan=5)

######################################
#List AND Ability Entry and Scrollbar#
######################################

#I am keeping these together since they technically overlap and only one should be visible
#at anytime depending on what the user is doing


###LIST

list1=Listbox(window,width=53,height=24)
list1.grid(row=7,column=0,rowspan=6,columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=7,column=5,rowspan=6, rows=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


###ENTRY

#blurb_text=e14.get('1.0','end')
e14=Text(window,width=53,height=24)
e14.grid(row=7,column=0,rowspan=6,columnspan=6)
#blurb_text=retrieve_input()


sb1=Scrollbar(window)
sb1.grid(row=7,column=5,rowspan=6, rows=7)

e14.configure(yscrollcommand=sb1.set)
sb1.configure(command=e14.yview)


########################################


#########
#Buttons#
#########

b1=Button(window,text="View all",width=8,command=view_command)
b1.grid(row=14,column=0)

b2=Button(window,text="Search entry",width=8,command=search_command)
b2.grid(row=14,column=1)

b3=Button(window,text="Add entry",width=8,command=add_command)
b3.grid(row=14,column=2)

b4=Button(window,text="Update",width=8,command=update_command)
b4.grid(row=14,column=3)

b5=Button(window,text="Delete",width=8,command=delete_command)
b5.grid(row=14,column=4)

b6=Button(window,text="Close",width=8,command=window.destroy)
b6.grid(row=14,column=5)


##############################
#Run view_command at start up#
##############################

view_command()

window.mainloop()

