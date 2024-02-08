class Tarefa:
    def __init__(self, nome, completa = False):
        self.nome =  nome
        self.completa = completa

    def adicionar_tarefas(tarefas, nome_tarefa):
        nova_tarefa = Tarefa(nome = nome_tarefa)
        tarefas.append(nova_tarefa)
        print(f'Tarefa {nome_tarefa} foi adiconada com sucesso!') 
        return

    def ver_tarefas(tarefas):
        print('\nLista de Tarefas:')
        for indice, tarefa, in enumerate(tarefas, start=1):
            status = '✓' if tarefa.completa == True else ''
            nome_tarefa = tarefa.nome
            print(f'{indice}, [{status}] {nome_tarefa}')
        return
    
    def atualizar_nome_terefa(tarefas, indice_tarefa, novo_nome_terefa):
        indice_tarefa_ajustado = int(indice_tarefa) - 1
        if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
            tarefas[indice_tarefa_ajustado] = Tarefa(nome= novo_nome_terefa, completa=False)
            print(f'Tarefa {indice_tarefa} atualiazada para {novo_nome_terefa}')
        else:
            print('Indice de tarefa invalido.')
        return
    
    def completar_tarefa(tarefas, indice_tarefa):
        indice_tarefa_ajustado = int(indice_tarefa) - 1
        if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
            tarefas[indice_tarefa_ajustado] = Tarefa(nome= nome_tarefa, completa=True)
        else:
            print('Indice de tarefa invalido.')
        return
    def deletar_tarefas_completadas(tarefas):
        print('Tarefas completadas foram deletadas')
        for indice,tarefa in enumerate(tarefas):
            if tarefa.completa == True:
                tarefas.pop(indice)
        return

tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar Tarefas completadas")
    print('6. Sair')

    escolha = input('Digite a sua escolha: ')

    if escolha == '1':
        nome_tarefa = input('Digite o nome da Tarefa que deseja adicionar: ')
        Tarefa.adicionar_tarefas(tarefas, nome_tarefa)

    elif escolha == '2':
        Tarefa.ver_tarefas(tarefas)

    elif escolha == '3':
        Tarefa.ver_tarefas(tarefas)
        indice_tarefa = input('Qual tarefa deseja atualizar: ')
        novo_nome = input('Digite a atualização da tarefa: ')
        Tarefa.atualizar_nome_terefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == '4':
        Tarefa.ver_tarefas(tarefas)
        indice_tarefa = input('Qual tarefa deseja marcar como completa: ')
        Tarefa.completar_tarefa(tarefas, indice_tarefa)
    elif escolha == '5':
        Tarefa.deletar_tarefas_completadas(tarefas)
        Tarefa.ver_tarefas(tarefas)
    elif escolha == '6':
        break
