import matplotlib.pyplot as plt
import seaborn as sns

def create_histogram(data, title = '', xlabel = '', ylabel = '', size = (8,4)):
    
    ax = sns.histplot(x=data, bins=20, kde=True, color='#8e7cc3')

    ax.figure.set_size_inches(size)
    ax.set_title(title , fontsize=14)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax

def plot_violin_boxplot(dados, titulo, xlabel, ylabel, cor='#8e7cc3'):

    fig, axs = plt.subplots(1, 2, figsize=(12, 8))

    sns.boxplot(x=dados, color=cor, ax=axs[0])
    axs[0].set_title(titulo)
    axs[0].set_xlabel(xlabel)
    axs[0].set_ylabel(ylabel)

    sns.violinplot(x=dados,color=cor,linewidth=3)
    axs[1].set_xlabel(xlabel)
    axs[1].set_ylabel(ylabel)

    plt.tight_layout()
    plt.show()