import streamlit as st
from templates.manterperfilUI import editar_perfil
from templates.mantermensagemUI import enviar_mensagem, apagar_mensagem
from templates.mantergrupoUI import listar_grupos, criar_grupo_interface, adicionar_membro_grupo, remover_membro_grupo, sair_grupo,  excluir_grupo
from templates.mantercontatoUI import listar_contatos, salvar_contato_interface
from models.membro import Membro, Membros
from models.grupo import Grupos
from models.contato import Contatos, Contato


def main():
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio("Escolha uma opção", [
        "Editar Perfil", "Enviar Mensagem", "Apagar Mensagem", "Criar Grupo",
        "Adicionar Membro", "Remover Membro", "Sair do Grupo", 
        "Listar Grupos", "Listar Contatos", "Salvar Contato"
    ])
    
    if opcao == "Editar Perfil":
        editar_perfil()
    elif opcao == "Enviar Mensagem":
        enviar_mensagem()  
    elif opcao == "Apagar Mensagem":
        apagar_mensagem()  
    elif opcao == "Criar Grupo":
        criar_grupo_interface()
    elif opcao == "Listar Grupos":
        listar_grupos()
    elif opcao == "Listar Contatos":
        listar_contatos()
    elif opcao == "Salvar Contato":
        salvar_contato_interface()
    elif opcao == "Adicionar Membro":
        adicionar_membro_grupo()
    elif opcao == "Remover Membro":
        remover_membro_grupo()
    elif opcao == "Sair do Grupo":
        sair_grupo()

if __name__ == "__main__":
    main()

def main():
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Escolha uma opção", ["Enviar Mensagem", "Excluir Grupo"])

    if menu == "Enviar Mensagem":
        enviar_mensagem()
    elif menu == "Excluir Grupo":
        excluir_grupo()
