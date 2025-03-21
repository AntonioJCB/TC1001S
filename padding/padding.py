import numpy as np
import cv2
import matplotlib.pyplot as plt

def padding(image, pad_height=1, pad_width=1, padding_type='constant', constant_value=0):
    # Mostrar información
    print(f"Padding type: {padding_type}")
    if padding_type == 'constant':
        print(f"Constant padding value: {constant_value}")

    # Convertir a RGB si la imagen es a color, solo para mostrar correctamente
    if len(image.shape) == 3:
        display_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        display_image = image

    # Aplicar padding según tipo
    if len(image.shape) == 2:
        # Imagen en escala de grises
        if padding_type == 'constant':
            padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)),
                                  mode='constant', constant_values=constant_value)
        else:
            padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode=padding_type)
    else:
        # Imagen a color
        if padding_type == 'constant':
            padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)),
                                  mode='constant', constant_values=constant_value)
        else:
            padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width), (0, 0)), mode=padding_type)

    print(f"Padded image: {padded_image.shape}")

    # Mostrar original y con padding
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    axs[0].imshow(display_image, cmap='gray' if len(image.shape) == 2 else None)
    axs[0].set_title("Original Image")
    axs[0].axis('off')

    axs[1].imshow(padded_image, cmap='gray' if len(image.shape) == 2 else None)
    axs[1].set_title(f"Padded Image ({padding_type})")
    axs[1].axis('off')

    plt.show()

    return padded_image

# Leer imagen
img = cv2.imread('padding\Turquia.jpg')  # Ajusta ruta si es necesario

# Elegir tipo de padding y valor si es 'constant'
print("Opciones de padding disponibles: constant, reflect, edge, symmetric, wrap")
padding_type = input("Introduce tipo de padding: ").strip().lower()

if padding_type == 'constant':
    try:
        constant_value = int(input("Introduce valor constante para padding (0-255): "))
    except ValueError:
        constant_value = 0
        print("Valor inválido, usando 0.")
else:
    constant_value = 0  

# Tamaño del padding
pad_h = int(input("Introduce padding en alto: "))
pad_w = int(input("Introduce padding en ancho: "))

# Aplicar padding
padded_result = padding(img, pad_height=pad_h, pad_width=pad_w,
                              padding_type=padding_type, constant_value=constant_value)

# Guardar resultado
cv2.imwrite('image_padding.jpg', padded_result)
