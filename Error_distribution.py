errors = y_test - y_pred

plt.figure(figsize=(10, 8))
plt.hist(errors, bins=50, edgecolor='k', alpha=0.7)
plt.xlabel('Prediction Error')
plt.ylabel('Frequency')
plt.title('Prediction Error Distribution')
plt.show()
