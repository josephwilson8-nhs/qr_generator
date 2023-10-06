import argparse
from pathlib import Path
import qrcode
from qrcode.image import pil


QR_OUTPUT_DIR = Path("./generated_qr_codes")
QR_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_qr_code(url: str, name: str) -> Path:
    """
    Generates a QR code based on the url passed and saves it as a png with the name
    provide.

    Parameters
    ----------
    url : str
        QR URL
    name : str
        Name of the QR code file to save it under

    Returns
    -------
    Path
        Path to the saved QR code
    """
    factory = pil.PilImage
    img = qrcode.make(data=url, image_factory=factory)
    path = QR_OUTPUT_DIR / f"{name}.png"
    img.save(path)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate QR codes from URLs")
    parser.add_argument("url", help="The URL to encode as a QR code", default="")
    parser.add_argument("name", help="Name to use for the output files", default="default_qr")
    args = parser.parse_args()

    png_file = generate_qr_code(url=args.url, name=args.name)

    print(f"QR code saved to: {png_file}")
