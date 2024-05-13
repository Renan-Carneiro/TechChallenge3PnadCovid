import streamlit as st
import requests

from streamlit_lottie import st_lottie



st.set_page_config(page_title='Tech Challenge3: PNAD COVID' , page_icon='✔' , layout='wide')
st.sidebar.success("Selecione uma página acima.")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#asset
lottie_animation = load_lottieurl('https://lottie.host/embed/fe826aed-b1b4-4a22-9b27-bd28df64b43b/VgeaePd6aS.json')

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
    with right_column:
        st_lottie(lottie_animation,height=300,key='covid')