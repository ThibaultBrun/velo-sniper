import io
from PIL import Image
import base64

def load_image_as_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def analyze_image(path: str) -> dict:
    image = Image.open(path)
    width, height = image.size
    format = image.format

    return {
        "path": path,
        "format": format,
        "width": width,
        "height": height,
        "base64": load_image_as_base64(path)
    }

if __name__ == "__main__":
    # Test rapide
    import sys
    from pprint import pprint

    if len(sys.argv) != 2:
        print("Usage: python image_analyzer.py path_to_image")
    else:
        result = analyze_image(sys.argv[1])
        pprint(result)
