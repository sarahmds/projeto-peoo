import streamlit as st
from models.contato import Contato, Contatos
from models.grupo import Grupos
from models.mensagem import Mensagens, Mensagem
from templates.mantergrupoUI import (
    adicionar_membro_grupo,
    criar_grupo_interface,
    excluir_grupo_interface,
    listar_grupos,
    remover_membro_grupo,
)
from templates.mantercontatoUI import excluir_contato_interface, listar_contatos

def main():
    st.title("Groupify")

    opcao = st.selectbox("Escolha uma opção", [
        "Editar Perfil",
        "Salvar Contato",
        "Enviar Mensagem",
        "Apagar Mensagem",
        "Criar Grupo",
        "Adicionar Membro ao Grupo",
        "Remover Membro do Grupo",
        "Excluir Grupo",
        "Excluir Contato",
        "Listar Contatos",
        "Listar Grupos",
        "Listar Mensagens"
    ])

    if opcao == "Editar Perfil":
        editar_perfil()
    elif opcao == "Salvar Contato":
        salvar_contato()
    elif opcao == "Enviar Mensagem":
        enviar_mensagem()
    elif opcao == "Apagar Mensagem":
        apagar_mensagem()
    elif opcao == "Criar Grupo":
        criar_grupo_interface()
    elif opcao == "Adicionar Membro ao Grupo":
        adicionar_membro_grupo()
    elif opcao == "Remover Membro do Grupo":
        remover_membro_grupo()
    elif opcao == "Excluir Grupo":
        excluir_grupo_interface()
    elif opcao == "Excluir Contato":
        excluir_contato()
    elif opcao == "Listar Contatos":
        listar_contatos()
    elif opcao == "Listar Grupos":
        listar_grupos()
    elif opcao == "Listar Mensagens":
        listar_mensagens()

# Função para excluir contato
def excluir_contato():
    st.title("Excluir Contato")
    contatos = Contatos.listar()

    if not contatos:
        st.warning("Não há contatos para excluir.")
        return

    contato_escolhido = st.selectbox(
        "Selecione o contato para excluir", 
        contatos, 
        format_func=lambda c: c.nome
    )

    if st.button("Excluir Contato"):
        contato_encontrado = next((c for c in contatos if c.id == contato_escolhido.id), None)

        if contato_encontrado:
            Contatos.excluir(contato_encontrado)
            st.success(f"Contato {contato_escolhido.nome} excluído com sucesso!")
        else:
            st.warning("Contato não encontrado.")

# Função para listar mensagens
def listar_mensagens():
    st.title("Listar Mensagens")
    mensagens = Mensagens.listar()

    if not mensagens:
        st.warning("Não há mensagens para exibir.")
        return

    for mensagem in mensagens:
        if mensagem.usuario_recebe:
            st.write(f"De: {mensagem.usuario_envia} - Para: {mensagem.usuario_recebe} - {mensagem.texto}")
        else:
            st.write(f"De: {mensagem.usuario_envia} - Para o Grupo: {mensagem.grupo_recebe} - {mensagem.texto}")

# Função para enviar mensagem
def enviar_mensagem():
    st.title("Enviar Mensagem")
    
    contatos = Contatos.listar()
    grupos = Grupos.listar()

    destinatario_tipo = st.radio("Enviar para", ("Contato", "Grupo"))
    destinatario = None

    if destinatario_tipo == "Contato":
        if not contatos:
            st.warning("Adicione contatos primeiro.")
            return
        destinatario = st.selectbox("Para o Contato", contatos, format_func=lambda c: c.nome)
    else:
        if not grupos:
            st.warning("Crie um grupo primeiro.")
            return
        destinatario = st.selectbox("Para o Grupo", grupos, format_func=lambda g: g.nome)

    mensagem_texto = st.text_area("Mensagem")

    if st.button("Enviar"):
        if mensagem_texto:
            if destinatario_tipo == "Contato":
                mensagem = Mensagem(
                    id=len(Mensagens.listar()) + 1,
                    usuario_envia="Você", 
                    usuario_recebe=destinatario.nome,  
                    grupo_recebe=None,
                    texto=mensagem_texto 
                )
            else:
                mensagem = Mensagem(
                    id=len(Mensagens.listar()) + 1,
                    usuario_envia="Você", 
                    usuario_recebe=None,
                    grupo_recebe=destinatario.nome,  
                    texto=mensagem_texto 
                )
            Mensagens.inserir(mensagem)
            st.success("Mensagem enviada!")
        else:
            st.warning("Digite uma mensagem.")

# Função para apagar mensagem
def apagar_mensagem():
    st.title("Apagar Mensagem")
    mensagens = Mensagens.listar()

    if not mensagens:
        st.warning("Não há mensagens para apagar.")
        return

    mensagem_escolhida = st.selectbox(
        "Selecione a mensagem para apagar", 
        mensagens, 
        format_func=lambda m: f"De: {m.usuario_envia} - Para: {m.usuario_recebe or m.grupo_recebe} - {m.texto}"
    )

    if st.button("Apagar"):
        mensagem_encontrada = next((m for m in mensagens if m.id == mensagem_escolhida.id), None)

        if mensagem_encontrada:
            Mensagens.remover(mensagem_encontrada)
            st.success("Mensagem apagada!")
        else:
            st.warning("Mensagem não encontrada.")

# Função para editar o perfil
def editar_perfil():
    st.title("Editar Perfil")
    nome_perfil = st.text_input("Novo nome para o perfil")
    if st.button("Salvar Alterações"):
        if nome_perfil:
            st.success(f"Perfil alterado para {nome_perfil} com sucesso!")
        else:
            st.warning("Por favor, preencha o novo nome do perfil.")

# Função para salvar o contato
def salvar_contato():
    st.title("Salvar Contato")
    nome_contato = st.text_input("Nome do Contato")
    telefone_contato = st.text_input("Telefone do Contato")

    if st.button("Salvar Contato"):
        if nome_contato and telefone_contato:
            id_contato = len(Contatos.listar()) + 1
            contato = Contato(id_contato, nome=nome_contato, telefone=telefone_contato)
            Contatos.inserir(contato)
            st.success(f"Contato {nome_contato} salvo com sucesso!")
        else:
            st.warning("Por favor, preencha todos os campos.")

if __name__ == "__main__":
    main()
