# prediction/forms.py
from django import forms

# Formulario para ingresar múltiples casos de predicción
class CancerForm(forms.Form):
    case_1 = forms.CharField(label='Caso 1 (30 valores separados por comas)')
    case_2 = forms.CharField(label='Caso 2 (opcional, 30 valores separados por comas)', required=False)
    case_3 = forms.CharField(label='Caso 3 (opcional, 30 valores separados por comas)', required=False)
