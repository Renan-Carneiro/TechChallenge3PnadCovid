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
    with left_column:
        st.header('O Desafio')
        st.write(
            """
           Fomos desafiados a nos imaginarmos como experts em Data Analytics de um grande hospital para entender como foi o comportamento da população durante a pandemia de Coronavírus e para identificar quais seriam os melhores indicadores para o planejamento em um novo cenário de surto da doença.
            """
        )
        st.write('[FIAP](https://postech.fiap.com.br/)')