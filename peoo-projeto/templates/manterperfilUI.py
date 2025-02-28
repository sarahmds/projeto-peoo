import streamlit as st
from models.contato import Contatos, Contato

def editar_perfil():
    st.title("Editar Perfil")
    nome = st.text_input("Nome", "")
    telefone = st.text_input("Telefone", "")
    foto = st.file_uploader("Upload da Foto", type=["jpg", "png", "jpeg"])

    if foto:
        st.image(foto, caption="Foto carregada", use_column_width=True)

    if nome:
        st.write(f"Nome Atual: {nome}")
    if telefone:
        st.write(f"Telefone Atual: {telefone}")

    if st.button("Salvar"):
        if nome and telefone:
            st.success(f"Perfil atualizado com sucesso! Novo nome: {nome}, Novo telefone: {telefone}")
        else:
            st.warning("Por favor, preencha o nome e o telefone antes de salvar.")