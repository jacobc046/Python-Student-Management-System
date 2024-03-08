from tkinter import *
import string

#read data from file
def openAndRead() -> None:
    global file, appData

    try: #if the file does not exist yet, create it
        file = open("studentManagementSystemAppData.txt", "x")
        file.write("8\nFalse\nF\n" + "-\n"*7)
        file.seek(0)
        appData = file.readlines()
        file.close()
    except:
        pass
    finally: #set file mode to read and write, convert lines to list
        file = open("studentManagementSystemAppData.txt", "r+")
        appData = file.readlines()
        appData = [line.strip() for line in appData] #strip each line of the file
    return


#create and display the settings window
def openSettingsWindow() -> None:
    global maxStudentIdLengthIdx, studentIdAllowsLettersIdx, failingGradeIdx
    
    #define index in the file of which line data should be stored on
    maxStudentIdLengthIdx = 0
    studentIdAllowsLettersIdx = 1
    failingGradeIdx = 2
    
    openAndRead() #reread the file for updated settings

    #create settings window
    settingsWindow = Toplevel(height = 400,width=300)
    settingsWindow.title("Settings")

    #allow user to determine the max length of the studnet ID (defualt is 8)
    global maxStudentIdLength
    Label(settingsWindow, text="Max Student ID Length:").grid(row=0, columnspan=2)
    maxStudentIdLength = Entry(settingsWindow,width=2)
    maxStudentIdLength.grid(row=0, column=1)
    maxStudentIdLength.insert(0,appData[0].strip()) #display current value in entry box

    #allow user to determine if the studnet ID will allow letters (int only by default)
    global studentIdAllowsLetters
    studentIdAllowsLetters = StringVar()
    studentIdAllowsLettersLabel = Label(settingsWindow, text="Allow characters in student ID")
    studnetIdAllowsLettersTrue = Radiobutton(settingsWindow, text="True", padx=2,variable=studentIdAllowsLetters,value="True")
    studnetIdAllowsLettersFalse = Radiobutton(settingsWindow, text="False", padx=2,variable=studentIdAllowsLetters,value="False")
    studentIdAllowsLettersLabel.grid(row=1)
    studnetIdAllowsLettersTrue.grid(row=1,column=1)
    studnetIdAllowsLettersFalse.grid(row=1,column=2)

    #allow user to set the letter of a failing grade between E or F (default is F)
    global failingGrade
    
    failingGrade = StringVar()
    failingGradeLabel = Label(settingsWindow,text="Failing grade letter:")
    failingGradeE = Radiobutton(settingsWindow, text="E",variable=failingGrade, value="E")
    failingGradeF = Radiobutton(settingsWindow,text="F",variable=failingGrade, value="F")
    failingGradeLabel.grid(row=2, column=0)
    failingGradeE.grid(row=2,column=1)
    failingGradeF.grid(row=2,column=2)

    #display currently selected choice on the buttons
    
    studentIdAllowsLetters.set(appData[studentIdAllowsLettersIdx].strip())
    failingGrade.set(appData[failingGradeIdx].strip())

    #modify the appData list with the updated values
    appData[maxStudentIdLengthIdx] = maxStudentIdLength
    appData[studentIdAllowsLettersIdx] = studentIdAllowsLetters
    appData[failingGradeIdx] = failingGrade

    #write the settings to the file
    def saveSettings() -> None:
        file = open("studentManagementSystemAppData.txt","w")

        #for each line in the range of the settings indexes, write the settings to the file
        for line in appData:
            try:
                file.write(line.get() + "\n")
            except:
                file.write(line+"\n")
        
        #update the file and close the window
        file.close()
        settingsWindow.destroy()

        return
    
    #window exitting buttons
    saveButton = Button(settingsWindow,text="Save",command=saveSettings)
    saveButton.grid(row=3,column=2)
    cancelButton = Button(settingsWindow,text="Cancel", command=settingsWindow.destroy)
    cancelButton.grid(row=3,column=0)

    return


