import streamlit as st

def enviar_mensagem():
    st.title("Enviar Mensagem")
    usuario = st.text_input("Para:")
    mensagem = st.text_area("Mensagem")
    if st.button("Enviar"):
        st.success("Mensagem enviada!")

def apagar_mensagem():
    st.title("Apagar Mensagem")
    id_mensagem = st.number_input("ID da Mensagem", min_value=1)
    if st.button("Apagar"):
        st.success("Mensagem apagada!")
