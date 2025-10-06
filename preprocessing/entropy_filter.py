import os
import numpy as np
import cv2
from skimage.measure import shannon_entropy

# ====================================================
# Function: extract_top_entropy_slices
# ----------------------------------------------------
# Given a 3D numpy volume, compute Shannon entropy for
# slices in axial, coronal, and sagittal orientations.
# For each orientation, the top 32 slices (by entropy)
# are saved as PNG images (0.png ... 31.png).
# ====================================================

def extract_top_entropy_slices(volume, output_dir, top_k=32):
    """
    Args:
        volume (np.ndarray): 3D numpy array (e.g., from np.load).
        output_dir (str): directory where results will be saved.
        top_k (int): number of slices with highest entropy to save.
    """

    # Define how to slice the volume in each orientation
    orientations = {
        "axial":    lambda v, i: v[:, i, :],   # axis=1
        "coronal":  lambda v, i: v[i, :, :],   # axis=0
        "sagittal": lambda v, i: v[:, :, i],   # axis=2
    }

    # Map orientation to the axis length
    axis_map = {
        "axial": 1,
        "coronal": 0,
        "sagittal": 2,
    }

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Process each orientation
    for orient, slicer in orientations.items():
        entropies = []
        axis_len = volume.shape[axis_map[orient]]

        # Compute entropy for each slice
        for i in range(axis_len):
            img = slicer(volume, i)
            ent = shannon_entropy(img)
            entropies.append((i, ent))

        # Pick top-k slices by entropy
        top_slices = sorted(entropies, key=lambda x: x[1], reverse=True)[:top_k]

        # Create a subdirectory for this orientation
        orient_dir = os.path.join(output_dir, orient)
        os.makedirs(orient_dir, exist_ok=True)

        # Save slices as 0.png ... (top_k-1).png
        for idx, (slice_idx, _) in enumerate(top_slices):
            img = slicer(volume, slice_idx)
            cv2.imwrite(os.path.join(orient_dir, f"{idx}.png"), img)

        print(f"[INFO] {orient}: saved {top_k} slices to {orient_dir}")


# ====================================================
# Example usage:
# ====================================================
if __name__ == "__main__":
    # Load your volume (update with your .npy path)
    volume = np.load("results/label-wholeVolume/sample.npy")

    # Set the output directory for entropy slices
    output_directory = "entropy_slices"

    # Run the extraction
    extract_top_entropy_slices(volume, output_directory, top_k=32)
