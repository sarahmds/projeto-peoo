import streamlit as st
from templates.manterperfilUI import editar_perfil
from templates.mantermensagemUI import enviar_mensagem, apagar_mensagem
from templates.mantergrupoUI import listar_grupos, criar_grupo_interface
from templates.mantercontatoUI import listar_contatos, salvar_contato_interface
# class indexUI():
#     def menu_admin():            
#         op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Horários", "Cadastro de Perfis", "Cadastro de Profissionais", "Cadastro de Serviços", "Abrir Agenda do Dia", "Meus Dados"])
        # if op == "Cadastro de Usuário":
        # if op == "Cadastro de Grupos":
        # if op == "Cadastro de contatos": 


def main():
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio("Escolha uma opção", [
        "Editar Perfil", "Enviar Mensagem", "Criar Grupo", "Adicionar Membro", "Remover Membro", "Sair do Grupo", "Listar Grupos", "Listar Contatos", "Salvar Contato"
    ])
    
    if opcao == "Editar Perfil":
        editar_perfil()
    elif opcao == "Enviar Mensagem":
        enviar_mensagem()
    elif opcao == "Criar Grupo":
        criar_grupo_interface()
main()


