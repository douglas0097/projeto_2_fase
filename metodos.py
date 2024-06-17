from banco_dados1 import *

#======================== Banco de Dados =======================

endereco = "localhost"
usuario = "root"
senha = "12345678"

conexao = criarConexaoInicial(endereco, usuario, senha)

sql_criar_bd = "CREATE DATABASE IF NOT EXISTS hospital"
criarBancoDados(conexao, sql_criar_bd)

sql_criar_tabela_medico = """
    CREATE TABLE IF NOT EXISTS medico(
        crm INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45),
        especialidade VARCHAR(45),
        telefone VARCHAR(45)
    )
"""
sql_criar_tabela_paciente = """
    CREATE TABLE IF NOT EXISTS paciente(
        cpf INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(45),
        idade VARCHAR(45),
        endereco VARCHAR(45),
        telefone VARCHAR(45)
    )
"""
sql_criar_tabela_agendamentos = """
    CREATE TABLE IF NOT EXISTS agendamento(
        id INT AUTO_INCREMENT PRIMARY KEY,
        cpf VARCHAR(45),
        consulta VARCHAR(45)
    )
"""
sql_criar_tabela_procedimentos = """
    CREATE TABLE IF NOT EXISTS procedimento(
        id INT AUTO_INCREMENT PRIMARY KEY,
        cpf VARCHAR(45),
        consulta VARCHAR(45)
    )
"""

criarTabela(conexao, "hospital", sql_criar_tabela_medico)
criarTabela(conexao, "hospital", sql_criar_tabela_paciente)
criarTabela(conexao, "hospital", sql_criar_tabela_agendamentos)
criarTabela(conexao, "hospital", sql_criar_tabela_procedimentos)

sql_listar_medicos = "SELECT * FROM medico"
sql_listar_pacientes = "SELECT * FROM paciente"
sql_listar_agendamentos = "SELECT * FROM agendamento"
sql_listar_procedimentos = "SELECT * FROM procedimento"

#====================== Métodos ============================

def imprime_menu_principal():
    print("""
           ╔═══════════════════════════════╗
           ║       Bem-vindo ao Help       ║
           ║ Escolha uma de nossas opções: ║
           ║  1. Médico                    ║
           ║  2. Paciente                  ║
           ║  3. Administrativo            ║
           ║  4. Sair                      ║
           ╚═══════════════════════════════╝ """)
def imprime_menu_medico():
    print(""" 
        ╔═════════════════════════════════════╗
        ║ Escolha uma de nossas opções:       ║
        ║                                     ║
        ║  1. Cadastrar médico                ║
        ║  2. Pesquisar médico por CRM        ║
        ║  3. Excluir médico por CRM          ║
        ║  4. Voltar ao menu anterior         ║
        ╚═════════════════════════════════════╝ """) 
def imprime_menu_paciente():
    print( """
        ╔═══════════════════════════════════════╗
        ║ Escolha uma de nossas opções:         ║
        ║                                       ║
        ║  1. Cadastrar paciente                ║
        ║  2. Pesquisar paciente por CPF        ║
        ║  3. Excluir paciente por CPF          ║
        ║  4. Voltar ao menu principal          ║
        ╚═══════════════════════════════════════╝ """)
def imprime_menu_administrativo():
    print( """
        ╔═══════════════════════════════════════╗
        ║ Escolha uma de nossas opções:         ║
        ║                                       ║
        ║  1. Agendamentos                      ║
        ║  2. Registro de procedimentos         ║
        ║  3. Voltar ao menu principal          ║
        ╚═══════════════════════════════════════╝ """)
def imprime_menu_agendamentos():
    print( """
        ╔═══════════════════════════════════════╗
        ║ Escolha uma de nossas opções:         ║
        ║                                       ║
        ║  1. Adicionar agendamentos            ║
        ║  2. Visualizar agendamentos           ║
        ║  3. Cancelar agendamento              ║
        ║  4. Voltar ao menu principal          ║
        ╚═══════════════════════════════════════╝ """)
def imprime_menu_procedimentos():
    print( """
        ╔═══════════════════════════════════════╗
        ║ Escolha uma de nossas opções:         ║
        ║                                       ║
        ║  1. Registrar um procedimento         ║
        ║  2. Listar procedimentos              ║
        ║  3. Voltar ao menu principal          ║
        ╚═══════════════════════════════════════╝ """)

