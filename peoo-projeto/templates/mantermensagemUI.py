import streamlit as st
from models.contato import Contatos
from models.grupo import Grupos
from models.mensagem import Mensagens, Mensagem

# Função para enviar mensagem
def enviar_mensagem():
    st.title("Enviar Mensagem")
    
    # Obtendo contatos e grupos
    contatos = Contatos.listar()
    grupos = Grupos.listar()

    # Seleção de destinatário
    destinatario_tipo = st.radio("Enviar para", ("Contato", "Grupo"))
    destinatario = None

    # Lógica para escolher o destinatário
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

    # Campo de texto para a mensagem
    mensagem_texto = st.text_area("Mensagem")

    # Envio da mensagem
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
    
    # Listando as mensagens
    mensagens = Mensagens.listar()

    if not mensagens:
        st.warning("Não há mensagens para apagar.")
        return

    # Seleção da mensagem para apagar
    mensagem_escolhida = st.selectbox(
        "Selecione a mensagem para apagar", 
        mensagens, 
        format_func=lambda m: f"De: {m.usuario_envia} - Para: {m.usuario_recebe or m.grupo_recebe} - {m.texto}"
    )

    if st.button("Apagar"):
        # Remover a mensagem escolhida
        mensagem_encontrada = next((m for m in mensagens if m.id == mensagem_escolhida.id), None)

        if mensagem_encontrada:
            Mensagens.remover(mensagem_encontrada)
            st.success("Mensagem apagada!")
        else:
            st.warning("Mensagem não encontrada.")
