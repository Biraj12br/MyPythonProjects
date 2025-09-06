"""Third Version(Improvised version of 2nd Version)"""


'''while True:
    options=input("Type add, edit, show, exit: ")

    match options:
        case 'add':
            item=input('Enter an item: ') + "\n"
            file = open("todo.txt", 'r')
            todos = file.readlines()
            file.close()

            todos.append(item)

            file = open("todo.txt", 'w')
            file.writelines(todos)
            file.close()

        case 'show' | 'display':
            """file = open("todo.txt", 'r')
            todos = file.readlines()
            file.close()"""

            with open('todo.txt','r') as file:
                todos=file.readlines()

            #new_todos=[items.strip('\n') for items in todos]

            new_todos=[]

            for items in todos:
                new_items = items.strip('\n')
                new_todos.append(new_items)

            print(f"Number of item are {len(new_todos)}")
            for i,j in enumerate(new_todos):
                print(f"{i+1} - {j.title()}")

        case 'edit' | "delete":
            file = open("todo.txt", 'r')
            todos = file.readlines()
            file.close()
            n=int(input("Enter the number: "))
            m=n-1
            q=input("Enter new element: ")
            todos[m]=q
        case 'exit':
            break'''
