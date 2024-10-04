from tkinter import * 
root=Tk()
c_width=500
c_height=500
canva=Canvas(root,width=c_width,height=c_height)

Y=int(c_height/2)
line = canva.create_line(0,Y,500,Y,fill="green")
coord1=10,50,240,210
oval=canva.create_oval(10,50,200,20,fill="red")
arc=canva.create_arc(coord1,start=0,extent=300,fill="blue")
                    
canva.pack()
root.mainloop()