def criar_medico_principal():
    def cria_medico():
                    
        testa = True

        while testa: 
            nome = input("\nInforme o nome do médico: ")
            especialidade = input("Informe a especialidade do médico: ")
            telefone = input("Informe o telefone do médico: ")

            if not nome or not especialidade or not telefone:
                print("\nInforme todos os dados solicitados!") 
            else:
                medico = { "nome": nome, "especialidade": especialidade, "telefone": telefone}
                testa = False
                return medico

    medico = cria_medico()

    nome = medico["nome"]
    especialidade = medico["especialidade"]
    telefone = medico["telefone"]

    #insere o medico na tabela
    sql_inserir_medico = "INSERT INTO medico (nome, especialidade, telefone) VALUES (%s, %s, %s)"
    dados_insert = (nome, especialidade, telefone)
    insertNaTabela(conexao, sql_inserir_medico, dados_insert)
    print("Médico cadastrado com sucesso!")
    print(listarTabelas(conexao, sql_listar_medicos))
def busca_medico_pelo_crm():

    crm = input("Informe o crm do medico que você deseja buscar: ")
    cursor = conexao.cursor()
    sql_buscar_medico = "SELECT * FROM medico WHERE crm = %s"
    cursor.execute(sql_buscar_medico, (crm,))
    medico = cursor.fetchone()
    
    if medico:
        print(f"\nMédico encontrado:\n"
          f"Nome: {medico[1]}\n"
          f"especialidade: {medico[2]}\n"
          f"telefone: {medico[3]}\n")
    else:
        print("Nenhum médico encontrado com o CRM informado.")
def exclui_medico_pelo_crm():
    #mostra os medicos cadastrados antes de excluir
    print(listarTabelas(conexao, sql_listar_medicos))
        
    #remove um medico pelo crm 
    crm = input("Informe o crm do medico que você deseja remover: ")
    cursor = conexao.cursor()

    # SQL para buscar o médico pelo CRM antes de excluir
    sql_buscar_medico = "SELECT * FROM medico WHERE crm = %s"
    cursor.execute(sql_buscar_medico, (crm,))
    medico = cursor.fetchone()

    # Verifica se o médico com o CRM existe
    if not medico:
        print(f"Médico com CRM {crm} não encontrado.")
    else:
        sql_remover = "DELETE FROM medico WHERE crm = %s"
        dados_remover = (crm,)
        excluirDadosTabela(conexao, sql_remover, dados_remover)
        print("Médico removido com sucesso!")
    #---------------------------------------------------

def criar_paciente_principal():
    def cria_paciente():

        testa = True

        while testa:

            nome = input("\nInforme o nome do paciente: ")
            idade = input("Informe a idade do paciente: ")
            endereco = input("Informe o endereco do paciente: ")
            telefone = input("Informe o telefone do paciente: ")

            if not nome or not idade or not endereco or not telefone:
                print("\nInforme todos os dados solicitados!")
            else:
                paciente = { "nome": nome, "idade": idade, "endereco": endereco, "telefone": telefone}
                testa = False
                return paciente

    paciente = cria_paciente()

    nome = paciente["nome"]
    idade = paciente["idade"]
    endereco = paciente["endereco"]
    telefone = paciente["telefone"]

    #insere o paciente na tabela
    sql_inserir_paciente = "INSERT INTO paciente (nome, idade, endereco, telefone) VALUES (%s, %s, %s, %s)"
    dados_insert = (nome, idade, endereco, telefone)
    insertNaTabela(conexao, sql_inserir_paciente, dados_insert)
    print("Paciente cadastrado com sucesso!")
    print(listarTabelas(conexao, sql_listar_pacientes))
def busca_paciente_pelo_cpf():
    cpf = input("Informe o cpf do paciente que você deseja buscar: ")
    cursor = conexao.cursor()
    sql_buscar_paciente = "SELECT * FROM paciente WHERE cpf = %s"
    cursor.execute(sql_buscar_paciente, (cpf,))
    paciente = cursor.fetchone()

    if paciente:
        print(f"\nPaciente encontrado:\n"
          f"Nome: {paciente[1]}\n"
          f"Idade: {paciente[2]}\n"
          f"Endereço: {paciente[3]}\n"
          f"Telefone: {paciente[4]}")
    else:
        print("Nenhum paciente encontrado com o CPF informado.")
