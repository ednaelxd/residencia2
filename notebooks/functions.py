import pandas as pd
import glob
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def concatenador(path):
    path = path
    filenames = glob.glob(path + "/*.csv")

    li= []

    for filename in filenames:
        df = pd.read_csv(filename, index_col=None, header=0, encoding='latin-1',sep=';',decimal=',')
        li.append(df)

    df2 = pd.concat(li, axis=0, ignore_index=True)
    
    return (df2)


#varre todos o objetos e identifica se possui relacao com obras
#Define como obra ou nao
def eh_obra(x):
    y=[]
    if ('OBRAS' in x) or ('OBRA' in x) or ('ENGENHARIA' in x) or
    ('engenharia' in x) or ('obras' in x) or ('obra' in x) or
    ('CONTRU-CAO' in x) or ('constru-cao' in x):
        y.append('OBRAS')
    else:
        y.append('COMPRA/SERVIÇOS')
    y=y.pop(0)
    return(y)

#aplica a função de descobrimento de obras de forma mais rápida no dataframe
def separaObra(df2):
    return pd.Series(eh_obra(row.Objeto)
        for row in df2.itertuples()
  )

#FOR THE CLUSTERS ANALISES
def bench_k_means(kmeans, name, data, labels):
    """Benchmark to evaluate the KMeans initialization methods.

    Parameters
    ----------
    kmeans : KMeans instance
        A :class:`~sklearn.cluster.KMeans` instance with the initialization
        already set.
    name : str
        Name given to the strategy. It will be used to show the results in a
        table.
    data : ndarray of shape (n_samples, n_features)
        The data to cluster.
    labels : ndarray of shape (n_samples,)
        The labels used to compute the clustering metrics which requires some
        supervision.
    """
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # Define the metrics which require only the true labels and estimator
    # labels
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # The silhouette score requires the full dataset
    results += [
        metrics.silhouette_score(
            data,
            estimator[-1].labels_,
            metric="euclidean",
            sample_size=300,
        )
    ]

    # Show the results
    formatter_result = (
        "{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}"
    )
    print(formatter_result.format(*results))
    
  