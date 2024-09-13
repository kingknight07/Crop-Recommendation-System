import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
 
cm = confusion_matrix(y_test, y_pred)

 
plt.figure(figsize=(12, 10))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()
