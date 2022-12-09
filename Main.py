import Sugestao
import Reclamacoes

sugestao = Sugestao.Sugestao()
reclamacoes = Reclamacoes.Reclamacoes()


opcao = 5
while opcao != 4:
    print('-' * 38)
    print('Sistema de Ouvidoria')
    print()
    print('Menu do Sistema')
    print('Opcoes:')
    print('1 para Registrar')
    print('2 para Listar')
    print('3 para apagar')
    print('4 para sair')
    print('-' * 38)
    opcao = int(input('Digite a sua opcao '))

    if opcao == 1:
        print('1- Sugestoes')
        print('2- Reclamações')
        registro = int(input('Escolha a opção: '))

        if registro == 1:
            print('Registrar Sugestoes')
            nome = input('Digite seu Nome ')
            descri = input('Digite sua Ocorrencia ')
            sugestao.adicionar_Ocorrencia(nome,descri)

        if registro == 2:
            print('Registrar Reclamações')
            nome = input('Digite seu Nome ')
            descri = input('Digite sua Reclamação ')
            reclamacoes.adicionar_Reclamacoes(nome,descri)
            

    if opcao == 2:
      sugestao.lista_sugestao()
      reclamacoes.lista_reclamacoes()

    if opcao == 3:
        print('-' * 50)
        print('[1]: Para apagar uma especifica\n[2]: Para apagar tudo')
        apagar = int(input('Digite '))
        print('-' * 50)

        if (apagar == 1):
            print('1- Sugestoes')
            print('2- Reclamações')
            remover = int(input('Escolha a opção: '))

            if (remover == 1):
                sugestao.lista_sugestao()
                postionToDelete = int(input('DIgite em que posição esta o item a ser apagado\n(Ex: se ele tiver na posição cinco digitas 5 ...)\n\t-'))
                sugestao.deletar_sugestao(postionToDelete)
            
            if (remover == 2):
                reclamacoes.lista_reclamacoes()
                postionToDeleteRecl = int(input('DIgite em que posição esta o item a ser apagado\n(Ex: se ele tiver na posição cinco digitas 5 ...)\n\t-'))
                reclamacoes.deletar_reclamacoes(postionToDeleteRecl)

        
        if (apagar == 2):
            print('1- Todas as Sugestoes')
            print('2- Todas as Reclamações')
            removerAll = int(input('Escolha a opção: '))
            
            if (removerAll == 1):
                sugestao.deletar_allsugestao()

            if (removerAll == 2):
                reclamacoes.deletar_allreclamacoes()
                
    if opcao == 4:
        print('Obrigado por usar o Sistema de Ouvidoria')
        break
