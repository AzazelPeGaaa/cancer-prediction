import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Obtener la ruta del directorio del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Cargar el archivo CSV
data = pd.read_csv(os.path.join(BASE_DIR, 'Breast_Cancer_Wisconsin.csv'))

# Eliminar la columna 'id' porque no es relevante para el modelo
data = data.drop(labels=['id'], axis=1)

# Convertir la columna 'diagnosis' a binario: Maligno (M) = 1, Benigno (B) = 0
data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

# Utilizar solo las 6 características más importantes
X = data[['concave points_worst', 'concave points_mean', 'perimeter_worst',
          'concavity_mean', 'radius_worst', 'area_worst']]

# La columna 'diagnosis' es nuestra etiqueta
y = data['diagnosis']

# Dividir los datos en entrenamiento y prueba (70% entrenamiento, 30% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar un modelo de RandomForest
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Crear la carpeta 'modelos' si no existe
modelos_dir = os.path.join(BASE_DIR, 'modelos')
if not os.path.exists(modelos_dir):
    os.makedirs(modelos_dir)

# Guardar el modelo entrenado
modelo_path = os.path.join(modelos_dir, 'breast_cancer_model.pkl')
joblib.dump(modelo, modelo_path)

print("Modelo reentrenado y guardado.")
