from sklearn.datasets import load_digits
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV

wine = load_digits()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target, name='target')
print(X.head())
print(y.value_counts())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "SVM": SVC(),
    "KNN": KNeighborsClassifier(),
    "Random Forest": RandomForestClassifier()
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    results[name] = y_pred

for name, pred in results.items():
    print(f"{name}:")
    print(classification_report(y_test, pred))

param_grid = {
    'C': [0.1, 1, 10, 100],  # Регуляризация
    'kernel': ['linear', 'rbf', 'poly'],  # Тип ядра
    'gamma': ['scale', 'auto', 0.001, 0.01, 0.1],  # Коэффициент ядра
    'degree': [2, 3, 4],  # Степень полиномиального ядра (только для 'poly')
    'coef0': [0.0, 0.1, 0.5]  # Независимый член (для 'poly' и 'sigmoid')
}

grid_search = GridSearchCV(models['SVM'], param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
print("Лучшие параметры:", grid_search.best_params_)
print("Лучшая точность:", grid_search.best_score_)
best_rf_model = grid_search.best_estimator_
best_rf_predictions = best_rf_model.predict(X_test)
print("Отчет по классификации для лучшей модели:\n", classification_report(y_test, best_rf_predictions))
