
import sys
from tkinter import *
from random import randint

class custom_canvas: #create canvas
    
    def __init__(self, width, height): #canvas constructor
        self.master = Tk()
        self.width = width
        self.height = height
       
    def create_reactangle(self,rect_list): #creating rectangles
        colours = ("#000000", "black")
        w = Canvas(self.master, width=self.width, height=self.height)
        w.pack()
        for values in rect_list:
            values=values.split(",")
            width,height=values[0],values[1]
            print(width,height)
            w.create_rectangle(0, 0, width, height, fill=colours[randint(0,1)])


        mainloop()
class Rectangle:
    def __init__(self, height, width,x=0,y=0): #rectangle constrctor
        self.width = width
        self.height = height
        self.x=x
        self.y=y
def pack(allRect,canvasSize):
    flag=0
    new_list=[]
    new_list2=[]

    for i in range(0,len(allRect)):
        for j in range(0,len(allRect)):
            if(allRect[i]!=allRect[j]):

                flag=1
        if flag==1:
            new_list2.append(Rectangle(20,20))

    print(len(new_list2))
    return new_list2
def main():
    path = sys.argv[1]
    with open(path, "r") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    lines2=[]
    for i in range(1,len(lines)):
        lines2.append(lines[i])
    lines=lines[0].split(",")
    width,height=lines[0],lines[1]
    c=custom_canvas(width,height)
    return_list=pack(lines2,lines[0])
    custom_canvas.create_reactangle(c,return_list)
if __name__ == "__main__":
    main()