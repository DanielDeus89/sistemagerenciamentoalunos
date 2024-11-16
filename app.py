import os

alunos = []

def exibir_opcoes():
    limpar_tela()
    print('1. Cadastrar novo aluno')
    print('2. Listar alunos cadastrados')
    print('3. Atualizar nota de um aluno')
    print('4. Excluir um aluno')
    print('5. Sair')

def cadastrar_novo_aluno():
    while True:
        nome_aluno = input('Digite o nome do novo Aluno: ').strip()
        if not nome_aluno:
            print('❌ O nome do aluno não pode estar vazio! Tente novamente.')
            continue

        while True:
            try:
                nota_aluno = float(input('Digite a nota do aluno (Entre 0 e 10): '))
                if 0 <= nota_aluno <= 10:
                    break
                else:
                    print('❌ A nota deve estar entre 0 e 10. Tente novamente.')
            except ValueError:
                print('❌ Por favor, insira um número válido para a nota.')

        aprovado = nota_aluno >= 6
        dados_do_aluno = {'nome': nome_aluno, 'nota': nota_aluno, 'aprovado': aprovado}
        alunos.append(dados_do_aluno)

        print(f'\n✅ O aluno {nome_aluno} foi cadastrado com sucesso!')
        print(f'   Nota: {nota_aluno} | Status: {"Aprovado" if aprovado else "Reprovado"}\n')

        while True:
            continuar = input('Deseja cadastrar outro aluno? (s/n) ').strip().lower()
            if continuar in ['s', 'n']:
                break
            print('❌ Opção inválida! Digite "s" para Sim ou "n" para Não.')

        if continuar == 'n':
            print('\n👍 Cadastro concluído! Retornando ao menu principal...')
            break

def listar_alunos():
    if not alunos:
        print("❌ Nenhum aluno cadastrado ainda.")
        return

    print("\n📋 Lista de Alunos")
    print(f"{'Nome'.ljust(20)} | {'Nota'.ljust(5)} | {'Status'}")
    print("-" * 35)
    for aluno in alunos:
        nome_aluno = aluno['nome']
        nota_aluno = aluno['nota']
        status = 'Aprovado' if aluno['aprovado'] else 'Reprovado'
        print(f"{nome_aluno.ljust(20)} | {str(nota_aluno).ljust(5)} | {status}")
    print('\n')

def atualizar_nota():
    nome_aluno = input('Digite o nome do aluno que deseja alterar a nota: ').strip()
    for aluno in alunos:
        if aluno['nome'].lower() == nome_aluno.lower():
            try:
                nova_nota = float(input(f"Digite a nova nota para {aluno['nome']} (Entre 0 e 10): "))
                if 0 <= nova_nota <= 10:
                    aluno['nota'] = nova_nota
                    aluno['aprovado'] = nova_nota >= 6
                    print(f"\n✅ Nota do aluno {aluno['nome']} atualizada com sucesso!")
                    return
                else:
                    print('❌ A nota deve estar entre 0 e 10.')
            except ValueError:
                print('❌ Insira um número válido.')
            return
    print(f"❌ Aluno '{nome_aluno}' não encontrado.")

def excluir_aluno():
    nome_aluno = input('Digite o nome do aluno que deseja excluir: ').strip()
    for i, aluno in enumerate(alunos):
        if aluno['nome'].lower() == nome_aluno.lower():
            alunos.pop(i)
            print(f"\n✅ O aluno {aluno['nome']} foi excluído com sucesso!")
            return
    print(f"❌ Aluno '{nome_aluno}' não encontrado.")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        exibir_opcoes()
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                cadastrar_novo_aluno()
            elif opcao == 2:
                listar_alunos()
            elif opcao == 3:
                atualizar_nota()
            elif opcao == 4:
                excluir_aluno()
            elif opcao == 5:
                print("\n👍 Saindo do sistema...")
                break
            else:
                print('❌ Opção inválida. Escolha entre 1 e 5.')
        except ValueError:
            print('❌ Insira um número válido.')

if __name__ == '__main__':
    main()
