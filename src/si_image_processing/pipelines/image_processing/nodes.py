import os
from PIL import Image, ImageDraw, ImageFilter


def process_image(
    input_path: str,
    output_path: str,
    rotation_angle: int,
    filter_name: str,
    watermark_text: str,
) -> str:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"No se encontró la imagen en: {input_path}")

    # 1. Carga de la imagen original
    image = Image.open(input_path)

    # 2. Transformación Geométrica
    rotated = image.rotate(rotation_angle)

    # 3. Convolución Espacial Condicional
    if filter_name == "EMBOSS":
        filtered = rotated.filter(ImageFilter.EMBOSS)
    elif filter_name == "FIND_EDGES":
        filtered = rotated.filter(ImageFilter.FIND_EDGES)
    else:
        filtered = rotated

    # 4. Superposición de la Marca de Agua
    draw = ImageDraw.Draw(filtered)
    draw.text((20, 20), watermark_text, fill="white")

    if filtered.mode in ("RGBA", "P"):
        filtered = filtered.convert("RGB")

    filtered.save(output_path)

    return output_path