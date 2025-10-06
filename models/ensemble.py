import numpy as np
from tensorflow.keras import models
from sklearn.metrics import accuracy_score, precision_score, recall_score

# ============================
# Load pre-trained models ----examples:
# ============================
model_paths = {
    'mobilenet': 'models2/h5modelmobaxi.h5',
    'resnet': 'models2/h5modelresaxi.h5',
    'vgg': 'models2/h5modelVggaxi.h5'
}

# Load models
model1 = models.load_model(model_paths['mobilenet'])
model2 = models.load_model(model_paths['resnet'])
model3 = models.load_model(model_paths['vgg'])

# ============================
# Load test data from numpy files
# ============================
numpy_data_path = 'numpy_data/'

x_test_200 = np.load(numpy_data_path + 'X1.npy')
x_test_224 = np.load(numpy_data_path + 'X2.npy')
y_test = np.load(numpy_data_path + 'X3.npy')

# Initialize an array to store predictions
y_pred = np.zeros((y_test.shape[0]))

# ============================
# Max voting function
# ============================
def max_voting(array):
    """
    Function to perform majority voting on model predictions.
    If there is no majority, return a default label (3 in this case).
    """
    counts = np.bincount(array)
    argmax = np.argmax(counts)
    if counts[argmax] > 1:
        return argmax
    else:
        return 3  # In case of a tie, return a default label

# ============================
# Perform predictions
# ============================
pred = np.zeros((3, 3))  # Store predictions from all models
max_vot_label = np.zeros((3), dtype=np.int64)

for i in range(y_test.shape[0]):
    # Predict from each model
    pred[0] = model1.predict(x_test_224[i:i+1])
    pred[1] = model2.predict(x_test_224[i:i+1])
    pred[2] = model3.predict(x_test_200[i:i+1])

    # Apply max-voting to the predictions
    max_vot_label[0] = pred[0].argmax(axis=-1)
    max_vot_label[1] = pred[1].argmax(axis=-1)
    max_vot_label[2] = pred[2].argmax(axis=-1)

    # Determine the final predicted label using max voting
    label = max_voting(max_vot_label)

    # If there is a tie, resolve it using the full predictions
    if label == 3:
        label = np.unravel_index(np.argmax(pred, axis=None), pred.shape)[0]

    # Store the final predicted label
    y_pred[i] = label

    # Print the true label and predicted label
    print(f"True label: {y_test[i].argmax(axis=-1)} | Predicted label: {label}")

# ============================
# Evaluate the performance
# ============================
print("\nEvaluation Results:")
print(f"Accuracy: {accuracy_score(y_test.argmax(axis=-1), y_pred)}")
print(f"Precision: {precision_score(y_test.argmax(axis=-1), y_pred)}")
print(f"Recall: {recall_score(y_test.argmax(axis=-1), y_pred)}")
