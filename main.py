from metodos import *

testa = True

while testa: 

    imprime_menu_principal()
    menu_principal = int(input("\nQual sua opção? ---> "))

#=========================== Médico ===========================
    if menu_principal == 1:

        imprime_menu_medico() #mostra o menu com as opções de médico              
        menu_medico = int(input("\nQual sua opção? ---> "))

        if menu_medico == 1:
            criar_medico_principal();  

        elif menu_medico == 2: 
            busca_medico_pelo_crm()
        
        elif menu_medico == 3:
            exclui_medico_pelo_crm()
            
        elif menu_medico == 4:
            testa = True
 
        else:
            print("\nOpção inválida!")
    
#========================= Pacientes =========================

    elif menu_principal == 2:

        imprime_menu_paciente() #mostra o menu com as opções de paciente 
        menu_paciente = int(input("\nQual sua opção? ---> "))
        
        if menu_paciente == 1:
            criar_paciente_principal()

        elif menu_paciente == 2: 
            busca_paciente_pelo_cpf()
             
        elif menu_paciente == 3:
            exclui_paciente_pelo_cpf()

        elif menu_paciente == 4:

            testa = True

        else:
            print("\nOpção inválida!")

#======================= Agendamentos =========================

    elif menu_principal == 3: 

        imprime_menu_administrativo() #mostra o menu com as opções administrativas 
        menu_administrativo = int(input("\nQual sua opção? ---> "))

        if menu_administrativo == 1:

            imprime_menu_agendamentos() #mostra o menu com as opções de agendamento 
            menu_agendamentos = int(input("\nQual sua opção? ---> "))

            if menu_agendamentos == 1:
                cria_agendamento()

            elif menu_agendamentos == 2: 
                busca_agendamento_pelo_codigo()
            
            elif menu_agendamentos == 3:
                exclui_agendamento_pelo_codigo()
                
            elif menu_agendamentos == 4:
                testa = True

            else:
                print("\nOpção inválida!")
        
        elif menu_administrativo == 2: 

            imprime_menu_procedimentos() #mostra o menu com as opções p\ procedimentos
            menu_procedimentos = int(input("\nQual sua opção? ---> "))

            if menu_procedimentos == 1:
                cria_procedimento()

            elif menu_procedimentos == 2:
                lista_procedimentos()
            
            else: 
                testa = True

        elif menu_administrativo == 3:
            testa = True

        else:
            print("\nOpção inválida!")

    elif menu_principal == 4: 

        testa1 = input("\nDeseja mesmo encerrar o programa? (Sim | Não)\nQual sua opção? ---> ")

        if testa1.upper() == "SIM":
            print("\nObrigado por utilizar nosso sistema!\n")
            testa = False

    else:
        print("\nOpção inválida!")