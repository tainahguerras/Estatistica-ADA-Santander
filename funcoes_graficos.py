import matplotlib.pyplot as plt
import seaborn as sns

def cria_histograma(dados, titulo = '', xlabel = '', ylabel = ''):
    
    sns.histplot(x=dados, bins=20, kde=True, color='#8e7cc3')

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def cria_boxplot(dados, titulo = '', xlabel = '', ylabel = ''):

    sns.boxplot(y=dados, color='#8e7cc3')

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def cria_pairplot(dados, hue=None):

    if hue is None:
        sns.pairplot(dados,
                kind='reg',
                plot_kws={'ci': None, 
                        'scatter_kws': {'color': '#ADD8E6', 's': 3}})
    else:
        sns.pairplot(dados, hue=hue,
                     kind='reg',
                     plot_kws={'ci': None, 
                               'scatter_kws': {'color': '#ADD8E6', 's': 3}})
    
    plt.show()