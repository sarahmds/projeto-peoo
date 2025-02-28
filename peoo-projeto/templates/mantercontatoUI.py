import streamlit as st
from models.contato import Contatos

# Função para listar contatos
def listar_contatos():
    st.title("Lista de Contatos")
    
    # Carregar os contatos
    Contatos.abrir()
    contatos = Contatos.listar()

    if contatos:
        st.write("### Contatos Salvos:")
        for contato in contatos:
            st.write(f"**Nome:** {contato.nome} | **Telefone:** {contato.telefone}")
    else:
        st.write("Nenhum contato salvo.")

# Função para excluir contato
def excluir_contato_interface():
    st.title("Excluir Contato")

    # Carregar contatos
    Contatos.abrir()
    contatos = Contatos.listar()

    if not contatos:
        st.warning("Não há contatos para excluir.")
        return

    # Seleção do contato para excluir
    contato_para_excluir = st.selectbox(
        "Selecione o contato para excluir",
        contatos,
        format_func=lambda c: c.nome
    )

    # Botão para excluir o contato
    if st.button("Excluir Contato"):
        if contato_para_excluir:
            Contatos.excluir(contato_para_excluir)  # Excluir o contato selecionado
            st.success(f"Contato '{contato_para_excluir.nome}' excluído com sucesso!")
        else:
            st.warning("Selecione um contato para excluir.")


