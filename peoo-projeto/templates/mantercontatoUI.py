import streamlit as st
class Contato:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

def salvar_contato_interface():
    st.title("Salvar Contato")
    nome = st.text_input("Nome do Contato")
    email = st.text_input("E-mail do Contato")
    
    if st.button("Salvar Contato"):
        if nome and email:
            contato = Contato(nome, email)
            salvar_contato(contato)
            st.success(f"Contato {nome} salvo com sucesso!")
        else:
            st.warning("Por favor, preencha todos os campos.")

def listar_contatos():
    contatos = carregar_arquivo("contatos.json")
    if contatos:
        st.write("Contatos Salvos:")
        for contato in contatos:
            st.write(f"Nome: {contato['nome']}, E-mail: {contato['email']}")
    else:
        st.write("Nenhum contato salvo.")
