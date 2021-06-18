#add tkinter basic template
from tkinter import *
root=Tk()
root.title("Driving License")
root.geometry("500x600")


root.configure(background="red")
canvas = Canvas(root, width=300, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="red")
canvas.create_rectangle(0, 345, 300, 400, fill="red")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Driving License")
label_id_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="  ID : ")
label_name_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="  Name : ")
label_birth_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="  Date Of Birth : ")
label_pin_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="  Pin no. : ")
label_add_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="  Address : ")
label_drive_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="  Authorisation To Drive The Following Vehicles : ")

#add label for name
label_ID=Label(root)
#add label for grade
label_Name=Label(root)
#add label for Subjects
label_Birth=Label(root)
label_Pin=Label(root)
label_Add=Label(root)
label_Drive=Label(root)
#add function
def mycarddetail():
    name="Krishna KVS Maddali"
    print(name)
    id = 1602994629
    print(id)
    dob = "October 11, 2010"
    Pin = 15273
    add = "2 Thimbleberry Court Waterveiliet"
    d = "Two Four"
    print(dob)
    label_ID["text"]=id
    label_Name["text"]=name
    label_Birth["text"]=dob
    label_Pin["text"]= Pin
    label_Add["text"]= add
    label_Drive["text"]= d
#add button
button1 = Button(root,text="Show My Id Card",command=mycarddetail)
button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_Name)
label_birth_window = canvas.create_window(90, 205, anchor=CENTER, window=label_Birth)
label_id_window = canvas.create_window(155, 252, anchor=CENTER, window=label_ID)

label_pin_window = canvas.create_window(120, 165, anchor=CENTER, window=label_Pin)
label_add_window = canvas.create_window(90, 205, anchor=CENTER, window=label_Add)
label_drive_window = canvas.create_window(155, 252, anchor=CENTER, window=label_Drive)
canvas.pack()

#tkinter basic template end statement

root.mainloop()