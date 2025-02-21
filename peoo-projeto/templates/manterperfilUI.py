import streamlit as st
def editar_perfil():
    st.title("Editar Perfil")
    nome = st.text_input("Nome", "")
    foto = st.file_uploader("Upload da Foto", type=["jpg", "png", "jpeg"])
    
    if foto:
        st.image(foto, caption="Foto carregada", use_column_width=True)
    
    if nome:
        st.write(f"Nome Atual: {nome}")
    
    if st.button("Salvar"):
        if nome:
            st.success(f"Perfil atualizado com sucesso! Novo nome: {nome}")
        else:
            st.warning("Por favor, preencha o nome antes de salvar.")
