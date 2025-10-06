# train_model

import tensorflow as tf
import numpy as np
import os

# ==============================================
# Load dataset paths (3 classes: MCI, NC, AD) / (2 classes: pMCI, sMCI)
# ==============================================
path = "path_to_images"   # <-- replace with your dataset path
images_path = tf.data.Dataset.list_files(path + "/*/*/*")

for i in images_path.take(1):
    print("One sample path : ", i)

# OR LABELS=["pMCI", "sMCI"]
LABELS = ["MCI", "NC", "AD"]

# Function to load and preprocess an image + assign label
def read_image_with_label(path):
    # Read image
    image = tf.io.read_file(path)
    image = tf.image.decode_png(image)
    image = tf.image.grayscale_to_rgb(image)         # convert grayscale to RGB
    image = tf.image.resize(image, [X, X])       # [X,X] e.g. [224,224]. resize to MODEL input size
    image = tf.image.per_image_standardization(image) # normalize

    # Extract label from path
    parts = tf.strings.split(path, os.path.sep)
    label = tf.strings.split(parts[-3], "-")[-1]  
    return image, LABELS == label   # one-hot encoded label


# ==============================================
# Train / Validation / Test split [reports](reports/README.md)
# ==============================================
images_path = images_path.shuffle(X)
a_path = images_path.skip(X)
test_path = images_path.take(X)
a_path = a_path.shuffle(X)
train_path = a_path.skip(X)
val_path = a_path.take(X)

# Map paths to (image, label) pairs
train_set = train_path.map(read_image_with_label)
test_set = test_path.map(read_image_with_label)
val_set = val_path.map(read_image_with_label)

# Shuffle and batch datasets (check [reports](reports/README.md))
train_set = train_set.shuffle(X).batch(Y)
test_set = test_set.shuffle(X).batch(1)
val_set = val_set.shuffle(X).batch(1)

print("Length of total data : ", len(images_path))
print("Length of training data : ", len(train_path))
print("Length of test data : ", len(test_path))
print("Length of validation data : ", len(val_path))


# ==============================================
# Model definition + custom classifier----M:e.g. MobileNet, S:e.g. (224,224,3)
# ==============================================
M1 = tf.keras.applications.M(
    include_top=False,
    weights="imagenet",    
    input_shape=S,
)

# Freeze base model layers (transfer learning)
for layer in M1.layers:
    layer.trainable = False

# Custom classification head
flat1 = tf.keras.layers.Flatten()(M1.layers[-1].output) 
# (check [reports](reports/README.md)). e.g. Dense 256, activation='relu'
class1 = tf.keras.layers.Dense(?, activation='?')(flat1)
# for Dropout (check [reports](reports/README.md)). 
dropout = tf.keras.layers.Dropout(X)(class1)
# 3 for [AD,MCI,CN] AND 2 for [pMCI,sMCI], for activation (check [reports](reports/README.md))
output = tf.keras.layers.Dense(3, activation='?')(dropout)  # 3 classes: MCI, NC, AD

# Define new model
model1 = tf.keras.models.Model(inputs=M1.inputs, outputs=output)
model1.summary()


# ==============================================
# Optimizer and Callbacks
# ==============================================
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

# Creating LR Scheduler
# for Learning Rate (check [reports](reports/README.md))
initial_learning_rate = X
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps=755,
    decay_rate=0.9,
    staircase=True)

METRICS = ['accuracy',
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall')
    ]


model1.compile(optimizer= Adam(lr_schedule), loss='categorical_crossentropy', metrics=METRICS)# cross entropy =loss 

callback = tf.keras.callbacks.EarlyStopping(monitor='accuracy', patience=4)

# Training the model

history = model1.fit(train_set,
                    epochs=50, 
                    validation_data=val_set,                                                          
                   )

# Save final model
model1.save('NAME.h5')
