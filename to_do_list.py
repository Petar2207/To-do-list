zavrsna=0
listt=list()
while zavrsna!="STOP":
    x = input("Choose a number:\n1) ADD task to 'To do list'\n2) Delete task from 'To do list'\n3) View all tasks in 'To do list'\n")
    try:
        x = int(x)
    except ValueError:
        print("Please enter a valid number.")
        continue
    max_length = max((len(task) for task in listt), default=0)
    if x>3:
        print("Chose number in range 1 to 3")
    if 0 < x < 4:
        if x==1:
            y=str(input("Enter task that you want to add"))
            codiraniy=y.upper().replace(" ","")
            if any(codiraniy == task.upper().replace(" ", "") for task in listt):
                print("You already have that task.")
                r=input("Pres enter if you want to add it to the list if not write'NO'")
                if r=="":
                    listt.append(y)
                    print("Added to list. List:",listt)
                else:
                    print("Task not added.")
            else:
                listt.append(y)
                print("Added to list. List:",listt)
        if x==2:
            if not listt:
                print("List is empthy")
                break
            else:
                vracanje=None
                change=str(input("Write which task you want to delete"))
                while vracanje is None:
                    change_cod=change.upper().replace(" ","")
                    while len(change_cod)>max_length:
                        change=input("Please write only task")
                        change_cod=change.upper().replace(" ","")
                    listindex=0
                    for task in listt:
                        if change_cod != task.upper().replace(" ", ""):
                            listindex=listindex+1
                        if change_cod == task.upper().replace(" ", ""):
                            listt.pop(listindex)
                            print(change, "deleted")
                            print(listt)
                            break

                    print("I cant find that item in list")
                    change=input("Try again or write 'CANCEL' to go back on start of program")
                    change_cod = change.upper().replace(" ", "")
                    if change_cod=="CANCEL":
                        break
        if x==3:
            print(listt)
    while zavrsna!="":
        zavrsna=input("If you want to leave program and delete tasks enter:'STOP'\nIf you want to continue just press enter")
        if zavrsna=="STOP":
            print(listt,"Thank you for participating")
            break
        elif zavrsna!="":
            print("Please try again")

