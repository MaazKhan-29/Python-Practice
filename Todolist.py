opr=0
todo={}

def add():
    while True:
        
        task=(input("Enter the task or Say done to complete: "))
        
        if task=="Done":
            break
        
        task_detail=(input("Enter the task detail: "))
        
        todo[task]=task_detail
        
    
def view():
    for i in todo:
        print(f"{i}:{todo[i]}")
        
def delete():
    
    x=input("Enter the task to be deleted: ")
    
    if x in todo:
        todo.pop(x)
    else:
        print("task not found: ") 
        
    view()       

while opr!=9:
    
    print("Enter 1 for add")
    print("Enter 2 for view")
    print("Enter 3 for delete")
    print("Enter 9 for exit")

    opr=int(input("Enter the number to perform operation: "))

    if opr==1:
        add()
    
    elif opr==2:
        view()
        
    elif opr==3:
        delete()   
        
    elif opr==9:
        break   
            
    
    
             
        
    
    
    
