from studentManagementFunctions import *

def main() -> None:
    
    #create main window
    root = Tk()
    root.title("Student Management System")
    root.geometry("800x510")

    #read file
    openAndRead()

    displayData(root) #display the table of student information 

    #root buttons
    settingsButton = Button(root,text="Settings",command=openSettingsWindow)
    newStudentButton = Button(root, text = "Create new student",bg="blue", command=openNewStudentWindow)
    deleteStudentButton = Button(root,text="Delete student", bg="red", command=openDeleteStudentWindow)
    closeProgramButton = Button(root,text="close", command=closeProgram)

    #grid root buttons
    settingsButton.grid(row=0,column=0)
    newStudentButton.grid(row=0,column=1, columnspan=2)
    deleteStudentButton.grid(row=0,column=3,columnspan=2)
    closeProgramButton.grid(row=0,column=9)

    #create table heading
    headings = ["First Name \n", "Last Name \n", "ID \n", 
                "Period 1 \nGrade", "Period 2 \nGrade", "Period 3 \nGrade",
                "Period 4 \nGrade","Period 5 \nGrade","Period 6 \nGrade"]
    columnNumber = 0
    for heading in headings:
        Label(root,text=heading,padx=10).grid(row=1,column=columnNumber)
        columnNumber += 1

    root.mainloop()
    
if __name__ == "__main__":
    main()