def createList():
    listName = []
    return listName

def add_task(newTask,listName=None):
    if listName is None:
        listName = []
        listName.append(newTask)
    return listName.append(newTask)
    
def list_tasks(allTasks):
    if not allTasks:
        print('A lista está vazia!!!!\n')
        return
    else:
        print("########## TAREFAS DE HOJE!!! ########## ")
        for position,task in enumerate(allTasks,start=1):
            print(f'Tarefa {position}: {task}')
        print()
        return allTasks


def valida_op(op):
    try:
        op = int(op) if int(op) else float(op)
        return op
    except ValueError as erro:
        try:
            op = float(op)
        except:
            return f'{op} Não é numero'
    


if __name__== '__main__':
    my_tasks = createList()
    my_tasks2 = createList()
    add_task('Tarefa 1',my_tasks)
    add_task('Tarefa 2',my_tasks)
    add_task('Tarefa 3',my_tasks)
    add_task('Tarefa 4',my_tasks)
    list_tasks(my_tasks)
    print(my_tasks2)

    print(type(valida_op(20.5504)))