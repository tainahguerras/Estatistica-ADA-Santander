import matplotlib.pyplot as plt
import seaborn as sns

def create_histogram(data, title = '', xlabel = '', ylabel = '', size = (8,4)):
    
    ax = sns.histplot(x=data, bins=20, kde=True, color='#8e7cc3')

    ax.figure.set_size_inches(size)
    ax.set_title(title , fontsize=12)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax

def create_violin_boxplot(data, title, ylabel, color='#8e7cc3', size = (8,4)):

    fig, axs = plt.subplots(1, 2, figsize = size, sharey=True)

    sns.boxplot(data, color=color, linewidth=2, ax=axs[0])
    axs[0].set_title(title)
    axs[0].set_ylabel(ylabel, fontsize=11)

    sns.violinplot(data,color=color,linewidth=3)
    axs[1].set_ylabel(ylabel, fontsize=11)

    plt.tight_layout()
    plt.show()