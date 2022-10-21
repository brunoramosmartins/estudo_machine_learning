import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

# Exemplo do livro p.22 (Aprendizado de Máquina com Scikit-Learn)

# Carregue os dados
oecd_bli = pd.read_csv('oecd_bli_2015.csv', thousands= ',')
gdp_per_capita = pd.read_csv('gdp_per_capita.csv', thousands= ',', delimiter = '\t', encoding = 'latin1', na_values = 'n/a')

# Prepare os dados
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_[country_stats['GDP per capita']]
y = np.c_[country_stats['Life satisfaction']]

# Visualize os dados
country_stats.plot(kind='scatter', x='GDP per capita', y = 'Life satisfaction')
plt.show()
