# 📊 Impacto de la Inteligencia Artificial y las Redes Sociales en la Salud y el Rendimiento Académico de Estudiantes

> **Facultad de Telemática — Universidad de Colima**  
> **Carrera:** Ingeniería de Software  
> **Materia:** Optativa — Big Data y Data Mining  
> **Alumno:** Manuel Alcaraz Baltazar (7H)  
> **Docente:** Dr. Juan Antonio Guerrero Ibañez  
> **Fecha:** Octubre 2026  

---

## 📑 Tabla de Contenidos
1. [Resumen Ejecutivo y Justificación](#1-resumen-ejecutivo-y-justificación)
2. [Descripción del Conjunto de Datos](#2-descripción-del-conjunto-de-datos)
3. [Traducción y Mapeo de Variables al Español](#3-traducción-y-mapeo-de-variables-al-español)
4. [Metodología de Análisis Exploratorio (EDA)](#4-metodología-de-análisis-exploratorio-eda)
5. [Visualizaciones Clave del Proyecto](#5-visualizaciones-clave-del-proyecto)
6. [Tablas Estadísticas Oficiales y Análisis de Outliers (IQR)](#6-tablas-estadísticas-oficiales-y-análisis-de-outliers-iqr)
7. [Hallazgos Clave y Alertas Metodológicas](#7-hallazgos-clave-y-alertas-metodológicas)
8. [Plan de Mejora y Recomendaciones](#8-plan-de-mejora-y-recomendaciones)
   - [Para el Alumnado](#a-recomendaciones-prácticas-para-el-alumnado)
   - [Para la Institución Educativa](#b-recomendaciones-para-la-institución-educativa)
9. [Valor Técnico y Competencias Adquiridas](#9-valor-técnico-y-competencias-adquiridas)
10. [Instrucciones de Instalación y Ejecución](#10-instrucciones-de-instalación-y-ejecución)

---

## 1. Resumen Ejecutivo y Justificación

En los últimos años, la adopción masiva de herramientas de **Inteligencia Artificial Generativa** y el consumo intensivo de **redes sociales** han transformado radicalmente la rutina de los estudiantes. Si bien estas tecnologías ofrecen facilidades para la investigación y la comunicación, el uso desmedido suele desplazar hábitos fundamentales para el bienestar, tales como el sueño reparador, la actividad física y la convivencia presencial.

### 🎯 Objetivo General
Desarrollar un análisis analítico y exploratorio riguroso sobre los hábitos digitales y de salud de los estudiantes para identificar patrones asociados al **riesgo de reprobación académica** (`Academic_Failure_Risk`), permitiendo la construcción de futuros modelos predictivos y el diseño de estrategias preventivas oportunas.

### ❓ Preguntas de Investigación
1. ¿Qué hábitos digitales y de bienestar correlacionan con mayor fuerza con el riesgo de reprobar?
2. ¿Qué diferencias cuantitativas existen entre los estudiantes en riesgo y aquellos sin riesgo?
3. ¿El nivel de agotamiento (*Burnout*) es un predictor temprano o representa una señal de colapso inminente (*Data Leakage*)?
4. ¿Existen diferencias significativas de riesgo entre géneros o niveles educativos?

---

## 2. Descripción del Conjunto de Datos

El conjunto de datos utilizado proviene del repositorio público de Kaggle: [AI and Social Media Impact: Student Health and Grades](https://www.kaggle.com/datasets/debayank2024/ai-and-social-media-impact-student-health-and-grades), publicado por Debayan Bandyopadhyay.

* **Registros:** 15,000 estudiantes únicos.
* **Variables:** 14 columnas (1 identificador, 9 numéricas y 4 categóricas).
* **Calidad:** 100% libre de valores nulos (`0 nulls`) y sin registros duplicados.

### 📋 Diccionario de Variables (Tabla 1)

| Variable Original | Tipo de Dato | Variable en Español | Qué Representa |
| :--- | :---: | :--- | :--- |
| `Student_ID` | Texto / ID | Identificador del estudiante | Código alfanumérico único por alumno (`STU_00001` a `STU_15000`). |
| `Age` | Entero | Edad | Edad en años cumplidos (rango de 13 a 25 años). |
| `Gender` | Categórica | Género | Identidad registrada: *Male* (Masculino), *Female* (Femenino), *Non-binary* (No binario). |
| `Education_Level` | Categórica | Nivel Escolar | Nivel académico: *High School* (Bachillerato), *College* (Nivel Intermedio), *University* (Universidad). |
| `Daily_Social_Media_Hours` | Decimal | Horas en redes sociales | Promedio de horas diarias dedicadas a redes sociales (0 a 14 hrs). |
| `Daily_AI_Tool_Usage_Hours` | Decimal | Horas con herramientas de IA | Promedio de horas diarias con herramientas de IA (0 a 9.5 hrs). |
| `Sleep_Hours` | Decimal | Horas de sueño | Horas promedio de sueño por noche (2.0 a 11.15 hrs). |
| `Physical_Activity_Hours` | Decimal | Horas de actividad física | Horas promedio diarias dedicadas a ejercicio/deporte (0 a 5.0 hrs). |
| `Mental_Health_Score` | Decimal | Puntaje de salud mental | Escala de bienestar psicológico de 0 a 100 (mayor puntaje = mejor salud). |
| `Physical_Health_Score` | Decimal | Puntaje de salud física | Escala de bienestar físico de 0 a 100 (mayor puntaje = mejor salud). |
| `Social_Isolation_Score` | Decimal | Aislamiento social | Nivel percibido de aislamiento de 1 a 10 (mayor puntaje = mayor aislamiento). |
| `Burnout_Level` | Categórica | Nivel de agotamiento | Nivel de fatiga académica: *Low* (Bajo), *Moderate* (Moderado), *High* (Alto), *Severe* (Severo). |
| `Academic_Performance_Score` | Decimal | Rendimiento académico | Calificación promedio del estudiante en escala de 0 a 100. |
| `Academic_Failure_Risk` | Binaria (0/1) | **Riesgo de reprobación (Target)** | Variable objetivo: **0 = Sin riesgo**, **1 = En riesgo de reprobar**. |

---

## 3. Traducción y Mapeo de Variables al Español

### 💡 Justificación Técnica y Pedagógica
Aunque los conjuntos de datos profesionales suelen estructurarse con nombres de columnas en inglés por convención de bases de datos, **la presentación de resultados analíticos a tomadores de decisiones, directivos escolares y docentes requiere que las visualizaciones y reportes sean inmediatamente legibles en español**, sin ambigüedades técnicas.

### 🛠️ Implementación en Código
Para mantener la integridad del DataFrame original y al mismo tiempo generar figuras y tablas comprensibles, se aplicó un mapeo mediante diccionarios y transformaciones ordenadas en **Pandas**:

```python
# 1. Diccionario de mapeo de nombres de variables al español
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

# 2. Mapeo ordinal para el nivel de agotamiento
burnout_map = {
    'Low': 'Bajo',
    'Moderate': 'Moderado',
    'High': 'Alto',
    'Severe': 'Severo'
}
```

Este enfoque garantizó que los gráficos generados con `matplotlib.pyplot` y `seaborn` mostraran títulos, ejes y etiquetas de categorías en español con precisión y orden lógico.

---

## 4. Metodología de Análisis Exploratorio (EDA)

Siguiendo las mejores prácticas vistas en la práctica de clase (*Tipos de Clima*):
1. **Inspección estructural:** Verificación de tipos con `df.info()`, dimensiones con `df.shape` y primeros/últimos registros con `head()` y `tail()`.
2. **Evaluación de calidad e integridad:** Comprobación de nulos con `df.isnull().sum()` y validación visual mediante `sns.heatmap(df.isnull(), cmap='Reds')`.
3. **Análisis univariado:** Conteo y proporciones de frecuencias con `value_counts()` y `countplot()`.
4. **Análisis de dispersión y distribución:** Histogramas de variables cuantitativas con cálculo dinámico de medias ($\mu$) y desviaciones estándar ($\sigma$).
5. **Análisis bivariado y multivariado:** Matriz de correlación de Pearson y diagramas de caja (*Boxplots*) condicionados por la variable objetivo.
6. **Detección no paramétrica de valores atípicos:** Aplicación de la regla del Rango Intercuartílico ($IQR$).

---

## 5. Visualizaciones Clave del Proyecto

El cuaderno incluye el código ejecutable para generar las 5 figuras centrales del reporte de avance:

### 🔹 Figura 1. Distribución del riesgo de reprobación y del nivel de agotamiento
* **Objetivo:** Visualizar el desbalance de clases y la distribución de la fatiga estudiantil.
* **Técnica:** `sns.countplot` en subplots de 1 fila × 2 columnas.
* **Hallazgo:** Muestra el marcado desbalance donde el **94.0% (14,100)** de los alumnos no está en riesgo y solo el **6.0% (900)** sí lo está. El agotamiento disminuye progresivamente: Bajo (60.0%), Moderado (28.0%), Alto (9.0%) y Severo (3.0%).

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.countplot(x='Academic_Failure_Risk', data=student_df, ax=axes[0], color='gray', edgecolor='black')
sns.countplot(x='Burnout_Level', data=student_df, order=['Low', 'Moderate', 'High', 'Severe'], ax=axes[1], color='silver', edgecolor='black')
```

---

### 🔹 Figura 2. Distribución de variables numéricas seleccionadas (Histogramas)
* **Objetivo:** Analizar la forma, simetría y dispersión de las 6 variables cuantitativas centrales.
* **Técnica:** Cuadrícula de $2 \times 3$ con `ax.hist(bins=30)` calculando media y desviación estándar en el título de cada gráfico.
* **Hallazgo:** Todas las variables siguen distribuciones acampanadas y continuas dentro de rangos biológica y académicamente consistentes.

```python
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
for ax, (col, nombre) in zip(axes.flatten(), variables_hist):
    media, desv = student_df[col].mean(), student_df[col].std()
    ax.hist(student_df[col], bins=30, color='gray', edgecolor='black', alpha=0.7)
    ax.set_title(f"{nombre}\nMedia: {media:.2f} | Desv. Est.: {desv:.2f}")
```

---

### 🔹 Figura 3. Matriz de correlaciones entre variables numéricas
* **Objetivo:** Identificar el grado de asociación lineal entre las 10 características numéricas.
* **Técnica:** `student_df.corr(numeric_only=True, method='pearson')` visualizado con `sns.heatmap(annot=True, fmt='.2f', cmap='Greys')`.
* **Hallazgo:** El riesgo de reprobación se asocia negativamente con la **salud mental ($-0.36$)**, el **rendimiento previo ($-0.30$)** y el **sueño ($-0.24$)**; y positivamente con las **redes sociales ($+0.33$)** y el **aislamiento ($+0.23$)**. La edad no tiene impacto ($+0.01$).

---

### 🔹 Figura 4. Comparación de variables clave entre estudiantes sin riesgo y en riesgo (Boxplots)
* **Objetivo:** Comparar la mediana, dispersión intercuartílica y valores atípicos de los grupos $0$ y $1$.
* **Técnica:** 4 diagramas de caja con `sns.boxplot(x='Academic_Failure_Risk', y=col, data=student_df)`.
* **Hallazgo:** Los estudiantes en riesgo presentan medianas visiblemente desplazadas: duermen menos de 5.5 horas, superan las 7.5 horas de redes sociales y sufren una fuerte caída en salud mental y rendimiento.

---

### 🔹 Figura 5. Proporción de estudiantes en riesgo según su nivel de agotamiento (Barras Apiladas)
* **Objetivo:** Cuantificar la tasa de reprobación en cada estadio de agotamiento.
* **Técnica:** `pd.crosstab(..., normalize='index') * 100` y graficado mediante `.plot(kind='bar', stacked=True)`.
* **Hallazgo:**
  * **Agotamiento Bajo:** 100% Sin riesgo, 0% En riesgo.
  * **Agotamiento Moderado:** 100% Sin riesgo, 0% En riesgo.
  * **Agotamiento Alto:** 66.7% Sin riesgo, **33.3% En riesgo**.
  * **Agotamiento Severo:** 0% Sin riesgo, **100.0% En riesgo**.

---

## 6. Tablas Estadísticas Oficiales y Análisis de Outliers (IQR)

### 📊 Tabla 2. Estadísticas descriptivas de las variables numéricas

| Variable | Media ($\mu$) | Desv. Estándar ($\sigma$) | Mínimo | Mediana | Máximo |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Edad (años)** | 19.04 | 3.77 | 13.00 | 19.00 | 25.00 |
| **Horas en redes sociales** | 4.54 | 2.40 | 0.00 | 4.50 | 14.00 |
| **Horas con IA** | 2.58 | 1.68 | 0.00 | 2.51 | 9.50 |
| **Horas de sueño** | 6.54 | 1.27 | 2.00 | 6.55 | 11.15 |
| **Horas de actividad física** | 1.25 | 1.04 | 0.00 | 1.13 | 5.00 |
| **Salud mental** | 72.51 | 9.25 | 32.56 | 73.76 | 91.76 |
| **Salud física** | 88.02 | 9.68 | 48.03 | 89.47 | 99.98 |
| **Aislamiento social** | 4.31 | 1.16 | 0.97 | 4.28 | 8.41 |
| **Rendimiento académico** | 78.31 | 11.54 | 23.99 | 78.59 | 99.98 |

---

### 📊 Tabla 3. Promedios según el riesgo de reprobación

| Variable | Sin riesgo ($N=14,100$) | En riesgo ($N=900$) | Diferencia Absoluta |
| :--- | :---: | :---: | :---: |
| **Horas en redes sociales** | 4.34 hrs | **7.67 hrs** | $+3.33$ hrs ($+76.7\%$) |
| **Horas con IA** | 2.53 hrs | **3.51 hrs** | $+0.98$ hrs ($+38.7\%$) |
| **Horas de sueño** | 6.62 hrs | **5.35 hrs** | $-1.27$ hrs (Déficit) |
| **Horas de actividad física** | 1.28 hrs | **0.68 hrs** | $-0.60$ hrs ($-46.9\%$) |
| **Salud mental** | 73.34 pts | **59.49 pts** | $-13.85$ puntos |
| **Salud física** | 88.46 pts | **81.05 pts** | $-7.41$ puntos |
| **Aislamiento social** | 4.24 pts | **5.37 pts** | $+1.13$ puntos |
| **Rendimiento académico** | 79.18 pts | **64.79 pts** | $-14.39$ puntos |

---

### 📐 Detección de Valores Atípicos con el Rango Intercuartílico ($IQR$)
Se calculó el rango intercuartílico $IQR = Q_3 - Q_1$ identificando las observaciones fuera del intervalo $[Q_1 - 1.5 \cdot IQR, Q_3 + 1.5 \cdot IQR]$:

```python
for c in num.columns.drop('Academic_Failure_Risk'):
    q1, q3 = num[c].quantile([0.25, 0.75])
    iqr = q3 - q1
    n = ((num[c] < q1 - 1.5 * iqr) | (num[c] > q3 + 1.5 * iqr)).sum()
    print(f'{c}: {n} valores atípicos')
```

* **Salud mental:** 175 casos atípicos.
* **Horas de sueño:** 96 casos atípicos.
* **Salud física:** 59 casos atípicos.
* **Rendimiento académico:** 56 casos atípicos.
* **Horas con IA:** 54 casos atípicos.
* **Actividad física:** 51 casos atípicos.
* **Horas en redes sociales:** 45 casos atípicos.
* **Aislamiento social:** 33 casos atípicos.
* **Edad:** 0 casos atípicos.

> **Decisión Técnica:** Los valores atípicos representan apenas entre el $0.2\%$ y el $1.1\%$ del total de datos y corresponden a situaciones humanas extremas pero plausibles (como dormir 2 horas o pasar 14 horas en pantalla). Por ende, **se conservan íntegramente** para no distorsionar el entrenamiento de modelos basados en árboles.

---

## 7. Hallazgos Clave y Alertas Metodológicas

1. **Desbalance de Clases Severo (94% / 6%):**  
   Un clasificador ingenuo que prediga siempre "Sin riesgo" alcanzaría un $94.0\%$ de precisión (*Accuracy*) pero sería completamente inútil. En la etapa de modelado será indispensable optimizar métricas como **Recall (Sensibilidad)**, **F1-Score**, **Precisión Balanceada** y **PR-AUC**.
2. **Alerta de Fuga de Información (*Data Leakage* con Burnout):**  
   El nivel de agotamiento predice de forma cuasi-perfecta el riesgo ($100\%$ en severo y $0\%$ en bajo/moderado). Un modelo que incluya `Burnout_Level` parecerá perfecto pero no funcionará como un verdadero detector temprano, sino como una alarma tardía. Se deben entrenar variantes de modelos con y sin esta variable.
3. **Uso Reactivo de la Inteligencia Artificial:**  
   Los alumnos en riesgo usan más horas la IA ($3.51$ vs $2.53$ hrs). Esto sugiere que recurren a herramientas generativas a última hora como un intento desesperado de resolver tareas atrasadas, sin un proceso reflexivo de estudio.
4. **El Sedentarismo como Agravante:**  
   La reducción a la mitad de la actividad física ($0.68$ hrs) priva a los estudiantes en riesgo de un mecanismo biológico natural para reducir el cortisol y regular el ciclo circadiano del sueño.

---

## 8. Plan de Mejora y Recomendaciones

### A. Recomendaciones Prácticas para el Alumnado 🎓
1. **Higiene Digital y Control de Pantallas:**
   - Establecer un límite diario en redes sociales (meta: menos de 4 horas al día).
   - Aplicar la regla de **cero pantallas 30 minutos antes de dormir** para recuperar un descanso mínimo de 7 horas continuas.
2. **Uso Productivo y Crítico de la IA:**
   - Utilizar herramientas de IA como un **tutor interactivo** (para pedir explicaciones paso a paso, generar cuestionarios de repaso o sintetizar lecturas densas) y no como un atajo de copiado pasivo.
3. **Autocuidado y Movimiento:**
   - Integrar 30 a 45 minutos diarios de actividad física para reducir la fatiga mental y mejorar la concentración.
   - Formar círculos de estudio presenciales para combatir el aislamiento social.
4. **Detección Oportuna del Estrés:**
   - Reconocer los primeros síntomas de agotamiento (*Burnout*) y solicitar apoyo psicopedagógico antes de llegar al nivel severo.

### B. Recomendaciones para la Institución Educativa 🏫
1. **Sistema Preventivo de Alertas Tempranas:**
   - Aplicar breves cuestionarios semestrales de bienestar (3-5 preguntas sobre sueño y estrés) para canalizar a tiempo a estudiantes con agotamiento moderado o alto.
2. **Talleres de Alfabetización en IA y Gestión del Tiempo:**
   - Capacitar a la comunidad estudiantil en metodologías de estudio efectivas y uso ético de la IA.
3. **Calendarización Académica Equilibrada:**
   - Evitar semanas de sobrecarga extrema coordinando las fechas de entregas y exámenes entre docentes para reducir picos de agotamiento colectivo.

---

## 9. Valor Técnico y Competencias Adquiridas

Al desarrollar esta práctica y avance de proyecto, se consolidaron las siguientes competencias profesionales en Ciencia de Datos e Inteligencia Artificial:

```
[Datos Crudos] ──> [Limpieza y Validación] ──> [Mapeo de Variables] ──> [Análisis Univariado/Multivariado] ──> [Detección de Sesgos/Leakage] ──> [Decisiones de Negocio/Impacto]
```

1. **Manipulación de Datos a Escala con Pandas y NumPy:**
   - Carga, indexación, filtrado, cálculos agregados (`groupby`, `mean`, `std`, `median`).
   - Generación de tablas cruzadas complejas con normalización por filas (`pd.crosstab(..., normalize='index')`).
2. **Visualización Analítica Avanzada con Matplotlib y Seaborn:**
   - Creación de cuadrículas de subplots con diseño visual consistente y legible.
   - Construcción de diagramas analíticos: Histogramas con anotaciones dinámicas, Heatmaps con coeficientes de correlación, Boxplots multivariados y Gráficos de Barras Apiladas (*Stacked Bar*).
3. **Estadística Descriptiva y Detección de Anomalías:**
   - Interpretación de medidas de tendencia central y dispersión.
   - Implementación algorítmica del método del Rango Intercuartílico ($IQR$) para la identificación rigurosa de valores atípicos.
4. **Pensamiento Crítico y Metodológico en Machine Learning:**
   - Identificación de problemas de desbalance severo de clases.
   - Detección de riesgos de fuga de información (*Data Leakage*) previa al modelado.
5. **Comunicación Técnica Efectiva:**
   - Capacidad de traducir métricas estadísticas complejas en hallazgos claros, explicaciones pedagógicas y recomendaciones accionables para directivos y estudiantes.

---

## 10. Instrucciones de Instalación y Ejecución

### Requisitos Previos
* Python 3.10 o superior.
* Jupyter Notebook o VS Code con extensión de Jupyter.

### Clonar el Repositorio y Configurar Entorno
```bash
# 1. Clonar el repositorio
git clone https://github.com/malcaraz37/BigDatayDataMining.git
cd BigDatayDataMining

# 2. Crear y activar entorno virtual
python -m venv .venv
# En Windows (PowerShell):
.venv\Scripts\Activate.ps1
# En Linux/Mac:
source .venv/bin/activate

# 3. Instalar librerías requeridas
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Ejecutar el Cuaderno
Abre el archivo [Dataset_Healthy_AI_SOCIAL_MEDIA_IMPACT.ipynb](file:///c:/Users/Manuel/Documents/BigDatayDataMining/AI%20SALUD/Dataset_Healthy_AI_SOCIAL_MEDIA_IMPACT.ipynb) dentro de la carpeta `AI SALUD/` y selecciona el kernel del entorno virtual `.venv`.

---
*Facultad de Telemática — Universidad de Colima | Octubre 2026*
