import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#sns.set_theme(style='whitegrid')
df = pd.read_csv('Basico/Student_Performance.csv', encoding='latin1')

plt.figure(figsize=(10, 6)) 
sns.barplot(data=df, x='internet_access', y='overall_score', hue='school_type')
plt.ylim(63, 65)
plt.title('Relación entre acceso a internet y rendimiento académico')
plt.xlabel('Acceso a internet')
plt.ylabel('Rendimiento académico')

plt.show()
