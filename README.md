<div align="center">

# AI and Social Media Impact on Student Health and Academic Performance
### Impacto de la Inteligencia Artificial y las Redes Sociales en la Salud y el Rendimiento Academico

**[ English Version ](#english-version) | [ Version en Espanol ](#version-en-espanol)**

</div>

---

<a name="english-version"></a>
# English Version

## 1. Project Overview

 Manuel Alcaraz Baltazar
* **Date:** October 2026

This project evaluates the impact of social media exposure and Artificial Intelligence tool usage on students' health indicators (sleep, physical activity, mental and physical health, social isolation) and academic performance. The primary objective is the early detection of students at risk of academic failure (`Academic_Failure_Risk`).

The analysis was developed through an Exploratory Data Analysis (EDA) in Python utilizing **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.

---

## 2. Dataset Description

The dataset was sourced from Kaggle: *AI and Social Media Impact: Student Health and Grades* (by Debayan Bandyopadhyay).

* **Total Records:** 15,000 unique students.
* **Total Features:** 14 attributes (1 identifier, 9 numerical, 4 categorical).
* **Data Quality:** Complete dataset with 0 missing values and 0 duplicate rows.

### Data Dictionary

| Feature | Data Type | Spanish Translation | Description |
| :--- | :---: | :--- | :--- |
| `Student_ID` | String | Identificador | Unique student identifier code (`STU_00001` to `STU_15000`). |
| `Age` | Integer | Edad | Age in years (range: 13 to 25 years). |
| `Gender` | Categorical | Genero | Registered gender: Male, Female, Non-binary. |
| `Education_Level` | Categorical | Nivel Escolar | Academic stage: High School, College, University. |
| `Daily_Social_Media_Hours` | Float | Horas en redes sociales | Daily hours spent on social platforms (0 to 14 hrs). |
| `Daily_AI_Tool_Usage_Hours` | Float | Horas con herramientas de IA | Daily hours using generative AI tools (0 to 9.5 hrs). |
| `Sleep_Hours` | Float | Horas de sueno | Average nightly sleep hours (2.0 to 11.15 hrs). |
| `Physical_Activity_Hours` | Float | Horas de actividad fisica | Daily exercise or physical activity (0 to 5.0 hrs). |
| `Mental_Health_Score` | Float | Salud mental | Psychological well-being score from 0 to 100. |
| `Physical_Health_Score` | Float | Salud fisica | Self-reported physical wellness score from 0 to 100. |
| `Social_Isolation_Score` | Float | Aislamiento social | Perceived social isolation scale (1 to 10). |
| `Burnout_Level` | Categorical | Nivel de agotamiento | Academic fatigue level: Low, Moderate, High, Severe. |
| `Academic_Performance_Score` | Float | Rendimiento academico | GPA or exam grade score from 0 to 100. |
| `Academic_Failure_Risk` | Binary (0/1) | Riesgo de reprobacion | **Target Variable: 0 = No Risk, 1 = At Risk of Failure**. |

---

## 3. Variable Translation and Mapping to Spanish

### Rationale
To ensure that all generated charts, summary matrices, and reports can be directly interpreted by faculty members, tutors, and administrative directors without language ambiguity, feature names and categorical levels were mapped to Spanish.

### Technical Implementation
Pandas dictionary mappings were implemented for clear labeling across Seaborn and Matplotlib outputs:

```python
# Feature mapping for charts and tables
var_names_es = {
    'Age': 'Edad (anos)',
    'Daily_Social_Media_Hours': 'Horas en redes sociales',
    'Daily_AI_Tool_Usage_Hours': 'Horas con herramientas de IA',
    'Sleep_Hours': 'Horas de sueno',
    'Physical_Activity_Hours': 'Horas de actividad fisica',
    'Mental_Health_Score': 'Salud mental',
    'Physical_Health_Score': 'Salud fisica',
    'Social_Isolation_Score': 'Aislamiento social',
    'Academic_Performance_Score': 'Rendimiento academico',
    'Academic_Failure_Risk': 'Riesgo de reprobacion'
}

# Ordered categorical mapping for Burnout
burnout_order = ['Low', 'Moderate', 'High', 'Severe']
burnout_labels = ['Bajo', 'Moderado', 'Alto', 'Severo']
```

---

## 4. Key Visualizations

The script generates 5 analytical figures:

1. **Figure 1. Distribution of Academic Failure Risk and Burnout Level:**
   * Uses `sns.countplot` across two subplots.
   * Demonstrates heavy class imbalance: **94.0% (14,100 students)** are not at risk, while **6.0% (900 students)** are at risk.
   * Burnout shows a decaying frequency: Low (60.0%), Moderate (28.0%), High (9.0%), Severe (3.0%).

2. **Figure 2. Distribution of Quantitative Features:**
   * $2 \times 3$ subplot grid with `ax.hist(bins=30)`.
   * Displays continuous bell-shaped curves and dynamically calculates mean ($\mu$) and standard deviation ($\sigma$) in each subplot title.

3. **Figure 3. Pearson Correlation Matrix:**
   * Computes linear correlation with `df.corr(numeric_only=True, method='pearson')` visualized via `sns.heatmap(annot=True)`.
   * Highlights that higher mental health ($-0.36$), academic score ($-0.30$), and sleep ($-0.24$) reduce risk, whereas social media usage ($+0.33$) and isolation ($+0.23$) increase risk.

4. **Figure 4. Comparative Boxplots (No Risk vs At Risk):**
   * Uses `sns.boxplot` for the 4 critical features.
   * Shows students at risk sleep under 5.5 hours, spend nearly double the time on social media (7.67 hrs), and experience lower mental health and grades.

5. **Figure 5. Proportion of At-Risk Students by Burnout Level (100% Stacked Bar):**
   * Constructed using `pd.crosstab(..., normalize='index') * 100` and `.plot(kind='bar', stacked=True)`.
   * Reveals that in *Severe* Burnout, 100% of students fail, and in *High* Burnout, 33.3% fail, whereas in *Low* and *Moderate*, risk is 0%.

---

## 5. Statistical Summary and Outlier Detection (IQR)

### Comparative Group Means (Table 3)

| Feature | No Risk ($N=14,100$) | At Risk ($N=900$) | Observed Impact |
| :--- | :---: | :---: | :--- |
| **Social Media Hours** | 4.34 hrs | **7.67 hrs** | $+76.7\%$ screen time increase |
| **AI Tool Hours** | 2.53 hrs | **3.51 hrs** | $+38.7\%$ reactive use |
| **Sleep Hours** | 6.62 hrs | **5.35 hrs** | $-1.27$ hrs sleep deficit |
| **Physical Activity** | 1.28 hrs | **0.68 hrs** | $-46.9\%$ reduction in exercise |
| **Mental Health Score** | 73.34 pts | **59.49 pts** | $-13.85$ point drop |
| **Academic Score** | 79.18 pts | **64.79 pts** | $-14.39$ point drop |

### Outlier Detection via Interquartile Range ($IQR$)
Outlier boundaries were defined by $[Q_1 - 1.5 \cdot IQR, Q_3 + 1.5 \cdot IQR]$ where $IQR = Q_3 - Q_1$:
* **Mental Health Score:** 175 outliers.
* **Sleep Hours:** 96 outliers.
* **Physical Health Score:** 59 outliers.
* **Academic Score:** 56 outliers.
* **AI Tool Usage:** 54 outliers.
* **Physical Activity:** 51 outliers.
* **Social Media Hours:** 45 outliers.
* **Social Isolation:** 33 outliers.

*Technical Decision:* Outliers represent less than $1.2\%$ of the total data and reflect plausible human edge cases (e.g., 2 hours of sleep or 14 hours on screens); therefore, all observations were preserved to prevent distortion in tree-based algorithms.

---

## 6. Key Findings and Methodological Considerations

1. **Severe Class Imbalance (94% / 6%):** Standard accuracy is misleading; classification models must prioritize **Recall**, **F1-Score**, and **PR-AUC**.
2. **Data Leakage in Burnout Feature:** Because `Burnout_Level` exhibits almost deterministic separation on the target, models should be evaluated both with and without this variable to ensure practical early detection.
3. **Reactive AI Usage:** At-risk students use AI tools more frequently ($3.51$ vs $2.53$ hrs), indicating late, reactive dependence rather than structured learning.
4. **Sedentary Lifestyle:** Cutting physical activity in half ($0.68$ hrs) worsens sleep disruption and stress regulation.

---

## 7. Recommendations

### For Students
* **Digital Hygiene:** Cap social media usage below 4 hours daily and avoid screens 30 minutes before sleep to secure at least 7 hours of rest.
* **Active AI Learning:** Leverage AI tools as an interactive tutor (generating practice quizzes and conceptual summaries) rather than copying homework solutions.
* **Daily Physical Exercise:** Maintain 30-45 minutes of daily exercise to lower isolation scores and refresh cognitive focus.
* **Early Stress Recognition:** Seek academic tutoring and counseling before moderate fatigue escalates into severe burnout.

### For Educational Institutions
* **Early Warning Check-ins:** Administer brief mid-term surveys regarding sleep and fatigue to identify at-risk students before final exams.
* **Balanced Workload Scheduling:** Coordinate major assignment deadlines across courses to avoid simultaneous workload spikes.

---

## 8. Technical Value and Acquired Competencies

* **Scalable Data Manipulation:** Group aggregations, hierarchical indexing, and normalized contingency tables with Pandas and NumPy.
* **Analytical Visualization:** Multi-panel subplots, annotated heatmaps, boxplots, and stacked bar charts using Matplotlib and Seaborn.
* **Non-Parametric Statistical Profiling:** Quantitative outlier identification using IQR bounds.
* **Critical Machine Learning Thinking:** Pre-modeling diagnosis of class imbalance and data leakage.
* **Technical Communication:** Translating raw datasets into actionable recommendations for institutional decision-making.

---

## 9. How to Run

### Requirements
* Python 3.10+
* Required packages: `pandas`, `numpy`, `matplotlib`, `seaborn`

```bash
# Run the complete analysis
python analisis_eda.py
```

---
---

<a name="version-en-espanol"></a>
# Version en Espanol

## 1. Descripcion del Proyecto

Manuel Alcaraz Baltazar
* **Fecha:** Octubre 2026

Este proyecto analiza el impacto del uso de redes sociales y herramientas de inteligencia artificial en los habitos de salud (sueno, actividad fisica, salud mental) y en el rendimiento escolar de los estudiantes, con el objetivo de identificar de forma temprana a quienes tienen riesgo de reprobacion academica (`Academic_Failure_Risk`).

El analisis se desarrollo mediante un Analisis Exploratorio de Datos (EDA) estructurado en Python, utilizando las librerias **Pandas**, **NumPy**, **Matplotlib** y **Seaborn**.

---

## 2. Conjunto de Datos

Los datos provienen del repositorio publico de Kaggle: *AI and Social Media Impact: Student Health and Grades* (por Debayan Bandyopadhyay).

* **Total de registros:** 15,000 estudiantes.
* **Total de variables:** 14 (1 identificador, 9 cuantitativas y 4 categoricas).
* **Calidad de datos:** 0 valores nulos y 0 registros duplicados.

### Diccionario de Variables

| Variable Original | Tipo | Variable en Espanol | Descripcion |
| :--- | :---: | :--- | :--- |
| `Student_ID` | Texto | Identificador | Codigo unico del estudiante (`STU_00001` a `STU_15000`). |
| `Age` | Entero | Edad | Edad en anos (13 a 25 anos). |
| `Gender` | Categorica | Genero | Masculino, Femenino o No binario. |
| `Education_Level` | Categorica | Nivel Escolar | Bachillerato (High School), Intermedio (College) o Universidad (University). |
| `Daily_Social_Media_Hours` | Decimal | Horas en redes sociales | Horas diarias dedicadas a redes sociales (0 a 14 hrs). |
| `Daily_AI_Tool_Usage_Hours` | Decimal | Horas con herramientas de IA | Horas diarias de uso de IA generativa (0 a 9.5 hrs). |
| `Sleep_Hours` | Decimal | Horas de sueno | Promedio de sueno diario por noche (2.0 a 11.15 hrs). |
| `Physical_Activity_Hours` | Decimal | Horas de actividad fisica | Horas diarias de deporte o ejercicio (0 a 5.0 hrs). |
| `Mental_Health_Score` | Decimal | Salud mental | Puntaje de bienestar psicologico de 0 a 100. |
| `Physical_Health_Score` | Decimal | Salud fisica | Puntaje de bienestar fisico de 0 a 100. |
| `Social_Isolation_Score` | Decimal | Aislamiento social | Escala de aislamiento percibido (1 a 10). |
| `Burnout_Level` | Categorica | Nivel de agotamiento | Nivel de fatiga: Bajo, Moderado, Alto o Severo. |
| `Academic_Performance_Score` | Decimal | Rendimiento academico | Calificacion promedio escolar (0 a 100). |
| `Academic_Failure_Risk` | Binaria | Riesgo de reprobacion | **Variable objetivo: 0 = Sin riesgo, 1 = En riesgo de reprobar**. |

---

## 3. Mapeo y Traduccion de Variables al Espanol

### Justificacion
Para garantizar que las graficas, tablas y reportes analiticos sean faciles de interpretar por docentes y directivos sin barreras de idioma, se implemento un mapeo ordenado de las columnas y niveles categoricos al espanol.

### Implementacion Tecnica
Se utilizaron diccionarios de mapeo aplicados directamente a las transformaciones y etiquetas de visualizacion:

```python
# Mapeo de nombres para visualizacion y tablas
var_names_es = {
    'Age': 'Edad (anos)',
    'Daily_Social_Media_Hours': 'Horas en redes sociales',
    'Daily_AI_Tool_Usage_Hours': 'Horas con herramientas de IA',
    'Sleep_Hours': 'Horas de sueno',
    'Physical_Activity_Hours': 'Horas de actividad fisica',
    'Mental_Health_Score': 'Salud mental',
    'Physical_Health_Score': 'Salud fisica',
    'Social_Isolation_Score': 'Aislamiento social',
    'Academic_Performance_Score': 'Rendimiento academico',
    'Academic_Failure_Risk': 'Riesgo de reprobacion'
}

# Ordenamiento logico de niveles de agotamiento
burnout_order = ['Low', 'Moderate', 'High', 'Severe']
burnout_labels = ['Bajo', 'Moderado', 'Alto', 'Severo']
```

---

## 4. Visualizaciones Clave del Proyecto

El codigo genera las 5 figuras analiticas descritas a continuacion:

1. **Figura 1. Distribucion del riesgo y agotamiento:**
   * Utiliza `sns.countplot` para mostrar que solo el **6.0% (900 estudiantes)** esta en riesgo de reprobacion frente al **94.0% (14,100)** sin riesgo.
   * Muestra la distribucion decreciente del agotamiento: Bajo (60.0%), Moderado (28.0%), Alto (9.0%) y Severo (3.0%).

2. **Figura 2. Distribucion de variables cuantitativas:**
   * Cuadricula $2 \times 3$ de histogramas con `ax.hist(bins=30)`.
   * Incluye el calculo automatico de la media ($\mu$) y desviacion estandar ($\sigma$) en el encabezado de cada grafico.

3. **Figura 3. Matriz de correlaciones de Pearson:**
   * Calcula `df.corr(numeric_only=True)` y la visualiza con `sns.heatmap(annot=True)`.
   * Identifica que la salud mental ($-0.36$), el rendimiento previo ($-0.30$) y el sueno ($-0.24$) reducen el riesgo; mientras que las redes sociales ($+0.33$) y el aislamiento ($+0.23$) lo incrementan.

4. **Figura 4. Comparacion entre grupos sin riesgo y en riesgo:**
   * Diagramas de caja (`sns.boxplot`) para las 4 variables clave.
   * Evidencia que los estudiantes en riesgo duermen sustancialmente menos y pasan casi el doble de tiempo en redes sociales.

5. **Figura 5. Proporcion de estudiantes en riesgo segun nivel de agotamiento:**
   * Grafico de barras apiladas al 100% con `pd.crosstab(..., normalize='index') * 100` y `.plot(kind='bar', stacked=True)`.
   * Demuestra que en agotamiento *Severo* el 100% reprueba y en *Alto* el 33.3%, mientras que en *Bajo* y *Moderado* el riesgo es 0%.

---

## 5. Tablas Estadisticas y Deteccion de Outliers (IQR)

### Comparacion de Promedios (Tabla 3)

| Variable | Sin riesgo (14,100) | En riesgo (900) | Impacto Observado |
| :--- | :---: | :---: | :--- |
| **Horas en redes sociales** | 4.34 hrs | **7.67 hrs** | Aumento de $+76.7\%$ en pantalla |
| **Horas con IA** | 2.53 hrs | **3.51 hrs** | Mayor uso reactivo ($+38.7\%$) |
| **Horas de sueno** | 6.62 hrs | **5.35 hrs** | Deficit de sueno de $-1.27$ hrs |
| **Actividad fisica** | 1.28 hrs | **0.68 hrs** | Reduccion del $-46.9\%$ |
| **Salud mental** | 73.34 pts | **59.49 pts** | Caida de $-13.85$ puntos |
| **Rendimiento academico** | 79.18 pts | **64.79 pts** | Caida de $-14.39$ puntos |

### Deteccion de Outliers mediante Rango Intercuartilico ($IQR$)
Se calculo $IQR = Q_3 - Q_1$ determinando los limites $[Q_1 - 1.5 \cdot IQR, Q_3 + 1.5 \cdot IQR]$:
* **Salud mental:** 175 casos atipicos.
* **Horas de sueno:** 96 casos atipicos.
* **Salud fisica:** 59 casos atipicos.
* **Rendimiento academico:** 56 casos atipicos.
* **Horas con IA:** 54 casos atipicos.
* **Actividad fisica:** 51 casos atipicos.
* **Horas en redes sociales:** 45 casos atipicos.
* **Aislamiento social:** 33 casos atipicos.

*Decision tecnica:* Los valores atipicos representan menos del $1.2\%$ de los registros y corresponden a casos extremos reales (ej. dormir solo 2 horas), por lo que se conservan en su totalidad.

---

## 6. Hallazgos Principales y Alertas Metodologicas

1. **Desbalance Severo de Clases:** Al haber solo un 6% de casos positivos, no se debe evaluar el modelado con *Accuracy*, sino priorizar metricas como **Recall**, **F1-Score** y **PR-AUC**.
2. **Riesgo de Fuga de Informacion (*Data Leakage*):** El nivel de agotamiento (`Burnout_Level`) actua como un sintoma terminal mas que como una alerta temprana. Se recomienda entrenar modelos con y sin esta variable.
3. **Uso Reactivo de la Inteligencia Artificial:** Los estudiantes con bajo rendimiento usan mas tiempo la IA generativa ($3.51$ vs $2.53$ hrs), lo que evidencia que la usan como atajo de ultima hora y no como herramienta de estudio planificado.
4. **Sedentarismo como Multiplicador:** Los estudiantes en riesgo realizan la mitad de actividad fisica diaria ($0.68$ hrs), agravando el estres y el insomnio.

---

## 7. Recomendaciones

### Para el Alumnado
* **Higiene digital:** Limitar el uso de redes sociales a menos de 4 horas diarias y evitar el uso de pantallas 30 minutos antes de dormir para asegurar al menos 7 horas de descanso.
* **Uso productivo de la IA:** Usar la IA como tutor para formular preguntas, resumir y resolver dudas complejas, en lugar de copiar respuestas sin asimilar el conocimiento.
* **Actividad fisica:** Realizar entre 30 y 45 minutos diarios de ejercicio para despejar la mente y reducir el aislamiento social.
* **Atencion al estres:** Reconocer senales tempranas de fatiga y solicitar apoyo psicopedagogico antes de llegar al agotamiento severo.

### Para la Institucion Educativa
* **Alertas tempranas:** Implementar check-ins semestrales breves sobre sueno y nivel de estres para detectar estudiantes en riesgo antes de los examenes finales.
* **Equilibrio de carga:** Coordinar fechas de entregas y evaluaciones entre asignaturas para evitar picos simultaneos de agotamiento academico.

---

## 8. Valor Tecnico y Competencias Adquiridas

El desarrollo de este proyecto aporto las siguientes competencias profesionales:
* **Analisis exploratorio avanzado con Pandas y NumPy:** Agrupaciones multivariadas, indexacion jerarquica y tablas de contingencia normalizadas.
* **Visualizacion analitica con Matplotlib y Seaborn:** Diseno de subplots legibles, matrices de correlacion y diagramas de caja.
* **Tratamiento estadistico de datos:** Aplicacion de estadistica no parametrica (IQR) y analisis de correlaciones bivariadas.
* **Criterio metodologico en Machine Learning:** Deteccion de desbalance de clases y prevencion de fuga de informacion (*Data Leakage*).
* **Comunicacion tecnica y de negocio:** Capacidad de traducir datos crudos a diagnosticos y planes de accion comprensibles.

---

## 9. Ejecucion del Codigo

### Requisitos
* Python 3.10 o superior.
* Librerias: `pandas`, `numpy`, `matplotlib`, `seaborn`.

### Ejecutar el Script Principal
```bash
python analisis_eda.py
```

---
*Facultad de Telematica — Universidad de Colima*
