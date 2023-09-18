tarefa = input("insira a sua tarefa: ")
arq = open('tarefas.txt', 'a', encoding='utf-8')
arq.write(f'{tarefa}\n')
arq.close()