import streamlit as st
def criar_grupo_interface():
    st.title("Criar Grupo")
    nome_grupo = st.text_input("Nome do Grupo")
    membros = st.text_area("Membros (separados por vírgula)")
    
    if st.button("Criar Grupo"):
        if nome_grupo and membros:
            grupo = mantergrupoUI(id=len(carregar_grupos())+1, nome=nome_grupo, membros=membros.split(','))
            salvar_grupo(grupo)
            st.success(f"Grupo {nome_grupo} criado com sucesso!")
        else:
            st.warning("Por favor, preencha todos os campos.")

def listar_grupos():
    grupos = carregar_arquivo("grupos.json")
    if grupos:
        st.write("Grupos Criados:")
        for grupo in grupos:
            st.write(f"Grupo: {grupo['nome']}")
            st.write(f"Membros: {', '.join(grupo['membros'])}")
    else:
        st.write("Nenhum grupo criado ainda.")
