# Mango-Cutter
Cuts single file manga images into 2 separate images.

**REQUIRES CONFIGURING `main.py` BEFORE USE!!**

Writes images as `.png` by default.

## Usage:
`--input_format=<Image format>` - Ex: `--input_format=jpg`<br/>
`--input=<Input directory of PNGs>` - Ex: `--input=IMAGES`<br/>
`--output=<Output directory of processed images>` - Ex: `--output=PROCESSED` <br/>

Example:
```bash
python main.py --input_format=jpg --input=IMAGES --output=PROCESSED
```

## Requirements:
- Python 3.11
- [Pillow](https://pypi.org/project/Pillow/) - [9.4.0](https://pypi.org/project/Pillow/9.4.0/)
