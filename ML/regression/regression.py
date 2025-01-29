import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def evaluate_model(model, x, y):
    y_pred = model.predict(x)
    return {
        'r2_score': r2_score(y, y_pred),
        'mse': mean_squared_error(y, y_pred),
        'mae': mean_absolute_error(y, y_pred)
    }

x_data = pd.read_csv('6_x.csv')
y_data = pd.read_csv('6_y.csv')

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)
metrics = {}

for idx, feature in enumerate(x_train.columns):
    model = LinearRegression()
    model.fit(x_train[[feature]], y_train)
    metrics[f'linear_{idx}'] = evaluate_model(model, x_test[[feature]], y_test)


multiple_linear_model = LinearRegression()
multiple_linear_model.fit(x_train, y_train)
metrics['multiple_linear'] = evaluate_model(multiple_linear_model, x_test, y_test)

for idx, feature in enumerate(x_train.columns):
    for degree in [2, 3]:
        poly = PolynomialFeatures(degree=degree)
        x_train_poly = poly.fit_transform(x_train[[feature]])
        x_test_poly = poly.transform(x_test[[feature]])
        model = LinearRegression()
        model.fit(x_train_poly, y_train)
        metrics[f'{idx}_degree_{degree}'] = evaluate_model(model, x_test_poly, y_test)

metrics_df = pd.DataFrame(metrics).T
metrics_df.to_csv('metrics.csv')