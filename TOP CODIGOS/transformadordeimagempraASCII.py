#coding: utf-8
#FEITO COM CHATGPT

from PIL import Image
import numpy as np

# Mapeamento de níveis de brilho para caracteres ASCII
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Redimensiona a imagem para um novo tamanho, mantendo a proporção."""
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    """Converte a imagem para escala de cinza."""
    return image.convert("L")

def pixel_to_ascii(pixel_value):
    """Converte um valor de pixel para o caractere ASCII correspondente."""
    return ASCII_CHARS[pixel_value // 25]  # 256 / len(ASCII_CHARS) = 25

def image_to_ascii(image_path, new_width=100):
    """Converte a imagem para arte ASCII."""
    try:
        # Abrir a imagem
        image = Image.open(image_path)

        # Redimensionar e converter para escala de cinza
        image = resize_image(image, new_width)
        image = grayscale_image(image)

        # Converter cada pixel para o caractere ASCII correspondente
        ascii_str = ""
        for y in range(image.height):
            for x in range(image.width):
                pixel_value = image.getpixel((x, y))
                ascii_str += pixel_to_ascii(pixel_value)
            ascii_str += "\n"

        return ascii_str
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        return None

def save_ascii_to_file(ascii_str, filename="ascii_art.txt"):
    """Salva a arte ASCII em um arquivo de texto."""
    with open(filename, "w") as f:
        f.write(ascii_str)

if __name__ == "__main__":
    # Caminho da imagem
    image_path = "IMAGEMEXEMPLO.jpg"  # Substitua pelo caminho da sua imagem

    # Gerar a arte ASCII
    ascii_art = image_to_ascii(image_path)

    if ascii_art:
        # Exibir na tela
        print(ascii_art)

        # Salvar em um arquivo
        save_ascii_to_file(ascii_art)
        print("Arte ASCII salva em 'ascii_art.txt'")


#FEITO COM CHATGPT