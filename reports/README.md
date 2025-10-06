## 🧠 Experimental Results 

**Multi-class Classification (AD vs. MCI vs. CN)**:

The performance of the models (VGG16, ResNet50, MobileNetV2) for multi-class classification was evaluated using the test, training, and validation datasets. The exact number of training, validation, and test data are 3264, 576, and 960, respectively. The ResNet50 model achieved the highest accuracy across the Axial and Coronal axes, while MobileNetV2 performed best on the Sagittal axis. Detailed results for each axis and model can be found in Table 2.

**AD Progression Estimation (pMCI vs. sMCI)**:

For estimating the progression of Alzheimer’s disease (AD), the MobileNetV2 model was used. In examining the progression of AD, the exact number of training, validation, and test data in each of the three axes is 2176, 384, and 640, respectively. The results showed that MobileNetV2 on the Axial axis achieved high accuracy on the test set. A detailed summary of the results can be found in Table 3.

- It should be noted that the test data were **not included** in the training or validation process.

--------

## ⚙️ Setup

**Classifier head (general)**:

- Dense layers with dropout for regularization.

- Final Softmax layer (3 classes for AD/MCI/CN, 2 classes for pMCI/sMCI).

- Optimization: Adam optimizer with learning rate scheduling.

**Model Setup**:

- The size of the input images of the two base models, MobileNetV2 and ResNet50, is 224×224, while that of the VGG16 base model is 200×200.

- Batch size = 4 , epoch= 50

- Each project had its own hyperparameter search. Full details can be found in **table 1**.

----------------

### 📊 Hyperparameters

                                                            TABLE 1.
| Pre-trained Model |   Axis   | Diagnosing AD (Dropout) | Diagnosing AD (LR) | Examining AD Progress (Dropout) | Examining AD Progress (LR) |
|-------------------|----------|-------------------------|--------------------|---------------------------------|----------------------------|
|                   |  Axial   |         0.6             |       1e-5         |              0.6                |          1e-5              |
|  **MobileNetV2**  | Coronal  |         0.6             |       1e-5         |              0.7                |          1e-4              |
|                   | Sagittal |         0.6             |       1e-5         |              0.7                |          1e-4              |
|                   |  Axial   |         0.01            |       1e-4         |               -                 |           -                |
|   **ResNet50**    | Coronal  |         0.01            |       1e-4         |               -                 |           -                |
|                   | Sagittal |         0.09            |       1e-3         |               -                 |           -                | 
|                   |  Axial   |         0.3             |       1e-4         |               -                 |           -                |
|     **VGG16**     | Coronal  |         0.3             |       1e-4         |               -                 |           -                |
|                   | Sagittal |         0.3             |       1e-4         |               -                 |           -                |


### 📊 Performance Visualization

- The results of multi-classification obtained from the proposed method based on different axes and models:

                                                            TABLE 2.
    | Pre-trained Model |   Axis   |     Accuracy (TesT)     |     Loss     |    Accuracy (Train)     |  Accuracy (Validation)  |
    |-------------------|----------|-------------------------|--------------|-------------------------|-------------------------|
    |                   |  Axial   |         99.89%          |     0.04     |          98.1%          |          100%           |
    |  **MobileNetV2**  | Coronal  |         99.79%          |     0.04     |          98.32%         |          100%           |
    |                   | Sagittal |         100%            |     0.01     |          99.29%         |          100%           |
    |                   |  Axial   |         100%            |     0.01     |          99.9%          |          100%           |
    |   **ResNet50**    | Coronal  |         100%            |     0.005    |          100%           |          100%           |
    |                   | Sagittal |         99.79%          |     0.05     |          96.12%         |          99.12%         |
    |                   |  Axial   |         99.05%          |     0.09     |          97.9%          |          98.9%          |
    |     **VGG16**     | Coronal  |         99.16%          |     0.1      |          97.74%         |          99.47%         |
    |                   | Sagittal |         100%            |     0.02     |          99.97%         |          100%           |


- Accuracy plots in 3 axes for VGG16, ResNet50, and MobileNetv2:
  
  <img width="469" height="349" alt="image" src="https://github.com/user-attachments/assets/813a8bce-1081-445f-a031-044eb0efa85b" />


- Results of estimating the progression of Alzheimer’s disease using the proposed method based on MobileNetV2:

                                                           TABLE 3.
   | Pre-trained Model |   Axis   |     Accuracy (TesT)     |     Loss     |    Accuracy (Train)     |  Accuracy (Validation)  |
   |-------------------|----------|-------------------------|--------------|-------------------------|-------------------------|
   |                   |  Axial   |         99.84%          |     0.01     |          99.82%         |          100%           |
   |  **MobileNetV2**  | Coronal  |         99.53%          |     0.03     |          92.85%         |          99.22%         |
   |                   | Sagittal |         99.06%          |     0.02     |          92.51%         |          99.48%         |


- Accuracy plots in three axes for MobileNetv2:

<img width="602" height="134" alt="image" src="https://github.com/user-attachments/assets/99a04233-7c5b-427d-8361-f2715607b1e2" />
