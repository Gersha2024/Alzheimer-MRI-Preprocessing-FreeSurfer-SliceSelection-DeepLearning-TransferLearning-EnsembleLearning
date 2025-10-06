import matplotlib.pyplot as plt
import tensorflow as tf

# ==============================================
# Load the saved model (ensure you use the correct model path)
# ==============================================
model = tf.keras.models.load_model('best_model.h5') 

# ==============================================
# Plot training history for metrics (precision, recall, accuracy, loss)
# ==============================================
fig, ax = plt.subplots(1, 4, figsize=(20, 3))
ax = ax.ravel()

for i, met in enumerate(['precision', 'recall', 'accuracy', 'loss']):
    ax[i].plot(model.history.history[met])  # training metric
    ax[i].plot(model.history.history['val_' + met])  # validation metric
    ax[i].set_title('Model {}'.format(met))
    ax[i].set_xlabel('epochs')
    ax[i].set_ylabel(met)
    ax[i].legend(['train', 'val'])

# Display the plot
plt.show()

# ==============================================
# Evaluate the model on the test set
# ==============================================
test_loss, test_accuracy, test_precision, test_recall = model.evaluate(test_set, verbose=1)

# Display the evaluation results
print("Test Loss: ", test_loss)
print("Test Accuracy: ", test_accuracy)
print("Test Precision: ", test_precision)
print("Test Recall: ", test_recall)


fig, ax = plt.subplots(1, 4, figsize=(20, 3))
ax = ax.ravel()

for i, met in enumerate(['precision', 'recall', 'accuracy', 'loss']):
    ax[i].plot(history.history[met])
    ax[i].plot(history.history['val_' + met])
    ax[i].set_title('Model {}'.format(met))
    ax[i].set_xlabel('epochs')
    ax[i].set_ylabel(met)
    ax[i].legend(['train', 'val'])  


print("Accuracy Test: ", modelMobCor.evaluate(test_set)[1])
