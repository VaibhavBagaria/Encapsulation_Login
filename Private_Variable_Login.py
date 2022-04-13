from tkinter import*
from PIL import ImageTk, Image
root=Tk()
root.title("Encapsulation")
root.geometry("400x500")

l1=Label(root,text="Name: ")
l1.place(relx=0.3,rely=0.1,anchor=CENTER)
Name_Entry=Entry(root)
Name_Entry.place(relx=0.55,rely=0.1,anchor=CENTER)
Name_l=Label(root,fg="red")
Name_l.place(relx=0.45,rely=0.15,anchor=CENTER)

l2=Label(root,text="Password: ")
l2.place(relx=0.3,rely=0.3,anchor=CENTER)
Password_Entry=Entry(root)
Password_Entry.place(relx=0.55,rely=0.3,anchor=CENTER)
Password_l=Label(root,fg="red")
Password_l.place(relx=0.45,rely=0.35,anchor=CENTER)

l3=Label(root,text="Captcha: ")
l3.place(relx=0.3,rely=0.5,anchor=CENTER)
captcha_Entry=Entry(root)
captcha_Entry.place(relx=0.55,rely=0.5,anchor=CENTER)
captcha_l=Label(root,fg="red")
captcha_l.place(relx=0.45,rely=0.55,anchor=CENTER)

class userDB():
    def __init__(self):
        self.__username="Rohan"
        self.__password="rohan19"
        self.captcha="19R2009"
        
    def show_user(self):
        Name_l['text']="Name: "+self.__username
        Password_l['text']="Password: "+self.__password
        captcha_l['text']="Captcha: "+self.captcha
        
obj_user=userDB()

def add_user():
    global obj_user
    obj_user.__username=Name_Entry.get()
    obj_user.__password=Password_Entry.get()
    obj_user.captcha=captcha_Entry.get()
    print("Detail Updated")
    
btn1=Button(root,text="Update Login Detail",command=add_user)
btn1.place(relx=0.35,rely=0.7,anchor=CENTER)

btn2=Button(root,text="Show Profile",command=obj_user.show_user)
btn2.place(relx=0.65,rely=0.7,anchor=CENTER)

root.mainloop()