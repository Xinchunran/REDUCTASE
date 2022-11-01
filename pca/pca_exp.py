from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd

def pca_analysis(xs: float, componets: int):
    pca = PCA(componets)
    xs_pca =  pca.fit_transform(xs)
    return xs_pca

def fig_pca(xs_data: float, ys_data: float):
    fig_dims = (7, 6)
    fig, ax = plt.subplots(figsize=fig_dims)
    sc = ax.scatter(xs_data[:,0], xs_data[:,1], c=ys_data, marker='.')
    ax.set_xlabel('PCA first principal component')
    ax.set_ylabel('PCA second principal component')
    plt.colorbar(sc, label='two components')
    plt.savefig("./pca_analysis.pdf", format="pdf")
    return print("analyzing the pca")

def main():
    data = pd.read_csv("./iris.csv")
    xs = data.iloc[:,0:4]
    ys = data.iloc[:, -1]
    pca_xs = pca_analysis(xs, 2)
    fig_pca(pca_xs, ys)



if __name__ == "__main__":
    main()
