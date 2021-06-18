#add tkinter basic template
from tkinter import *
root=Tk()
root.title("Driving License")
root.geometry("900x700")


root.configure(background="red")
canvas = Canvas(root, width=500, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 500, 55, fill="teal")
canvas.create_rectangle(0, 345, 500, 400, fill="teal")

label_heading = canvas.create_text(250, 90, font=('Times', '24', 'bold italic'),anchor=CENTER, text="Driving License")
label_id_tag = canvas.create_text(20, 125, font=('Times', '16', 'bold'), anchor=W, text="  ID : ")
label_name_tag = canvas.create_text(20, 145, font=('Times', '16', 'bold'),anchor=W, text="  Name : ")
label_birth_tag = canvas.create_text(20, 165, font=('Times', '16', 'bold'),anchor=W, text="  Date Of Birth : ")
label_pin_tag = canvas.create_text(20, 185, font=('Times', '16', 'bold'),anchor=W, text="  Pin no. : ")
label_add_tag = canvas.create_text(20, 205, font=('Times', '16', 'bold'),anchor=W, text="  Address : ")
label_drive_tag = canvas.create_text(20, 225, font=('Times', '16', 'bold'),anchor=W,  text="  Authorisation To Drive The Following Vehicles : ")

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
    print(type(name))
    id = 1602994629
    print(type(id))
    dob = "November 10, 2011"
    Pin = 15273
    add = "2 Thimbleberry Court Waterveiliet"
    d = "Two Four"
    print(type(dob))
    label_ID["text"]=id
    label_Name["text"]=name
    label_Birth["text"]=dob
    label_Pin["text"]= Pin
    label_Add["text"]= add
    label_Drive["text"]= d
#add button
button1 = Button(root,text="Show My Id Card",command=mycarddetail)
button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(250, 330, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(200, 125, anchor=W, window=label_ID)
label_name_window = canvas.create_window(200, 145, anchor=W, window=label_Name)
label_birth_window = canvas.create_window(200,165 , anchor=W, window=label_Birth)


label_pin_window = canvas.create_window(200, 185, anchor=W, window=label_Pin)
label_add_window = canvas.create_window(200, 205, anchor=W, window=label_Add)
label_drive_window = canvas.create_window(370, 225, anchor=W, window=label_Drive)
canvas.pack()

#tkinter basic template end statement

root.mainloop()












