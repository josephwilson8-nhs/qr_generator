"""
Creates QR Code based off of user inputs and saves to file.
"""
from pathlib import Path
from typing import Tuple
import inquirer
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
    url = str(inquirer.text(message="Input the URL to encode as a QR code"))
    name = str(inquirer.text(message="Input the name to use for the output files"))

    png_file = generate_qr_code(url=url, name=name)

    print(f"QR code saved to: {png_file}")
