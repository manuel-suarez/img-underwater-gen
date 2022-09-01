import os
import numpy as np
from PIL import Image

root_folder = r"C:\Users\masua\Downloads\Cimat\Nyu v2"
base_dir = "NYU_GT"
clean_dir = "NYU_CL"
under_dir = "NYU_UW"

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

TYPE = type_1

# Traverse all files in directory
for num_image in range(1, 2):
    # Conform image and depth filenames
    fname = f"{num_image}_Image_.bmp"
    dname = f"{num_image}_Depth_.bmp"
    # Open images
    image = np.array(Image.open(os.path.join(root_folder, base_dir, fname)))
    print("Image: ", image.shape, image.dtype, np.max(image), np.min(image))
    depth = np.array(Image.open(os.path.join(root_folder, base_dir, dname)))
    print("Depth: ", depth.shape, depth.dtype, np.max(depth), np.min(depth))
    # Remove blank edges
    image0 = image[10:-10, 10:-10, :] / 255
    depth0 = depth[10:-10, 10:-10] / 255

    print("Image0: ", image0.shape, image0.dtype, np.max(image0), np.min(image0))
    print("Depth0: ", depth0.shape, depth0.dtype, np.max(depth0), np.min(depth0))

    # Parámetros aleatorios de profundidad y horizonte
    deep = 5 - 2 * np.random.rand()
    horization = 15 - 14.5 * np.random.rand()

    # Término beta
    A1 = 1.5 * TYPE[0]**deep
    A2 = 1.5 * TYPE[1]**deep
    A3 = 1.5 * TYPE[2]**deep
    # Término t
    t1 = TYPE[0]**(depth0 * horization)
    t2 = TYPE[1]**(depth0 * horization)
    t3 = TYPE[2]**(depth0 * horization)

    print("T1", t1.shape, t1.dtype)
    print("T2", t2.shape, t2.dtype)
    print("T3", t3.shape, t3.dtype)

    # Underwater image
    I = np.zeros(image0.shape)
    print("I", I.shape, I.dtype)
    I[:, :, 0] = image0[:, :, 0] * t1 + (1 - t1) * A1
    I[:, :, 1] = image0[:, :, 1] * t2 + (1 - t2) * A2
    I[:, :, 2] = image0[:, :, 2] * t3 + (1 - t3) * A3
    print("I", I.shape, I.dtype)

    # Guardamos imagen
    clean_img = Image.fromarray((image0 * 255).astype(np.uint8))
    clean_img.save(os.path.join(root_folder, under_dir, fname))
    underwater_img = Image.fromarray((I * 255).astype(np.uint8))
    uname = f"{num_image}_Underwater_.bmp"
    underwater_img.save(os.path.join(root_folder, under_dir, uname))