import functions.basic_functions as bfunc
import functions.complex_functions as cfunc

mytasks = bfunc.createList()
taskHistory = bfunc.createList()

while True:
    print("1. Adicionar tarefa"
            "\n2. Listar Tarefas"
            "\n3. Defazer"
            "\n4. Refazer"
            "\n0. Sair")
    op = input("Digite qual opção deseja fazer: ")
    op = bfunc.valida_op(op)

    if op == 1:
        task = input('Digite a tarefa: ')
        bfunc.add_task(task,mytasks)
    elif op == 2:
        bfunc.list_tasks(mytasks)
    elif op == 3:
        if not mytasks:
            print('A lista está vazia! Nada para desfazer!!\n')
        else:
            undo = mytasks[-1]
            res = cfunc.desfazer(undo,mytasks,taskHistory)
            print(res)
    elif op == 4:
        if not mytasks:
            print('A lista está vazia! Nada para refazer!!\n')
        elif not taskHistory:
                print('Todas as tarefas foram refeitas. Nada para refazer!!\n')
        else:
            redo = taskHistory[-1]      
            res = cfunc.refazer(redo,mytasks,taskHistory)
            print(res)
    elif op == 0:
        print('Até a próxima!!!')
        print()
        break
    else:
        print('Você precisa digitar uma das opções acima!!!!')
        print(op)
        print(type(op))
        print()


    