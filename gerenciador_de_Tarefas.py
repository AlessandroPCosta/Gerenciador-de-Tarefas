
def adicionar_tarefas(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, 'completada': False}
    tarefas.append(tarefa)
    print(f'Tarefa {nome_tarefa} foi adiconada com sucesso!')  
    return

def ver_tarefas(tarefas,):
    print('\nLista de Tarefas:')
    for indice, tarefa in enumerate(tarefas, start=1):
        status = '✓' if tarefa ['completada'] else ''
        nome_tarefa = tarefa ["tarefa"]
        print(f'{indice}, [{status}] {nome_tarefa}')
    return

def atualizar_nome_terefa(tarefas, indice_tarefa, novo_nome_terefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]['tarefa'] = novo_nome_terefa
        print(f'Tarefa {indice_tarefa} atualiazada para {novo_nome_terefa}')
    else:
        print('Indice de tarefa invalido.')
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]['completada'] = True
    else:
        print('Indice de tarefa invalido.')
    return

def deletar_tarefas_completadas(tarefas):
    print('Tarefas completadas foram deletadas')
    for tarefa in tarefas:
        if tarefa['completada'] == True:
            tarefa.remove(tarefa)
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
        adicionar_tarefas(tarefas, nome_tarefa)

    elif escolha == '2':
        ver_tarefas(tarefas)

    elif escolha == '3':
        ver_tarefas(tarefas)
        indice_tarefa = input('Qual tarefa deseja atualizar: ')
        novo_nome = input('Digite a atualização da tarefa: ')
        atualizar_nome_terefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == '4':
        ver_tarefas(tarefas)
        indice_tarefa = input('Qual tarefa deseja marcar como completa: ')
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == '5':
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == '6':
        break
print('Programa finalizado')