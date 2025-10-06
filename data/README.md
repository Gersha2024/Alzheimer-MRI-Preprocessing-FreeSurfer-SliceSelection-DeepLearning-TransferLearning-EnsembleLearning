# Data Folder

This folder contains metadata manifests for subjects in the **ADNI dataset**.  
Raw MRI data is **not included** due to licensing restrictions.

----

### For the three main stages:
- **50 AD images**  
- **50 CN images**  
- **50 MCI images**  

**File Formats**:  
- The metadata manifests are provided in **CSV (`.csv`)** format for the three main stages (AD, CN, MCI).
- The **MMSE range** for the included subjects is 24 to 30.  
- Images correspond to **ADNI Subject IDs** and **Image Data IDs** as used in the study.


### For **pMCI** and **sMCI**:

- The dataset for **progressive MCI (pMCI)** and **stable MCI (sMCI)** was obtained from the ADNI dataset as part of the study:  
*Salvatore, C., A. Cerasa, and I. Castiglioni, MRI characterizes the progressive course of AD and predicts conversion to Alzheimer’s dementia 24 months before probable diagnosis. Frontiers in aging neuroscience, 2018. 10: p. 135*.
- The metadata for **sMCI** and **pMCI** is provided via the [Salvatore et al. 2018 GitHub repository](https://github.com/christiansalvatore/Salvatore-200Longitudinal).

Images were originally in **DICOM format**, and the dataset contains **MRI scans** acquired in **MPRAGE** modality.

----

## To use the data:
1. Download the MRI scans from [ADNI Data Access](http://adni.loni.usc.edu/data-samples/access-data/).
2. Use the provided manifests to map the images to each stage.
3. Run the preprocessing steps as described in [`preprocessing/`](/preprocessing/).

**Note**: This folder only contains metadata and manifests. Raw MRI images must be accessed directly from ADNI.  
For further details on the study, visit the [Salvatore et al. 2018 Longitudinal GitHub repository](https://github.com/christiansalvatore/Salvatore-200Longitudinal).

