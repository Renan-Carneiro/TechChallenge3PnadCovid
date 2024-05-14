import streamlit as st
from PIL import Image

st.markdown("""
# **Introdução**

Fomos desafiados a nos imaginarmos como experts em Data Analytics de um grande hospital para entender como foi o comportamento da população durante a pandemia de Coronavírus e para identificar quais seriam os melhores indicadores para o planejamento em um novo cenário de surto da doença.

O estudo do PNAD-COVID-19, realizado pelo IBGE (Instituo Brasileiro de Geografia e Estatística), é uma ótima fonte de dados, contendo todos os dados necessários para enfrentarmos o desafio proposto, além, é claro, de serem confiáveis. Tudo aquilo que é necessário para apresentarmos as análises propostas podem ser encontrados no estudo.

## A proposta exigiu que fizéssemos as análises dos seguintes dados:

- Características clínicas dos sintomas;
- Características da população;
- Características da sociedade;

## Além disso, ao entrarmos na base de dados do PNAD-COVID-19 e organizarmos esta base para análise, trouxemos as seguintes características:

- Utilização de no máximo 20 perguntas feitas na pesquisa;
- Utilizar 3 meses para construção da solução;
- Caracterização dos sintomas clínicos da população;
- Comportamento da população na época da COVID-19;
- Características econômicas da Sociedade.

A partir dessas condições, trouxemos uma breve análise dessas informações, explicitando o modo como organizamos o banco de dados, o porquê da seleção das melhores perguntas que trariam as melhores respostas e, por fim, as ações mais efetivas que o hospital deverá tomar em caso de um novo surto de COVID-19.
""")