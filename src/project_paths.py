from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
INPUT_DIR = DATA_DIR / "inputs"
OUTPUT_DIR = DATA_DIR / "outputs"
ASSETS_DIR = ROOT_DIR / "assets"
CERTS_DIR = ASSETS_DIR / "certs"
IMAGES_DIR = ASSETS_DIR / "images"
ICONS_DIR = ASSETS_DIR / "icons"
FORMS_DIR = ASSETS_DIR / "forms"
VENDOR_DIR = ASSETS_DIR / "vendor"

for folder in (DATA_DIR, INPUT_DIR, OUTPUT_DIR, ASSETS_DIR):
    folder.mkdir(parents=True, exist_ok=True)
