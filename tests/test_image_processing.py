import os
import sys

# Asegúrate de que estas líneas inicien pegadas al borde izquierdo (sin espacios)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from si_image_processing.pipelines.image_processing.nodes import process_image  # noqa: E402


def test_process_image():
    input_img = "data/01_raw/marte.jpg"
    output_img = "data/03_primary/test_output.jpg"

    # Eliminar residuo anterior si existe
    if os.path.exists(output_img):
        os.remove(output_img)

    # Ejecución de prueba controlada
    result = process_image(
        input_path=input_img,
        output_path=output_img,
        rotation_angle=45,
        filter_name="EMBOSS",
        watermark_text="Test UCV",
    )

    # Aserciones lógicas
    assert result == output_img
    assert os.path.exists(output_img)