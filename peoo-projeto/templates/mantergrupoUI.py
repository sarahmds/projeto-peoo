import streamlit as st
from models.grupo import Grupos, Grupo  # Importando corretamente a classe Grupo
from models.contato import Contatos
from models.membro import Membros, Membro

# Função para listar os grupos
def listar_grupos():
    grupos = Grupos.listar()
    if grupos:
        st.write("Grupos Criados:")
        for grupo in grupos:
            st.write(f"Grupo: {grupo.nome}, ID: {grupo.id}")
            membros_grupo = Membros.listar()
            if membros_grupo:
                st.write("Membros:")
                for membro in membros_grupo:
                    if membro.id_grupo == grupo.id:
                        contato = Contatos.listar_id(membro.id_perfil)
                        if contato:
                            st.write(f"- {contato.nome}")
            else:
                st.write("Nenhum membro neste grupo.")
    else:
        st.write("Nenhum grupo criado ainda.")

# Função para criar um grupo
def criar_grupo_interface():
    st.title("Criar Grupo")
    nome_grupo = st.text_input("Nome do Grupo")

    if st.button("Criar Grupo"):
        if nome_grupo:
            grupo = Grupo(id=len(Grupos.listar()) + 1, nome=nome_grupo)  # Agora, a classe Grupo está corretamente importada
            Grupos.inserir(grupo)
            st.success(f"Grupo {nome_grupo} criado com sucesso!")
        else:
            st.warning("Por favor, preencha o nome do grupo.")

# Função para adicionar membro ao grupo
def adicionar_membro_grupo():
    st.title("Adicionar Membro ao Grupo")
    grupos = Grupos.listar()
    if not grupos:
        st.warning("Crie um grupo primeiro.")
        return

    grupo_selecionado = st.selectbox("Selecione o Grupo", grupos, format_func=lambda g: g.nome)
    contatos = Contatos.listar()
    if not contatos:
        st.warning("Adicione contatos primeiro.")
        return

    contato_selecionado = st.selectbox("Selecione o Contato", contatos, format_func=lambda c: c.nome)

    if st.button("Adicionar Membro"):
        # Verificar se o contato já é membro do grupo
        if any(membro.id_perfil == contato_selecionado.id for membro in Membros.listar() if membro.id_grupo == grupo_selecionado.id):
            st.warning(f"{contato_selecionado.nome} já é membro deste grupo.")
        else:
            membro = Membro(id=len(Membros.listar()) + 1, id_grupo=grupo_selecionado.id, id_perfil=contato_selecionado.id)
            Membros.inserir(membro)
            st.success(f"Membro {contato_selecionado.nome} adicionado ao grupo {grupo_selecionado.nome}!")

# Função para remover membro do grupo
def remover_membro_grupo():
    st.title("Remover Membro do Grupo")
    grupos = Grupos.listar()
    if not grupos:
        st.warning("Crie um grupo primeiro.")
        return

    grupo_selecionado = st.selectbox("Selecione o Grupo", grupos, format_func=lambda g: g.nome)
    membros_grupo = [membro for membro in Membros.listar() if membro.id_grupo == grupo_selecionado.id]
    if not membros_grupo:
        st.warning("Nenhum membro neste grupo.")
        return

    membro_selecionado = st.selectbox("Selecione o Membro", membros_grupo, format_func=lambda m: Contatos.listar_id(m.id_perfil).nome)

    if st.button("Remover Membro"):
        Membros.excluir(membro_selecionado)
        st.success(f"Membro {Contatos.listar_id(membro_selecionado.id_perfil).nome} removido do grupo {grupo_selecionado.nome}!")

# Função para sair do grupo
def sair_grupo():
    st.title("Sair do Grupo")
    grupos = Grupos.listar()
    if not grupos:
        st.warning("Crie um grupo primeiro.")
        return

    grupo_selecionado = st.selectbox("Selecione o Grupo", grupos, format_func=lambda g: g.nome)
    membros_grupo = [membro for membro in Membros.listar() if membro.id_grupo == grupo_selecionado.id]
    if not membros_grupo:
        st.warning("Nenhum membro neste grupo.")
        return

    membro_selecionado = st.selectbox("Selecione o Membro", membros_grupo, format_func=lambda m: Contatos.listar_id(m.id_perfil).nome)

    if st.button("Sair do Grupo"):
        Membros.excluir(membro_selecionado)
        st.success(f"Você saiu do grupo {grupo_selecionado.nome}!")

def excluir_grupo():
    st.title("Excluir Grupo")
    grupos = Grupos.listar()

    if not grupos:
        st.warning("Não há grupos para excluir.")
        return

    grupo_escolhido = st.selectbox(
        "Selecione o grupo para excluir", 
        grupos, 
        format_func=lambda g: g.nome
    )

    if st.button("Excluir"):
        Grupos.remover(grupo_escolhido)
        st.success(f"Grupo {grupo_escolhido.nome} excluído com sucesso!")
