"""
Proyecto: Impacto de la Inteligencia Artificial y las Redes Sociales en la Salud y el Rendimiento Academico de Estudiantes
Manuel Alcaraz Baltazar 
Fecha: Octubre 2026
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. CONFIGURACION DE ENTORNO Y ESTILO
# ==========================================
sns.set_theme(style='whitegrid')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# ==========================================
# 2. CARGA DEL CONJUNTO DE DATOS
# ==========================================
csv_filename = 'AI_SocialMedia_Student_Health_Dataset_clean.csv'

if not os.path.exists(csv_filename):
    alt_paths = [
        os.path.join('AI SALUD', csv_filename),
        os.path.join('..', csv_filename),
        r'c:\Users\Manuel\Documents\BigDatayDataMining\AI SALUD\AI_SocialMedia_Student_Health_Dataset_clean.csv',
        r'c:\Users\Manuel\Documents\BigDatayDataMining\AI_SocialMedia_Student_Health_Dataset_clean.csv'
    ]
    for p in alt_paths:
        if os.path.exists(p):
            csv_filename = p
            break

student_df = pd.read_csv(csv_filename)
print(f"Dataset cargado exitosamente. Dimensiones: {student_df.shape[0]} filas x {student_df.shape[1]} columnas\n")

# ==========================================
# 3. ANALISIS EXPLORATORIO INICIAL (EDA)
# ==========================================
print("--- PRIMEROS 6 REGISTROS ---")
print(student_df.head(6))

print("\n--- ULTIMOS 6 REGISTROS ---")
print(student_df.tail(6))

print("\n--- INFORMACION ESTRUCTURAL DEL DATASET ---")
student_df.info()

print("\n--- RESUMEN ESTADISTICO NUMERICO ---")
print(student_df.describe())

print("\n--- RESUMEN ESTADISTICO CATEGORICO ---")
print(student_df.describe(include='object'))

print("\n--- VALORES NULOS POR COLUMNA ---")
print(student_df.isnull().sum())

print("\n--- VERIFICACION DE DUPLICADOS ---")
print("Registros completos duplicados:", student_df.duplicated().sum())
print("Student_IDs duplicados:", student_df['Student_ID'].duplicated().sum())

print("\n--- DISTRIBUCION DE LA VARIABLE OBJETIVO (Academic_Failure_Risk) ---")
print("Conteo absoluto:")
print(student_df['Academic_Failure_Risk'].value_counts())
print("\nPorcentaje (%):")
print(student_df['Academic_Failure_Risk'].value_counts(normalize=True) * 100)

print("\n--- DISTRIBUCION DE VARIABLES CATEGORICAS ---")
print("Genero:\n", student_df['Gender'].value_counts())
print("\nNivel Educativo:\n", student_df['Education_Level'].value_counts())
print("\nNivel de Agotamiento:\n", student_df['Burnout_Level'].value_counts())

# ==========================================
# 4. MAPEO DE VARIABLES AL ESPANOL
# ==========================================
var_names_es = {
    'Age': 'Edad (años)',
    'Daily_Social_Media_Hours': 'Horas en redes sociales',
    'Daily_AI_Tool_Usage_Hours': 'Horas con herramientas de IA',
    'Sleep_Hours': 'Horas de sueño',
    'Physical_Activity_Hours': 'Horas de actividad física',
    'Mental_Health_Score': 'Salud mental',
    'Physical_Health_Score': 'Salud física',
    'Social_Isolation_Score': 'Aislamiento social',
    'Academic_Performance_Score': 'Rendimiento académico',
    'Academic_Failure_Risk': 'Riesgo de reprobación'
}

burnout_es = {
    'Low': 'Bajo',
    'Moderate': 'Moderado',
    'High': 'Alto',
    'Severe': 'Severo'
}

# ==========================================
# 5. VISUALIZACIONES CLAVE (FIGURAS 1 A 5)
# ==========================================

# FIGURA 1: Distribucion del riesgo y nivel de agotamiento
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.countplot(x='Academic_Failure_Risk', data=student_df, ax=axes[0], color='gray', edgecolor='black')
axes[0].set_title('Riesgo de reprobación', fontsize=12)
axes[0].set_xlabel('Riesgo (0: Sin riesgo, 1: En riesgo)')
axes[0].set_ylabel('Estudiantes')

orden_burnout = ['Low', 'Moderate', 'High', 'Severe']
sns.countplot(x='Burnout_Level', data=student_df, order=orden_burnout, ax=axes[1], color='silver', edgecolor='black')
axes[1].set_title('Nivel de agotamiento', fontsize=12)
axes[1].set_xlabel('Nivel de agotamiento (Low, Moderate, High, Severe)')
axes[1].set_ylabel('Estudiantes')

plt.suptitle('Figura 1. Distribución del riesgo de reprobación y del nivel de agotamiento', fontsize=13, y=1.02)
plt.tight_layout()
plt.show()

# FIGURA 2: Histogramas de variables cuantitativas
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
variables_hist = [
    ('Daily_Social_Media_Hours', 'Horas en redes sociales'),
    ('Daily_AI_Tool_Usage_Hours', 'Horas con herramientas de IA'),
    ('Sleep_Hours', 'Horas de sueño'),
    ('Mental_Health_Score', 'Puntaje de salud mental'),
    ('Academic_Performance_Score', 'Rendimiento académico'),
    ('Social_Isolation_Score', 'Aislamiento social')
]

for ax, (col, nombre) in zip(axes.flatten(), variables_hist):
    media = student_df[col].mean()
    desv = student_df[col].std()
    ax.hist(student_df[col], bins=30, color='gray', edgecolor='black', alpha=0.7)
    ax.set_title(f"{nombre}\nMedia: {media:.2f} | Desv. Est.: {desv:.2f}", fontsize=11)
    ax.set_xlabel('Valor')
    ax.set_ylabel('Frecuencia')

plt.suptitle('Figura 2. Distribución de variables numéricas seleccionadas', fontsize=13, y=1.02)
plt.tight_layout()
plt.show()

# FIGURA 3: Matriz de correlaciones de Pearson
plt.figure(figsize=(10, 8))
correlations = student_df.corr(numeric_only=True, method='pearson')
sns.heatmap(correlations, annot=True, fmt='.2f', cmap='Greys', vmin=-1, vmax=1)
plt.title('Figura 3. Matriz de correlaciones entre variables numéricas', fontsize=13, pad=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print("\n--- CORRELACION CON EL RIESGO DE REPROBACION ---")
print(correlations['Academic_Failure_Risk'].sort_values().to_frame(name='Correlacion'))

# FIGURA 4: Diagramas de caja comparativos (Boxplots)
fig, axes = plt.subplots(1, 4, figsize=(16, 4.5))
variables_box = [
    ('Daily_Social_Media_Hours', 'Horas en redes sociales'),
    ('Sleep_Hours', 'Horas de sueño'),
    ('Mental_Health_Score', 'Salud mental'),
    ('Academic_Performance_Score', 'Rendimiento académico')
]

for ax, (col, nombre) in zip(axes, variables_box):
    sns.boxplot(x='Academic_Failure_Risk', y=col, data=student_df, ax=ax, color='lightgray')
    ax.set_title(nombre, fontsize=11)
    ax.set_xlabel('Riesgo de reprobación')
    ax.set_ylabel(nombre)

plt.suptitle('Figura 4. Comparación de variables clave entre estudiantes sin riesgo y en riesgo', fontsize=13, y=1.03)
plt.tight_layout()
plt.show()

# FIGURA 5: Barras apiladas (Stacked Bar) de riesgo por nivel de agotamiento
burnout_risk_stacked = pd.crosstab(
    student_df['Burnout_Level'],
    student_df['Academic_Failure_Risk'],
    normalize='index'
) * 100
burnout_risk_stacked = burnout_risk_stacked.reindex(['Low', 'Moderate', 'High', 'Severe'])

burnout_risk_stacked.plot(kind='bar', stacked=True, figsize=(8, 5), color=['#d3d3d3', '#333333'], edgecolor='black')
plt.title('Figura 5. Proporción de estudiantes en riesgo según su nivel de agotamiento', fontsize=12, pad=10)
plt.xlabel('Nivel de agotamiento (Burnout Level)')
plt.ylabel('% de estudiantes')
plt.ylim(0, 105)
plt.xticks(rotation=0)
plt.legend(['Sin riesgo (0)', 'En riesgo (1)'], title='Condición')
plt.tight_layout()
plt.show()

# ==========================================
# 6. TABLAS ESTADISTICAS Y OUTLIERS (IQR)
# ==========================================

# TABLA 2: Estadisticas descriptivas
columnas_num = [
    'Age', 'Daily_Social_Media_Hours', 'Daily_AI_Tool_Usage_Hours', 'Sleep_Hours',
    'Physical_Activity_Hours', 'Mental_Health_Score', 'Physical_Health_Score',
    'Social_Isolation_Score', 'Academic_Performance_Score'
]

tabla_2 = pd.DataFrame({
    'Media': student_df[columnas_num].mean(),
    'Desv. estándar': student_df[columnas_num].std(),
    'Mínimo': student_df[columnas_num].min(),
    'Mediana': student_df[columnas_num].median(),
    'Máximo': student_df[columnas_num].max()
})
print("\n--- TABLA 2: ESTADISTICAS DESCRIPTIVAS ---")
print(tabla_2.round(2))

# TABLA 3: Promedios segun el riesgo de reprobacion
columnas_t3 = [
    'Daily_Social_Media_Hours', 'Daily_AI_Tool_Usage_Hours', 'Sleep_Hours',
    'Physical_Activity_Hours', 'Mental_Health_Score', 'Physical_Health_Score',
    'Social_Isolation_Score', 'Academic_Performance_Score'
]
tabla_3 = student_df.groupby('Academic_Failure_Risk')[columnas_t3].mean().T
tabla_3.columns = ['Sin riesgo (14,100)', 'En riesgo (900)']
print("\n--- TABLA 3: PROMEDIOS SEGUN EL RIESGO DE REPROBACION ---")
print(tabla_3.round(2))

# DETECCION DE OUTLIERS CON METODO IQR
print("\n--- DETECCION DE VALORES ATIPICOS (METODO IQR) ---")
num_df = student_df.select_dtypes('number')
for c in num_df.columns.drop('Academic_Failure_Risk'):
    q1, q3 = num_df[c].quantile([0.25, 0.75])
    iqr = q3 - q1
    n = ((num_df[c] < q1 - 1.5 * iqr) | (num_df[c] > q3 + 1.5 * iqr)).sum()
    print(f"{c}: {n} valores atípicos")

# ==========================================
# 7. TABLAS ADICIONALES (ANEXO B)
# ==========================================
print("\n--- TABLA B3: RIESGO DE REPROBACION POR GRUPO (%) ---")
print("Por Genero:\n", (student_df.groupby('Gender')['Academic_Failure_Risk'].mean() * 100).round(1))
print("\nPor Nivel Educativo:\n", (student_df.groupby('Education_Level')['Academic_Failure_Risk'].mean() * 100).round(1))
print("\nPor Nivel de Agotamiento:\n", (student_df.groupby('Burnout_Level')['Academic_Failure_Risk'].mean() * 100).round(1))

print("\nAnalisis finalizado exitosamente.")
