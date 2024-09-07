import numpy as np
import joblib
from django.shortcuts import render

# Cargar el modelo
modelo_path = 'prediction/modelos/breast_cancer_model.pkl'
modelo = joblib.load(modelo_path)

def cancer_prediction(request):
    if request.method == 'POST':
        # Recolectar datos para los dos pacientes
        pacientes = []
        for i in range(1, 3):
            concave_points_worst = float(request.POST.get(f'concave_points_worst_{i}', 0))
            concave_points_mean = float(request.POST.get(f'concave_points_mean_{i}', 0))
            perimeter_worst = float(request.POST.get(f'perimeter_worst_{i}', 0))
            concavity_mean = float(request.POST.get(f'concavity_mean_{i}', 0))
            radius_worst = float(request.POST.get(f'radius_worst_{i}', 0))
            area_worst = float(request.POST.get(f'area_worst_{i}', 0))

            paciente = [concave_points_worst, concave_points_mean, perimeter_worst, concavity_mean, radius_worst, area_worst]
            pacientes.append(paciente)

        # Convertir la lista a un array numpy
        pacientes_np = np.array(pacientes)

        # Realizar predicciones utilizando el modelo
        predicciones = modelo.predict_proba(pacientes_np)

        # Preparar los resultados para mostrar en la plantilla
        resultados = []
        for idx, prediccion in enumerate(predicciones):
            resultado = {
                "Paciente": f"Paciente {idx + 1}",
                "Probabilidad_de_Benigno": prediccion[0],
                "Probabilidad_de_Maligno": prediccion[1]
            }
            resultados.append(resultado)

        return render(request, 'prediction/cancer_prediction.html', {'resultados': resultados})

    return render(request, 'prediction/cancer_prediction.html')
