import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def configure_plot_style(font_size: int = 14):
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['ps.fonttype'] = 42
    plt.rcParams.update({'font.size': font_size})
    plt.rcParams["figure.figsize"] = (10, 7)

# Plot PCA latent space colored by player position ( and can be colord by league) 
def plot_pca(df: pd.DataFrame, x_col='Latent_Dim1', y_col='Latent_Dim2', hue='Position_Label'):
    plt.figure()
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, palette='Set2', s=100)
    plt.title("PCA - Latent Space Colored by Position")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend(title=hue)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Plot t-SNE latent space colored by player position ( and can be colord by league) 
def plot_tsne(df: pd.DataFrame, x_col='TSNE_Dim1', y_col='TSNE_Dim2', hue='Position_Label'):
    plt.figure()
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, palette='tab10', s=100)
    plt.title("t-SNE - Latent Space Colored by Position")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend(title=hue)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

