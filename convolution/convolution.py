import numpy as np
import cv2
import matplotlib.pyplot as plt

def convolve_image_no_padding(image, kernel, average=False):
    # Mostrar imagen original en color si tiene 3 canales
    if len(image.shape) == 3:
        print(f"Original image with {image.shape[2]} channels.")
        original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        print(f"Grayscale image. Shape: {image.shape}")
        original_image = image

    # Convertir a escala de grises
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    print(f"Converted to grayscale. Shape: {gray_image.shape}")

    # Rotar kernel 180°
    kernel = np.flipud(np.fliplr(kernel))
    print(f"Kernel rotated. Shape: {kernel.shape}")

    image_row, image_col = gray_image.shape
    kernel_row, kernel_col = kernel.shape

    # Definir dimensiones de la salida sin padding
    output_row = image_row - kernel_row + 1
    output_col = image_col - kernel_col + 1
    output = np.zeros((output_row, output_col))

    for row in range(output_row):
        for col in range(output_col):
            region = gray_image[row:row + kernel_row, col:col + kernel_col]
            value = np.sum(kernel * region)
            if average:
                value /= (kernel_row * kernel_col)
            output[row, col] = value

    print(f"Output Image size (no padding): {output.shape}")

    # Asegurar valores entre 0-255
    output = np.clip(output, 0, 255).astype(np.uint8)

    # Mostrar imágenes: Original, Escala de grises, Convolución
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    axs[0].imshow(original_image)
    axs[0].set_title("Original Image")
    axs[0].axis('off')

    axs[1].imshow(gray_image, cmap='gray')
    axs[1].set_title("Escala de grises")
    axs[1].axis('off')

    axs[2].imshow(output, cmap='gray')
    axs[2].set_title("Convolved Output")
    axs[2].axis('off')

    plt.show()

    return output

# Leer imagen
img = cv2.imread('convolution\\Turquia.jpg')  # Ajusta la ruta si es necesario

# Kernel 3x3 de desenfoque
kernel = np.ones((3, 3))

# Ejecutar convolución sin padding
resultado = convolve_image_no_padding(img, kernel, average=True)

# Guardar resultado
cv2.imwrite('resultado.jpg', resultado)
