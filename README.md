# img2snes

img2snes is a Python program that converts an image to a SNES-compatible format, 8bpp format. The program takes an image file in BMP, PNG, or JPEG format and converts it to a 256-color image with a palette that can be used on the Super Nintendo Entertainment System (SNES). The program then creates a tileset, a tilemap, and a palette file that can be used in SNES game development, mainly for intros.

## Requirements

- Python 3.6 or higher
- Pillow library (can be installed using `pip install pillow`)

## Usage

1. Clone the repository to your local machine.
2. Open a terminal window and navigate to the project directory.
3. Run the `img2snes.py` file using Python:

```
python img2snes.py
```

4. Enter the name of the image file you want to convert when prompted.
5. Wait for the program to finish running. The converted files will be saved in the same directory as the original image file.

## Supported Formats

img2snes supports the following file formats:

- BMP
- PNG
- JPEG

## Output Files

img2snes outputs the following files:

- `intro.set`: the tileset file, containing the tiles used in the image.
- `intro.map`: the tilemap file, containing the arrangement of tiles used in the image.
- `intro.col`: the palette file, containing the 256-color palette used in the image.

## Credits

This project was created by Douglas Diniz. 
