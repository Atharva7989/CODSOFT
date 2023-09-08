# To do list
l=[]
idx=1
while True:

    y=1
    print()
    print("To Do List ")
    print()
    print()
    print("1.ADD TASK")
    print()
    print("2.Delete Task")
    print()
    print("3.Update Task")
    print()
    print("4.Display")
    print()
    print("5.Exit")
    print()
    c=1
    choice=int(input("Enter choice : "))
    print()
    match choice:
        
        
          case 1:
             print("Enter Task")
             print()
             #n=int(input())
             #for i in range (0,n):
             sum=input()
             l.append(sum)
        

             
          case 2:
             """print("Delete Task")
             for i in l:
                 print("Task",c,":",i,end="")
                 print()
                 c+=1
             index=int(input())
             print("Enter no of Task to remove")
             print()
             z=index-1
             
             print(l.pop(z))
             print("Task Deleted Sucessfully")
             print()
             print(l)
             print()"""

             print("Delete Task")
             for idx, task in enumerate(l[1:], start=1):
                 
                 print("Task", idx, ":", task)
             index = int(input("Enter no of Task to remove: "))
             if 1 <= index < len(l):
                 
                 removed_task = l.pop(index)
                 print("Task", index, "(", removed_task, ") Deleted Successfully")
             else:
                 print("Invalid task index")
      
          case 3:
              print("Enter task to update")
              index1=int(input())
              z=index1-1
              n=input()
              l[z]=n
              print(l)
              print()

          case 4:
              print("Total Task")
              print()
              w=1
              for i in l:
                  print("Task : ",w,"",i,end=" ")
                  w=w+1
                  print()

        
          case 5:
              print("Exited")
              break

          case _:

              print("Invalid Choice")
             
                 
                   
                 
                 
               
                     

             

             
        
    
