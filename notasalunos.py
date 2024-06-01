import os

dict_alunos = {}
dict_professores = {}
dict_disciplinas = {}
select = 0

# Verifica se o usuário deseja continuar utilizando a função atual
def continuar_funcao():
    while True:
        try:
            resposta = int(input('Deseja voltar ao menu principal?\n1 - Sim\n2 - Nao\n'))
            if resposta == 1 or resposta == 2:
                os.system('cls')
                return resposta
            else:
                raise TypeError
        except TypeError:
            print('[ERRO] Opção Inválida! Tente novamente. [ERRO]\n')

# Função para registrar novo aluno
def registrar_novo_aluno():
    novo_aluno = []

    while True:
        try:
            matricula = int(input('Digite a matricula do novo aluno: '))
            # Verifica se o aluno não já existe no dicionário, caso negativo, o registra
            if matricula in dict_alunos:
                print('Esse aluno já está registrado!')
            else:
                novo_aluno.append(input('Digite o nome do aluno: '))
                novo_aluno.append(int(input('Digite a idade do aluno: ')))
                dict_alunos[matricula] = novo_aluno
                print('Aluno cadastrado com sucesso!\n')
                print(f'Matricula: {matricula}, nome: {dict_alunos[matricula][0]}, idade: {dict_alunos[matricula][1]}\n')
        except ValueError:
            print('A matricula deve ser um número inteiro!\n')
        finally:
            resposta = continuar_funcao()
            if resposta == 1:
                break

def registrar_novo_professor():
    novo_professor = []

    while True:
        try:
            matricula = int(input('Digite a matricula do professor: '))
            if matricula in dict_professores:
                print('Esse professor já está registrado')
            else:
                novo_professor.append(input('Digite o nome do professor: '))
                novo_professor.append(int(input('Digite a idade do professor: ')))
                dict_professores[matricula] = novo_professor
                print('Professor cadastrado com sucesso!\n')
                print(f'Matriculaa: {matricula}, nome: {dict_professores[matricula][0]}, idade: {dict_professores[matricula][1]}')
        except ValueError:
            print('A matricula deve ser um número inteiro!\n')
        finally:
            resposta = continuar_funcao()
            if resposta == 1:
                break


while True:
    selecao = int(input('Desempenho escolar\nO que deseja?\n1 - Registrar novo aluno\n2 - Registrar novo professor\n3 - Registrar nova disciplina\n4 - Registrar nota de aluno\n5 - Editar nota de aluno\n6 - Imprimir nota de todos os alunos\n0 - Sair\n'))
    match selecao:
        case 0:
            os.system('cls')
            print('Encerrando...')
            quit()
        case 1:
            registrar_novo_aluno()
        case 2:
            registrar_novo_professor()
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case 6:
            ...
        case _:
            print('[ERRO] Opção inválida! Tente novamente. [ERRO]')