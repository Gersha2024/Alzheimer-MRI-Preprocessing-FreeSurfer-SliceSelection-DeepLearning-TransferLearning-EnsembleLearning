## FreeSurfer Setup and Processing

This document outlines the installation and setup of **FreeSurfer** and the preprocessing steps using FreeSurfer's **autorecon-1** pipeline for processing MRI data.

### Why Use FreeSurfer?

FreeSurfer is a robust software package used to process and analyze MRI brain images. The **autorecon-1** pipeline is commonly used for preprocessing tasks such as motion correction, skull stripping, and normalization. This preprocessing is essential to ensure that the MRI data is in an optimal format for further analysis, including slice extraction and Shannon entropy calculation.

## 1. **Install FreeSurfer ( v7.1.1 is used )**

Follow the instructions on the official [FreeSurfer Download Page](https://surfer.nmr.mgh.harvard.edu/fswiki/Download) to download and install FreeSurfer.

## 2. **Set up the FreeSurfer environment**
In your terminal, set up FreeSurfer by running the following commands:
      
```
export FREESURFER_HOME=/Applications/freesurfer/7.1.1
source $FREESURFER_HOME/SetUpFreeSurfer.sh
```

## 3. **Verify the FreeSurfer setup**
Check if FreeSurfer is properly installed by running:

```
echo $FREESURFER_HOME
```

  If the setup is correct,this will display the FreeSurfer home directory path.

## 4. **Set the directory for FreeSurfer outputs**
Set the directory where the processed FreeSurfer data will be stored (e.g., Desktop):

```
export SUBJECTS_DIR=/Users/MacBook/Desktop
```

## 5. **Run the FreeSurfer preprocessing pipeline**
To start processing the MRI data, use the recon-all command:

```
recon-all -s adfree -i input_image.nii -autorecon1 -time
```

  -s adfree: Creates a directory named adfree for the processed data.

  -i input_image.nii: Replace this with the path to your MRI file.

  -autorecon1: This runs the first stage of FreeSurfer's automatic processing.

  -time: This shows the processing time.

## 6. **Check the output directory**
After processing, confirm that the output directory exists by running:

```
echo $SUBJECTS_DIR/adfree
```

 This should return the path to the processed data folder.

## Notes

**FreeSurfer Preprocessing**: 

  Make sure FreeSurfer is correctly installed and the environment is set up before running the recon-all command.

**File Paths**: 

  Always replace file paths in the commands with your actual file locations. 

**Execution Order**: 

  Follow the steps in order – FreeSurfer preprocessing → MGZ to PNG conversion → Shannon entropy slice selection.
