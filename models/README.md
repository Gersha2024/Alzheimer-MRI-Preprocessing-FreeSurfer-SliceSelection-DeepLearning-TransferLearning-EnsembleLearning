# Models Folder

This folder contains the implementation of transfer learning experiments and evaluation scripts for Alzheimer’s disease detection and progression analysis using MRI scans from the ADNI dataset.  

### Multi-class classification (AD vs MCI vs CN):

Goal: detect the three main stages of Alzheimer’s disease.

Models: MobileNetV2, VGG16, and ResNet50 were fine-tuned and later combined using an ensemble strategy.

### Binary classification (pMCI vs sMCI):

Goal: predict progression of MCI into Alzheimer’s disease 24 months before probable diagnosis.

Model: MobileNetV2 only. No ensemble was used in this setting.

----

## Structure

- **`train_model.py`** → Training pipeline for transfer learning and fine-tuning.  
  - Loads preprocessed MRI slices (axial, coronal, sagittal).  
  - Applies transfer learning with three backbone models: MobileNetV2, VGG16, and ResNet50.  
  - Supports fine-tuning with task-specific hyperparameters.
  📌 Link to training code → [`models/train_model.py`](models/train_model.py)
  - Saves trained models in `.h5` format.  

- **`evaluate.py`** → Evaluation and testing pipeline.  
  - Uses **CrossEntropy loss**.  
  - Evaluation metrics: Accuracy, Precision, Recall, F1-score.
  📌 Link to evaluation code → [`models/evaluate.py`](models/evaluate.py)

- **`ensemble.py`** → Ensemble learning.  
  - Combines predictions from three trained models using **majority voting**.  
  - Resolves ties with an alternative selection strategy.  
  - Provides final ensemble predictions for the AD vs MCI vs CN task.
  📌 Link to ensemble code → [`models/ensemble.py`](models/ensemble.py) 

----

## Notes
- Each model has been fine-tuned with different hyperparameters depending on the architecture and the MRI orientation.  
- For detailed hyperparameters and training results, see the [`reports`](reports/README.md) folder.  
- This folder focuses on **implementation**, while all experimental results and visualizations are documented in [`reports`](reports/README.md).  

