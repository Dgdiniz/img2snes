from PIL import Image

class Img2Snes:
    def __init__(self):
        """
        Initializes the ImageConverter object with all the necessary instance variables.
        """
        self.img = None
        self.width = None
        self.height = None
        self.newimg = None
        self.palette = None
        self.snes_palette = []
        self.tilemap = []
        self.tiles = []

    def open_image(self, filename):
        """
        Opens the specified image file and gets its width and height.

        Args:
            filename: The name of the image file to open.
        """
        self.img = Image.open(filename)
        self.width, self.height = self.img.size

    def convert_image(self):
        """
        Converts the image to 256 colors and gets its palette.
        """
        self.newimg = self.img.convert(mode='P', colors=256)
        self.palette = bytes(self.newimg.getpalette())

    def create_snes_palette(self):
        """
        Converts the palette to SNES format.
        """
        for i in range(0, len(self.palette), 3):
            r = self.palette[i]
            g = self.palette[i+1]
            b = self.palette[i+2]
        
            self.snes_palette.append((((g & 0b11111000) << 2) & 0xff) | ((r & 0b11111000) >> 3))
            self.snes_palette.append(((b & 0b11111000) >> 1) | ((g & 0b11111000) >> 6))

    def save_palette(self):
        """
        Saves the palette to a file.
        """
        with open("intro.col", "wb") as f:
            f.write(bytes(self.snes_palette))

    def create_tilemap(self):
        """
        Creates the tilemap.
        """
        for i in range(32*32):
            self.tilemap.append(i & 0xff)
            self.tilemap.append((i & 0x3ff) >> 8)

    def save_tilemap(self):
        """
        Saves the tilemap to a file.
        """
        with open("intro.map", "wb") as f:
            f.write(bytes(self.tilemap))

    def create_tiles(self):
        """
        Creates the tiles.
        """
        for y in range(0, self.height, 8):
            for x in range(0, self.width, 8):
                block = self.newimg.crop((x, y, x+8, y+8))
                pixels = block.load()
                tile = []
                
                for bit_offset in range(0, 8, 2):
                    for i in range(8):
                        byte1 = 0
                        byte2 = 0
                        for j in range(8):
                            mask = 1 << (bit_offset)
                            byte1 |= ((pixels[j, i] & mask) << (7 - j)) >> bit_offset
                            byte2 |= ((pixels[j, i] & (mask << 1)) << (7 - j)) >> (bit_offset + 1)
                        tile.append(byte1)
                        tile.append(byte2)
                
                self.tiles.append(tile)

    def save_tiles(self):
        """
        Saves the tiles to a file.
        """
        with open("intro.set", "wb") as f:
            for tile in self.tiles:
                f.write(bytes(tile))

    def convert(self, filename):
        """
        Converts the specified image using all the different parts.

        Args:
            filename: The name of the image file to convert.
        """
        self.open_image(filename)
        self.convert_image()
        self.create_snes_palette()
        self.save_palette()
        self.create_tilemap()
        self.save_tilemap()
        self.create_tiles()
        self.save_tiles()

if __name__ == '__main__':
    # Create an Img2Snes object and convert the specified image
    converter = Img2Snes()
    filename = input("Enter the file name: ")
    converter.convert(filename)

