import streamlit as st
from models.grupo import Grupos, Grupo
from models.contato import Contato, Contatos
from models.membro import Membros, Membro

def listar_grupos():
    grupos = Grupos.listar()
    if grupos:
        st.write("Grupos Criados:")
        for grupo in grupos:
            st.write(f"Grupo: {grupo.nome}, ID: {grupo.id}")
            # Filtra os membros do grupo atual
            membros_grupo = [membro for membro in Membros.listar() if membro.id_grupo == grupo.id]
            if membros_grupo:
                st.write("Membros:")
                for membro in membros_grupo:
                    contato = Contatos.listar_id(membro.id_perfil)
                    if contato:
                        st.write(f"- {contato.nome}")
                    else:
                        st.write(f"- Membro com ID {membro.id_perfil} não encontrado.")
            else:
                st.write("Nenhum membro neste grupo.")
    else:
        st.write("Nenhum grupo criado ainda.")

def criar_grupo_interface():
    st.title("Criar Grupo")
    nome_grupo = st.text_input("Nome do Grupo")

    if st.button("Criar Grupo"):
        if nome_grupo:
            grupo = Grupo(id=len(Grupos.listar()) + 1, nome=nome_grupo)
            Grupos.inserir(grupo)
            Grupos.salvar()  # Salva os grupos
            st.success(f"Grupo {nome_grupo} criado com sucesso!")
        else:
            st.warning("Por favor, preencha o nome do grupo.")

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
        # Verifica se o membro já foi adicionado
        if any(m.id_perfil == contato_selecionado.id and m.id_grupo == grupo_selecionado.id for m in Membros.listar()):
            st.warning(f"{contato_selecionado.nome} já é membro deste grupo.")
        else:
            membro = Membro(id=len(Membros.listar()) + 1, id_grupo=grupo_selecionado.id, id_perfil=contato_selecionado.id)
            Membros.objetos.append(membro)
            Membros.salvar()  # Salvar após adicionar
            st.success(f"Membro {contato_selecionado.nome} adicionado ao grupo {grupo_selecionado.nome}!")

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

    # Carrega o nome do membro selecionado
    membro_selecionado = st.selectbox("Selecione o Membro", membros_grupo, format_func=lambda m: Contatos.listar_id(m.id_perfil).nome)

    if st.button("Remover Membro"):
        # Remover membro
        if membro_selecionado:
            Membros.objetos = [m for m in Membros.objetos if m.id != membro_selecionado.id]
            Membros.salvar()  # Salvar após remover
            st.success(f"Membro {Contatos.listar_id(membro_selecionado.id_perfil).nome} removido do grupo {grupo_selecionado.nome}!")

def excluir_grupo_interface():
    st.title("Excluir Grupo")

    Grupos.abrir()

    if not Grupos.listar():
        st.warning("Não há grupos para excluir.")
        return

    grupo_para_excluir = st.selectbox(
        "Selecione o grupo para excluir", 
        Grupos.listar(), 
        format_func=lambda g: g.nome
    )

    if st.button("Excluir Grupo"):
        if grupo_para_excluir:
            grupo_a_excluir = next((g for g in Grupos.listar() if g.id == grupo_para_excluir.id), None)

            if grupo_a_excluir:
                Grupos.excluir(grupo_a_excluir)
                Grupos.salvar()  # Salvar após excluir
                st.success(f"Grupo '{grupo_a_excluir.nome}' excluído com sucesso!")
            else:
                st.warning("Grupo não encontrado!")
        else:
            st.warning("Selecione um grupo para excluir.")


