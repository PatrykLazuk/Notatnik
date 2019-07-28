import os
import datetime

# ustalenie obecnej daty i ścieżki do pliku
today = datetime.date.today()
diaryEntriesFolder = "Entries"
portableDir = os.getcwd()
folderDirectory = os.path.join(portableDir, diaryEntriesFolder)
try:
    os.mkdir(diaryEntriesFolder)
    print("Directory ", diaryEntriesFolder, " Created ")
except:
    print("Main folder located, proceeding.")

print("Welcome to the Python Diary.")

while True:

    print('\nMAIN MENU\n')
    print('1. Open an existing entry')
    print('2. Create a new entry')
    print('3. Edit an existing entry')
    print('4. Delete an entry')
    print('5. Exit the program')
    menuChoice = input('\nWhat do you wish to do?: ')
    if menuChoice == '1':

        while True:
            # wypisanie wszystkich plików w folderze Entries
            print('\nEntries: ')
            content = os.listdir(folderDirectory)
            entriesCounter = range(len(folderDirectory))
            contentDict = {key: value for key, value in zip(entriesCounter, content)}
            for entry in contentDict:
                print(entry, ":", contentDict[entry])
            if len(content) == 0:
                print('There is no files in Entries dir.\nCreate new file!')
                input('Press enter to continue')
                break
            else:
                openIndicator = True

            while openIndicator:
                try:
                    openChoice = input('\nPlease enter a number of a file to open: ')
                    fileToOpen = contentDict[int(openChoice)]
                    print(fileToOpen)
                    with open(os.path.join(folderDirectory, fileToOpen), "r") as file:
                        entryText = file.read()
                        print("\n"+entryText+"\n")
                        openIndicator = False
                except:
                    print("Wrong entry number. Enter correct entry number")
                    continue

            openBack = input('Open another entry? [y/n]: ')
            if openBack == "y":
                openIndicator = True
                continue
            elif openBack == "n":
                break
            else:
                print('There is no such option. Back to menu!')
                break
    elif menuChoice == '2':
        #wypisanie wszystkich plików w folderze Entries
        print('\nEntries: ')
        content = os.listdir(folderDirectory)
        entriesCounter = range(len(folderDirectory))
        contentDict = {key: value for key, value in zip(entriesCounter, content)}
        for entry in contentDict:
            print(entry, ":", contentDict[entry])
        #nadanie wartosci kluczowi Create
        createIndicator = True
        while createIndicator:
            while True:
                name = input("Please enter a name for new Diary file: ")
                fileName = str(today) + " " + name + ".txt"
                newFileDir = os.path.join(portableDir, diaryEntriesFolder, fileName)

                if name == "":
                    print("The new file needs a name.")
                    break
                elif os.path.exists(newFileDir):
                    print("File with name", name, "already exists. Please enter unique name")
                    break
                else:
                    #Stworzenie nowego pliku i wpisanie treści
                    with open(newFileDir, "w") as file:
                        print("Please enter a new note:\n")
                        text = input()
                        file.write(text)

                        print("Note saved")
                        createIndicator = False
                        break

    elif menuChoice == '3':

        while True:
            # wypisanie wszystkich plików w folderze Entries
            print('\nEntries: ')
            content = os.listdir(folderDirectory)
            entriesCounter = range(len(folderDirectory))
            contentDict = {key: value for key, value in zip(entriesCounter, content)}
            for entry in contentDict:
                print(entry, ":", contentDict[entry])
            if len(content) == 0:
                print('There is no files in Entries dir.\nCreate new file!')
                input('Press enter to continue')
                break
            else:
                editIndicator = True

            while editIndicator:
                try:
                    editChoice = input('\nPlease enter a number of a file to edit: ')
                    fileToOpen = contentDict[int(editChoice)]
                    print(fileToOpen)
                    with open(os.path.join(folderDirectory,fileToOpen), "r") as file:
                        entryText = file.read()
                        print("\n"+entryText+"\n")
                    with open(os.path.join(folderDirectory, fileToOpen), "a") as file:
                        print("Please enter an addition to the note",fileToOpen,":\n")
                        appendText = input()
                        file.write("\n"+appendText)
                        editIndicator = False
                except:
                    print("Wrong entry number. Enter correct entry number")
                    continue

            editBack = input('Edit another entry? [y/n]: ')
            if editBack == "y":
                editIndicator = True
                continue
            elif editBack == "n":
                break
            else:
                print('There is no such option. Back to menu!')
                break

    elif menuChoice == '4':
        while True:
            # wypisanie wszystkich plików w folderze Entries
            print('\nEntries: ')
            content = os.listdir(folderDirectory)
            entriesCounter = range(len(folderDirectory))
            contentDict = {key: value for key, value in zip(entriesCounter, content)}
            for entry in contentDict:
                print(entry, ":", contentDict[entry])
            if len(content) == 0:
                print('There is no files in Entries dir.\nCreate new file!')
                input('Press enter to continue')
                break
            else:
                deleteIndicator = True

            while deleteIndicator:
                try:
                    deleteChoice = input('\nPlease enter a number of a file to delete: ')
                    fileToDelete = contentDict[int(deleteChoice)]
                    fileToDeletePath = os.path.join(folderDirectory, fileToDelete)
                    print(fileToDeletePath)
                    os.remove(fileToDeletePath)
                    print('\nFile',fileToDelete,'deleted!')
                    input('\nPress enter to continue.')
                    deleteIndicator = False
                except:
                    print("Wrong entry number. Enter correct entry number")
                    continue

    elif menuChoice == '5':
        print('Thank you for using Python Diary.\nBye!')
        exit()
    else:
        print('Please select correct number')
        continue
