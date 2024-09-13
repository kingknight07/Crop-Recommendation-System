importances = rf_model.feature_importances_
features = ['N', 'P', 'K', 'pH', 'rainfall', 'temperature']

# Feature importances sorting
indices = np.argsort(importances)

plt.figure(figsize=(10, 8))
plt.title('Feature Importances')
plt.barh(range(X_train.shape[1]), importances[indices], align='center')
plt.yticks(range(X_train.shape[1]), np.array(features)[indices])
plt.xlabel('Feature Importance')
plt.show()
