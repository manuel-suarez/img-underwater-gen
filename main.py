import os
from PIL import Image

root_folder = r"C:\Users\masua\Downloads\Cimat\Nyu v2\NYU_GT"
base_img = "NYU_GT"
clean_img = "NYU_CL"
under_img = "NYU_UW"

# Type of submarine ambient
type_I = [0.85, 0.961, 0.982]
type_IA = [0.84, 0.955, 0.975]
type_IB = [0.83, 0.95, 0.968]
type_II = [0.80, 0.925, 0.94]
type_III = [0.75, 0.885, 0.89]
type_1 = [0.75, 0.885, 0.875]
type_3 = [0.71, 0.82, 0.8]
type_5 = [0.67, 0.73, 0.67]
type_7 = [0.62, 0.61, 0.5]
type_9 = [0.55, 0.46, 0.29]

# Traverse all files in directory
for num_image in range(1, 1450):
    # Conform image and depth filenames
    fname = f"{num_image}_Image_.bmp"
    dname = f"{num_image}_Depth_.bmp"
    # Open images
    image = Image.open(os.path.join(root_folder, base_img, fname))
    depth = Image.open(os.path.join(root_folder, base_img, dname))
    # Remove blank edges
    image0 = image[0:-11, 0:-11, :]
    depth0 = depth[0:-11, 0:-11, :] / 255 # Depth between 0 and 1