def exclui_paciente_pelo_cpf():
    
    #mostra os pacientes cadastrados antes de excluir
    print(listarTabelas(conexao, sql_listar_pacientes))

    #remove um paciente pelo cpf 
    cpf = input("Informe o cpf do paciente que você deseja remover: ")

    cursor = conexao.cursor()

    # SQL para buscar o paciente pelo CPF antes de excluir
    sql_buscar_paciente = "SELECT * FROM paciente WHERE cpf = %s"
    cursor.execute(sql_buscar_paciente, (cpf,))
    paciente = cursor.fetchone()

    # Verifica se o paciente com o CPF existe
    if not paciente:
        print(f"Paciente com CPF {cpf} não encontrado.")
    else:
        sql_remover = "DELETE FROM paciente WHERE cpf = %s"
        dados_remover = (cpf,)
        excluirDadosTabela(conexao, sql_remover, dados_remover)
        print("Paciente removido com sucesso!")

def cria_agendamento():
    def cria_agendamento():
                    
        testa = True

        while testa: 
            cpf = input("\nInforme o cpf do paciente: ")
            consulta = input("Informe o procedimento que será realizado: ")
            if not cpf or not consulta:
                print("\nInforme todos os dados solicitados!")
            else:
                agendamento = { "cpf": cpf, "consulta": consulta}
                testa = False
                return agendamento

    agendamento = cria_agendamento()

    cpf = agendamento["cpf"]
    consulta = agendamento["consulta"]

    #insere o medico na tabela
    sql_inserir_agendamento = "INSERT INTO agendamento (cpf, consulta) VALUES (%s, %s)"
    dados_insert = (cpf, consulta)
    insertNaTabela(conexao, sql_inserir_agendamento, dados_insert)
    print("Agendamento realizado com sucesso!")
    print(listarTabelas(conexao, sql_listar_agendamentos))
def busca_agendamento_pelo_codigo():

    id = input("\nInforme o código do agendamento que você deseja buscar: ")

    cursor = conexao.cursor()
    sql_buscar_agendamento = "SELECT * FROM agendamento WHERE id = %s"
    cursor.execute(sql_buscar_agendamento, (id,))
    consulta = cursor.fetchone()

    if consulta:
        print(f"\nAgendamento encontrado:\n"
        f"CPF do paciente: {consulta[1]}\n"
        f"Procedimento: {consulta[2]}\n")
    else:
        print("Nenhum agendamento encontrado.")
def exclui_agendamento_pelo_codigo():

    #mostra os agentamentos cadastrados antes de excluir
    print(listarTabelas(conexao, sql_listar_agendamentos))

    #remove um agendamento pelo código
    id = input("Informe o código do agendamento que você deseja remover: ")

    cursor = conexao.cursor()

    # SQL para buscar o paciente pelo CPF antes de excluir
    sql_buscar_agendamento = "SELECT * FROM agendamento WHERE id = %s"
    cursor.execute(sql_buscar_agendamento, (id,))
    consulta = cursor.fetchone()

    # Verifica se o paciente com o CPF existe
    if not consulta:
        print(f"Agendameno com código {id} não encontrado.")
    else:
        sql_remover = "DELETE FROM agendamento WHERE id = %s"
        dados_remover = (id,)
        excluirDadosTabela(conexao, sql_remover, dados_remover)
        print("Agendamento removido com sucesso!")

def cria_procedimento():
    def cria_procedimento():
                        
        testa = True

        while testa: 
            cpf = input("\nInforme o cpf do paciente: ")
            consulta = input("Informe o procedimento que foi realizado: ")

            if not cpf or not consulta:
                print("\nInforme todos os dados solicitados!")
            else:
                procedimento = { "cpf": cpf, "consulta": consulta}
                testa = False
                return procedimento

    procedimento = cria_procedimento()

    cpf = procedimento["cpf"]
    consulta = procedimento["consulta"]

    #insere o procedimento na tabela
    sql_inserir_procedimento = "INSERT INTO procedimento (cpf, consulta) VALUES (%s, %s)"
    dados_insert = (cpf, consulta)
    insertNaTabela(conexao, sql_inserir_procedimento, dados_insert)

    print("Procedimento cadastrado com sucesso!")
    print(listarTabelas(conexao, sql_listar_procedimentos))
def lista_procedimentos():
    print(listarTabelas(conexao, sql_listar_procedimentos))