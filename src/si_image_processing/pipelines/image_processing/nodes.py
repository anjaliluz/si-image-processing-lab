import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont

def process_image(
    input_path: str,
    output_path: str,
    rotation_angle: int,
    filter_name: str,
    watermark_text: str
) -> str:
    # 1. Cargar la imagen original
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"No se encontró la imagen en: {input_path}")
        
    image = Image.open(input_path)
    
    # 2. Aplicar rotación geométrica
    processed = image.rotate(rotation_angle, expand=True)
    
    # 3. Aplicar filtro convolucional paramétrico
    if filter_name == "EMBOSS":
        processed = processed.filter(ImageFilter.EMBOSS)
    elif filter_name == "FIND_EDGES":
        processed = processed.filter(ImageFilter.FIND_EDGES)
    elif filter_name == "BLUR":
        processed = processed.filter(ImageFilter.BLUR)
        
    # 4. Inyección de la marca de agua (Texto dinámico)
    draw = ImageDraw.Draw(processed)
    # Colocar en una esquina de la imagen
    draw.text((20, 20), watermark_text, fill="white")
    
    # [CORRECCIÓN CRÍTICA]: Forzar conversión a RGB para evitar error RGBA en JPEG
    if processed.mode in ("RGBA", "P"):
        processed = processed.convert("RGB")
        
    # 5. Asegurar directorio de salida y guardar producto analítico
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    processed.save(output_path, "JPEG")
    
    return output_path