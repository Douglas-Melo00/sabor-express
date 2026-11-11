# def é para definir a funçao. os é a bliblioteca para funcionar os recursos do terminal
# pass serve para nao aparecer linha vermelha no codigo enquanto ainda define a função
# append() cria uma lista adicionando elementos em posiçoões
# remove() remove elementos da lista
# pop() remove a posição de um elemento na lista, sucessivamente os outros elementos mudam de lugar para preencher o espaço.
# insert()  adiciona um dado manualmente ao código, ou para adicionar um dado que o usuário digitou em uma lista que já existe. Controla a posição onde o dado vai entrar.
# for significa para cada. laço de repetição que é definido manualmente.
# in significa que esta se referindo a uma lista
# while  laço de repetição que é indefinido, não tem fim enquanto uma condição apresentar verdadeira, apresentando verdadeira ele termina.
# as serve para dar apelido a variavel, biblioteca (modulos) e arquivos abertos.


import os  # O módulo 'os' permite interagir com o sistema operacional (utilizado aqui para limpar a tela do terminal).

# Lista global que armazena dicionários contendo as informações de cada restaurante cadastrado.
restaurantes = [{'nome':'Praça','categoria':'japonesa','ativado': False},
                {'nome':'Pizza suprema', 'categoria':'Pizza','ativado': True},
                {'nome': 'Cantina', 'categoria':'italiana','ativado': False}]

def exbir_nome_do_programa(): 
    """Exibe o logotipo estilizado do programa em ASCII art no topo do console."""
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░
""")

def exibir_opcoes():
    """Exibe no menu principal as opções disponíveis para o usuário interagir."""
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    """Prepara a tela e exibe o subtítulo correspondente ao encerramento do app."""
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    """Pausa a execução aguardando o usuário pressionar uma tecla e reinicia o fluxo chamando main()."""
    input('\nDigite uma tecla para voltar ao menu')
    main()

def opcao_invalida():
    """Trata entradas incorretas do usuário, exibindo um aviso e retornando ao menu."""
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto): 
    """
    Cria uma moldura dinâmica ao redor de um texto usando o tamanho da string.
    - len(texto): Conta a quantidade de caracteres da string recebida.
    - Operador de multiplicação de strings ('*'): Repete o caractere '*' para criar a linha proporcional ao texto.
    - os.system('cls'): Limpa a tela do terminal do Windows antes de exibir o subtítulo.
    """
    os.system('cls')
    linha = '*' * (len(texto) + 4) # Multiplica o asterisco pelo tamanho do texto + 4 espaços de respiro
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """Coleta dados de um novo estabelecimento, cria um dicionário e o adiciona à lista global de restaurantes."""
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    
    # Criação de um dicionário representando o novo restaurante com status padrão inativo (False)
    dados_do_restaurante = {'nome': nome_do_restaurante,'categoria': categoria, 'ativado':False}
    
    # O método .append() adiciona o novo dicionário ao final da lista 'restaurantes'
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Percorre a lista de restaurantes e exibe os dados formatados em formato de tabela no terminal."""
    exibir_subtitulo('Listando restaurantes')

    # O método .ljust() preenche a string com espaços à direita para alinhar perfeitamente as colunas
    print (f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status") 
    
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        
        # Operador ternário inline: define 'ativado' se for True, ou 'desativado' se for False
        ativo = 'ativado' if restaurante['ativado'] else 'desativado'
        
        print(f"{nome.ljust(22)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    """Busca um restaurante pelo nome e inverte o seu estado atual (ativado/desativado)."""
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    
    # Variável de controle (bandeira) para verificar se o item foi encontrado ou não na busca
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            
            # O operador 'not' inverte o valor booleano atual (de True para False, ou de False para True)
            restaurante['ativado'] = not restaurante['ativado']
            
            # Operador ternário para customizar a mensagem de acordo com o novo estado gerado
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativado'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    # 'if not' verifica se a bandeira continua falsa (ou seja, percorreu tudo e não achou o restaurante)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
        
    voltar_ao_menu_principal()

def escolher_opcoes():
    """Lê a escolha do usuário e direciona para a função correspondente usando estruturas condicionais e tratamento de erros."""
    try:
        # Tenta converter a entrada do usuário para um número inteiro
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}\n')

        # Direcionamento de fluxo com base na escolha numérica
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except:
        # Bloco except captura falhas (como o usuário digitar letras em vez de números) e evita que o programa quebre
        opcao_invalida()

def main():
    """Função principal que gerencia o ciclo de vida inicial da aplicação."""
    os.system('cls')
    exbir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

# Garante que o programa seja executado diretamente a partir do arquivo principal
if __name__ == '__main__':
    main()