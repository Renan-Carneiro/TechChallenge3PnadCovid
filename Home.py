import streamlit as st
from PIL import Image
st.set_page_config(page_title="Tech Challenge3: PNAD COVID", page_icon=":house:",layout='wide')
st.sidebar.success("Selecione uma página acima.")
image = Image.open("./imagens/covid.png")
st.image(image)


#Header
with st.container():

    st.title('Bem vindo(a)')
    st.title('Tech Challenge 3: PNAD COVID')
    st.subheader('Use a barra de navegação ao lado para navegar')
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    st.header('O Desafio')
    st.write(
        """
        Esse estudo é para a Pós Graduação em Data Analytics da FIAP, entregue em 05/2024.
        """
    )
    st.write('[FIAP](https://postech.fiap.com.br/)')