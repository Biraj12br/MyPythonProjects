'''----------------------TO-Do App----------------------------'''

#First Version using List

'''todo=[]
while True:
    b=input("Type add, edit, show, exit: ")

    match b:
        case 'add':
            c=input('Enter a number: ')
            todo.append(c)
            file = open("todo.txt", 'w')
            file.writelines(todo)
            file.close()
        case 'show' | 'display':
            print(f"Number of item are {len(todo)}")
            for i,j in enumerate(todo):
                print(f"{i+1} - {j.title()}")

        case 'edit' | "delete":
            n=int(input("Enter the number: "))
            m=n-1
            q=input("Enter new element: ")
            todo[m]=q
        case 'exit':
            break '''