#create and display the student creation window
def openNewStudentWindow() -> None:

    openAndRead() #reread the file for any changes

    #create window
    newStudentWindow = Toplevel(height=600, width=400)
    newStudentWindow.title("Enter student data")

    #create 4 new items in the line list to be replaced by user entries later
    appData.append("\n"*4)

    #create labels for the entry boxes
    Label(newStudentWindow,text="First name").grid(row=0, column=0)
    Label(newStudentWindow,text="Last name").grid(row=1,column=0)
    Label(newStudentWindow,text="ID").grid(row=2,column=0)

    #create entry boxes and lay them out in the grid
    firstName = Entry(newStudentWindow,width=20)
    lastName = Entry(newStudentWindow,width=20)
    id = Entry(newStudentWindow, width=appData[maxStudentIdLengthIdx])
    Label(newStudentWindow,text="Grades").grid(row=3,column=0)
    firstName.grid(row=0,column=1)
    lastName.grid(row=1,column=1)
    id.grid(row=2,column=1)
 
    #create 6 string variables for the grades
    period1Grade = StringVar()
    period2Grade = StringVar()
    period3Grade = StringVar()
    period4Grade = StringVar()
    period5Grade = StringVar()
    period6Grade = StringVar()

    #list of options for the drop down menus of the grade boxes
    #with the failing grade based on user settings
    failingGrade = appData[failingGradeIdx]
    gradeOptions = ["A+","A","A-",
                    "B+","B","B-",
                    "C+","C","C-",
                    "D+","D","D-",
                    str(failingGrade),
                    "None"]

    #create six drop down menu objects and set them in the grid
    period1GradeMenu = OptionMenu(newStudentWindow, period1Grade,*gradeOptions)
    period2GradeMenu = OptionMenu(newStudentWindow, period2Grade,*gradeOptions)
    period3GradeMenu = OptionMenu(newStudentWindow, period3Grade,*gradeOptions)
    period4GradeMenu = OptionMenu(newStudentWindow, period4Grade,*gradeOptions)
    period5GradeMenu = OptionMenu(newStudentWindow, period5Grade,*gradeOptions)
    period6GradeMenu = OptionMenu(newStudentWindow, period6Grade,*gradeOptions)
    period1GradeMenu.grid(row=4, column=0)
    period2GradeMenu.grid(row=4,column=1)
    period3GradeMenu.grid(row=4,column=2)
    period4GradeMenu.grid(row=5,column=0)
    period5GradeMenu.grid(row=5,column=1)
    period6GradeMenu.grid(row=5,column=2)

    grades = [period1Grade,period2Grade,period3Grade,period4Grade,period5Grade,period6Grade]

    #set each default drop down option to "None"
    for grade in grades:
        grade.set("None")

    #create label object for error message
    global errorMessage
    errorMessage = Label(newStudentWindow)
    errorMessage.grid(row=6,column=1)

    #write the new student data to the file
    def writeStudent(first, last, id, grades):

        #convert the entries in the boxes to strings
        firstName = first.get()
        lastName = last.get()
        id = id.get()
        grades = ", ".join([i.get() for i in grades])

        ##check for unfilled entries or id related errors
        #no first name given
        if firstName == "": 
            errorMessage.config(text="Please enter a first name",bg="red")
            return
        #no last name given
        elif lastName == "": 
            errorMessage.config(text="Please enter a last name",bg="red")
            return
        #no ID given
        elif id == "": 
            errorMessage.config(text="Please enter an ID number",bg="red")
            return
        #student ID already exists
        elif id in appData:
            errorMessage.config(text="ID already exists",bg="red")
            return
        elif appData[studentIdAllowsLettersIdx] == "False" and any([(letter in string.ascii_letters) for letter in id]):
            errorMessage.config(text="Student ID does not allow letters",bg="red")
            return
        #length of student ID exceeds the max length allowed
        elif len(id) > int(appData[maxStudentIdLengthIdx]): 
            errorMessage.config(text=f"ID exceeds {appData[maxStudentIdLengthIdx]} characters",bg="red")
            return

        #write student informatin to end of file
        for i in [id, firstName, lastName, grades]: file.write(i + "\n")

        #close file and window, update the data table in the main window
        file.close()
        newStudentWindow.destroy()
        displayData()

        return

    #create cancel and create student buttons
    Button(newStudentWindow, text="Create", command=lambda: writeStudent(firstName,lastName,id,grades)).grid(row=6,column=3)
    Button(newStudentWindow, text="Cancel", command=newStudentWindow.destroy).grid(row=6, column=0)

    return


