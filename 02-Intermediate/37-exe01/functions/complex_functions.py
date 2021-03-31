import functions.basic_functions

confirm_options_yes = ('YES','yes','Y','y','Yes','YeS','YEs','yeS','yEs','yES')
confirm_options_no = ('NO','no','No','nO','N')

def desfazer(task,listName,listHistory):
    confirm = input(f'Certeza que deseja deletar a task "{task}"  ? (Y)es or (N)o: ')
    if confirm in confirm_options_yes:
        listName.pop()
        listHistory.append(task)
        return f'"{task}" apagado com sucesso!\n'
    elif confirm in confirm_options_no:
        return
    else:
        print('Nenhum opção válida!')

def refazer(task,listName,listHistory):
    confirm = input(f'Certeza que deseja refazer a task {task} ? (Y)es or (N)o: ')
    if confirm in confirm_options_yes:
            listName.append(task)
            listHistory.pop()
            return f'"{task}" refeita com sucesso!!!\n'
    elif confirm in confirm_options_no:
        return
    else:
        print('Nenhum opção válida!')


if __name__== '__main__':
    lista = [0,1,2,3,4,5]
    print(desfazer(lista))
