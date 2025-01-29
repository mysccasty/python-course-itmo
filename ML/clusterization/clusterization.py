import pandas as pd
import warnings
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, AgglomerativeClustering, SpectralClustering, DBSCAN, Birch, MeanShift
from sklearn.metrics import (
    silhouette_score,
    adjusted_rand_score,
    homogeneity_score,
    v_measure_score,
    fowlkes_mallows_score
)

warnings.filterwarnings("ignore")
# Загрузка датасета
digits = load_iris()
data = pd.DataFrame(digits.data)
data['target'] = digits.target

# Стандартизация данных
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data.drop('target', axis=1))

# Метрики для оценки
def evaluate_clustering(true_labels, predicted_labels, data_scaled):
    print("Adjusted Rand Index (ARI):", adjusted_rand_score(true_labels, predicted_labels))
    print("Silhouette Score:", silhouette_score(data_scaled, predicted_labels))
    print("Homogeneity Score:", homogeneity_score(true_labels, predicted_labels))
    print("V-measure Score:", v_measure_score(true_labels, predicted_labels))
    print("Fowlkes-Mallows Index (FMI):", fowlkes_mallows_score(true_labels, predicted_labels))
    print("-" * 60)

# K-means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(data_scaled)
print("K-means Results:")
evaluate_clustering(data['target'], kmeans_labels, data_scaled)

# Agglomerative Clustering
agglo = AgglomerativeClustering(n_clusters=3)
agglo_labels = agglo.fit_predict(data_scaled)
print("Agglomerative Clustering Results:")
evaluate_clustering(data['target'], agglo_labels, data_scaled)

# Spectral Clustering
spectral = SpectralClustering(n_clusters=3, random_state=42)
spectral_labels = spectral.fit_predict(data_scaled)
print("Spectral Clustering Results:")
evaluate_clustering(data['target'], spectral_labels, data_scaled)

# DBSCAN
dbscan = DBSCAN()
dbscan_labels = dbscan.fit_predict(data_scaled)
print("DBSCAN Results:")
evaluate_clustering(data['target'], dbscan_labels, data_scaled)

# Birch
birch = Birch(n_clusters=3)
birch_labels = birch.fit_predict(data_scaled)
print("Birch Results:")
evaluate_clustering(data['target'], birch_labels, data_scaled)

# Mean Shift
meanshift = MeanShift()
meanshift_labels = meanshift.fit_predict(data_scaled)
print("Mean Shift Results:")
evaluate_clustering(data['target'], meanshift_labels, data_scaled)

param_grid = {
    'n_clusters': [3],
    'threshold': [0.1, 0.3, 0.5, 0.7, 1.0],
    'branching_factor': [25, 50, 100, 150]
}

# Модель Birch
birch = Birch()

# Поиск лучших параметров
grid_search = GridSearchCV(birch, param_grid, scoring='adjusted_rand_score', cv=3)
grid_search.fit(data_scaled)

# Лучшие параметры и результат
print("Лучшие параметры:", grid_search.best_params_)

# Использование лучшей модели
best_birch = grid_search.best_estimator_
birch_labels = best_birch.fit_predict(data_scaled)

# Оценка качества
print("Birch Results после настройки:")
evaluate_clustering(data['target'], birch_labels, data_scaled)
