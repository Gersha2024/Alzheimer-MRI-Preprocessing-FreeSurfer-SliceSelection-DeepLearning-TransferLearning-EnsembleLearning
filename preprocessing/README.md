# Preprocessing Folder

This folder contains the scripts and tools used for preprocessing MRI data. The preprocessing steps include FreeSurfer processing, conversion of MGZ volumes to PNG slices, and Shannon entropy-based slice selection.

## Overview of Preprocessing Steps

### Step 1 – FreeSurfer Installation and Processing

In this step, we used **FreeSurfer** to preprocess MRI data. The data was processed using FreeSurfer's **autorecon-1** pipeline, which involves several stages including motion correction, skull stripping, and normalization.

- **Input Data**: MRI volumes in **DICOM** format were used from the **ADNI** dataset.
- **FreeSurfer Version**: We used **FreeSurfer v7.1.1** to process the data.
- **FreeSurfer Steps**: The following stages were performed in FreeSurfer:
  1. Motion correction and conform
  2. Non-uniform intensity normalization (NU)
  3. Talairach transform computation
  4. Intensity normalization
  5. Skull stripping

  For detailed instructions on installing and configuring **FreeSurfer**, please refer to the [FreeSurfer Setup Guide](freesurfer.md).

### Step 2 – Conversion: MGZ to 2D Slices

Once the data was preprocessed using FreeSurfer, we converted the processed **`.mgz`** volumes into **2D slices** in **axial**, **coronal**, and **sagittal** orientations. 

**Tool Used**: We used the [mgz2imgslices](https://github.com/FNNDSC/mgz2imgslices) tool for this conversion.

**License**: This tool is licensed under the **MIT License**.

**Installation & Usage**:
  Instead of cloning manually, the tool can be installed directly from PyPI: 
  ```
  pip install mgz2imgslices
  rm -rf results
  mkdir results && chmod 777 results
  mgz2imgslices -I /path/to/your/data/ --inputFile  input_file.mgz --outputDir /path/to/output/ --outputFileStem output_name --outputFileType png --lookupTable FreeSurferColorLUT.txt
```

**Output Files**:

After running the command, the following files will be generated in the output directory:

- 2D slice images: These will be saved as PNG files for each slice in axial, coronal, and sagittal orientations.

- output_name.npy: A NumPy array that stores the 2D slices in a format that can be used for further processing (e.g., entropy calculation).

**Important Notes**:

- The `FreeSurferColorLUT.txt` file is essential for proper labeling of the voxel values. This file should be placed in the same directory as the .mgz file.

- If you don’t already have this file, you can download it directly from the [pl-mgz2imageslices](https://github.com/FNNDSC/pl-mgz2imageslices) repository and copy it into the same directory as your `.mgz` file.

- The resulting output_name.npy can be loaded into Python using np.load() for further processing (e.g., Shannon entropy).


### Step 3 – Slice Selection with Shannon Entropy
After converting the data to 2D slices, we selected the most informative slices based on Shannon entropy. We calculated the entropy for each slice and selected the top 32 slices for each orientation (axial, coronal, sagittal).

**Tool Used**: The script [Slice Selection with Shannon Entropy](entropy_filter.py) was used for this step.
For more details on the slice selection method and the Shannon entropy calculation, please refer to the script entropy_filter.py in this folder.
