# LINK GITHUB PROJETO
# https://github.com/ikeda27/cdd_embraer_titanic 

#site referência: https://medium.com/@suzana.svm/data-science-udacity-titanic-e5b04a8e415f

# APENAS USE ISSO CASO FOR NO PC EM VEZ DO SITE ONLINE !!!
#pip install numpy
#pip install pandas
#pip install matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# MÉTODOS DE IMPORTAÇÃO (PARA FUTUROS HELPS)
# NO PYTHON DO PC FUNFA
# CAMINHO DIRETO DO ARQUIVO
#titanic = pd.read_csv("C:\Users\Ikeda\Downloads\test.csv")

# NO PYTHON DO COLLAB TEM O ESQUEMA !!!
# CARREGA O ARQUIVO DO LADO ESQUERDO OU NO GOOGLE DRIVE ANTES !!!
# DAI FUNFA !!!
# ARQUIVO DIRETO AO IMPORTAR DO LADO ESQUERDO EM "UPLOAD"
#titanic = pd.read_csv("test.csv")
# GOOGLE DRIVE (EXEMPLO DE URL)
#titanic = pd.read_csv('https://drive.google.com/open?id=1DPZZQ43w8brRhbEMolgLqOWKbZbE-IQu')

# OU COLOCA O SITE DO ARQUIVO QUE VAI TAMBÉM
# DADOS DE TESTE VIU !!!
#titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# INPUT DE DADOS DIRETO DAQUI DO KAGGLE (ADICIONADO DA PÁGINA OFICIAL DO DESAFIO)
file = "test"
titanic = pd.read_csv("../input/titanic/" + file + ".csv")
titanic.head()

