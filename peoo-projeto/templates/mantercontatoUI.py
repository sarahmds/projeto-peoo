import streamlit as st
from models.contato import Contatos, Contato

def salvar_contato_interface():
    st.title("Salvar Contato")
    nome = st.text_input("Nome do Contato")
    telefone = st.text_input("Telefone do Contato")

    if st.button("Salvar Contato"):
        if nome and telefone:
            contato = Contato(nome, telefone)
            Contatos.inserir(contato)
            st.success(f"Contato {nome} salvo com sucesso!")
        else:
            st.warning("Por favor, preencha todos os campos.")

def listar_contatos():
    st.title("Lista de Contatos")
    contatos = Contatos.listar()
    if contatos:
        st.write("### Contatos Salvos:")
        for contato in contatos:
            st.write(f"**Nome:** {contato.nome} | **Telefone:** {contato.telefone}")
    else:
        st.write("Nenhum contato salvo.")