#open window to delete student data
def openDeleteStudentWindow() -> None:
    openAndRead() #read the file for any updates

    #create the window
    deleteStudentWindow = Toplevel(height=300, width=400)
    deleteStudentWindow.title("Delete Student")

    #create prompt for user
    Label(deleteStudentWindow,text="Enter the ID of the student to delete:").grid(row=0)

    #create entry box
    maxStudentIdLength = appData[maxStudentIdLengthIdx]
    id = Entry(deleteStudentWindow, width=maxStudentIdLength)
    id.grid(row=1)

    #remove the student data from the file
    def deleteStudent(id:str) -> None:
        global appData

        ##check for errors in ID the user entered and display an error message
        #no id given
        if id == "": 
            Label(deleteStudentWindow,text="Please enter an ID",bg="red").grid(row=3)
            return
        #ID DNE
        elif id not in [line.strip() for line in appData]: 
            Label(deleteStudentWindow,text="Student does not exist",bg="red").grid(row=3)
            return

        #find the index of the line that the deleted student's ID is stored on
        lineIndex = appData.index(id)

        #move to the beginning of the file and delete everything
        file.seek(0)
        file.truncate()

        #rewrite all data except for the 4 lines of data associated with the deleted student
        for i in range(len(appData)):
            if i not in range(lineIndex,lineIndex+4):
                file.write(appData[i].strip() + "\n")

        #close the window and file, update the data table in the main window
        deleteStudentWindow.destroy()
        file.close()
        displayData()

        return
        
    #create cancel and delete student buttons
    Button(deleteStudentWindow, text = "Delete", command=lambda:deleteStudent(id.get())).grid(row=2, column=1)
    Button(deleteStudentWindow,text="Cancel",command=deleteStudentWindow.destroy).grid(row=2,column=0)

    return


#create/update the data table displayed in the main window
def displayData(root) -> None:
    global entries
    global appData

    #read the file for changes
    openAndRead()

    #destroy all existing displayed data 
    try:
        #delete each label object in the list of label objects being displayed
        for label in entries: label.destroy()
    except:
        pass
    finally:
        #create an empty list to store all data label objects
        entries = []
        r = 2

        #create label objects for each student in order of id, first, last, and grades
        for index in range(10,len(appData),4):
            id = appData[index]
            firstName = appData[index+1]
            lastName = appData[index+2]
            grades = appData[index+3]

            firstNameLabel = Label(root,text=firstName)
            lastNameLabel = Label(root,text=lastName)
            idLabel = Label(root,text=id)

            firstNameLabel.grid(row=r,column=0)
            lastNameLabel.grid(row=r,column=1)
            idLabel.grid(row=r,column=2)

            #add the label object to the label objects list 
            for label in [firstNameLabel,lastNameLabel,idLabel]: entries.append(label) 

            #convert string of grades in file to a list and store each grade as a separate label
            col = 3
            for grade in grades.split(","):
                gradeLabel = Label(root,text=grade)

                gradeLabel.grid(row=r,column=col)

                #add the grade label to the label objects list
                entries.append(gradeLabel)

                col += 1

            r+= 1

    return


#close the main window and the file
def closeProgram() -> None:
    file.close()
    exit()