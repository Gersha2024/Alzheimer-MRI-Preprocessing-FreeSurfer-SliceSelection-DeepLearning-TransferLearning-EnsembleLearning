

# 🧠 Alzheimer’s Disease Detection using Transfer Learning

This project leverages transfer learning techniques to detect Alzheimer's disease (AD) and predict its progression using MRI scans. By applying advanced deep learning models on T1-weighted brain MRI data, the goal is to classify different stages of AD (AD, MCI, CN) and forecast the progression from Mild Cognitive Impairment (MCI) to Alzheimer's dementia (pMCI vs. sMCI), offering potential for early detection and intervention.

---

## 📂 Project Structure
- `data/`: Metadata manifests (Excel files) for subjects across different diagnostic stages (no raw MRI included).
- `preprocessing/`: Scripts for FreeSurfer preprocessing, slice extraction, and slice selection.
- `models/`: Transfer learning and ensemble learning experiments with MobileNetV2, VGG16, and ResNet50.
- `reports/`: Experimental results, summaries, and visualizations.

  ---

## ⚠️ Data Availability
- Dataset: **ADNI (Alzheimer’s Disease Neuroimaging Initiative)**.  
- Due to licensing restrictions, raw data and FreeSurfer-preprocessed `.mgz` files are **not included** in this repository.  
- Instead, the `data/` folder contains **3 manifest files** related to 3 main stages AD-MCI-CN
- These manifests contain **subject IDs and metadata only**.
- The images for **progressive MCI (pMCI)** and **stable MCI (sMCI)** were obtained from the ADNI dataset and the **Longitudinal Study** project, as described in the study:  
  *Salvatore, C., A. Cerasa, and I. Castiglioni, MRI characterizes the progressive course of AD and predicts conversion to Alzheimer’s dementia 24 months before probable diagnosis. Frontiers in aging neuroscience, 2018. 10: p. 135*.
  The images were downloaded using metadata from the **Longitudinal Study** project, based on the GitHub repository:  
  [Salvatore et al. 2018 Longitudinal GitHub](https://github.com/christiansalvatore/Salvatore-200Longitudinal)
  These data correspond to the longitudinal study that tracks subjects for **24 months**.
- To reproduce results, please:  
  1. Apply for access at [ADNI Data Access](http://adni.loni.usc.edu/data-samples/access-data/).  
  2. Download the required MRI scans.  
  3. Use the manifests in `data/` to select subjects for each stage.  

📌 For more details, see [`data/README.md`](data/README.md).

---

## 🔧 Preprocessing Workflow
- **Input Data**: T1-weighted MRI volumes from ADNI.  
- **Step 1 – FreeSurfer**: Each MRI was processed with the [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/) pipeline (`autorecon-1`, 5 stages):  
  - Motion correction and conform  
  - Non-uniform intensity normalization (NU)  
  - Talairach transform computation  
  - Intensity normalization  
  - Skull stripping  
- **Output**: Preprocessed 3D volumes in `.mgz` format.  
- **Step 2 – Conversion**:  
  Preprocessed `.mgz` volumes were converted into 2D slices using [mgz2imgslices](https://github.com/FNNDSC/mgz2imgslices) (MIT License).  
  This tool generates both `.npy` arrays and `.png` slice images, each `.mgz` volume was converted into 2D PNG slices in the **axial, coronal, and sagittal** orientations.  
- **Step 3 – Slice Selection**: For each orientation, Shannon entropy was computed across slices, and the top **32 informative slices** were selected.  

📌 For more details, see [`preprocessing/README.md`](preprocessing/README.md).

---

## 🚀 Models
- Transfer learning with **MobileNetV2, VGG16, and ResNet50**.  
- Experiments conducted **per orientation** (axial, coronal, sagittal).  
- Ensemble learning approach for improved performance. 

📌 For more details, see [`models/`](models/).

---

## 📊 Reports
- **Multi-class classification**: Alzheimer’s Disease (AD), Mild Cognitive Impairment (MCI), and Cognitively Normal (CN).  
- **Progression analysis**: distinguishing *pMCI* (progressive) from *sMCI* (stable).  
- Detailed results, tables, and figures are available in the [`reports/`](reports/) folder.
- Hyperparameter settings for each model and orientation are provided in [`reports/`](reports/).  

---

## 🧾 Citation
If you use this code, please cite ADNI as required:  
[ADNI Citation Guidelines](http://adni.loni.usc.edu/data-samples/citation/)

---

## 📜 License
- This project is licensed under the **MIT License**.  
- The `mgz2imgslices` tool is used under its original license. Please refer to its [mgz2imgslices](https://github.com/FNNDSC/mgz2imgslices) (MIT License) for details.  
- Check ADNI’s data usage policy before working with the dataset.

