from PIL import Image

root_folder = r"C:\Users\masua\Downloads\Cimat\Nyu v2\NYU_GT"
clean_img = "NYU_GT"
under_img = "NYU_UW"

# Tipos de ambiente submarino
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

# Recorremos el número total de imágenes utilizando el mapa de profundidad para generar la imagen sintética
