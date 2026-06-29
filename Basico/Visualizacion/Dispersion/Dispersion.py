import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style='whitegrid') #graficas mas profesionales
df = pd.read_csv('Basico/Student_Performance.csv', encoding='latin1')


plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='study_hours', y='overall_score', hue='study_method')
plt.title('Relacion entre horas de estudio y rendimiento academico')
plt.xlabel('Horas de estudio')
plt.ylabel('Rendimiento academico')

plt.show()