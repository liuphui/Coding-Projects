from PIL import Image
import os

def convertAscii(image, type, saveas, scale):
    scale = int(scale)
    
    w, h = image.size
    
    grid = []
    for i in range(h):
        grid.append(["X"] * w)
        
    pix = image.load()
    
    for y in range(h):
        for x in range(w):
            if sum(pix[x, y]) == 0:
                grid[y][x] = "#"
            elif sum(pix[x, y]) in range(1, 100):
                grid[y][x] = "X"
            elif sum(pix[x, y]) in range(100, 200):
                grid[y][x] = "%"
            elif sum(pix[x, y]) in range(200, 300):
                grid[y][x] = "&"
            elif sum(pix[x, y]) in range(300, 400):
                grid[y][x] = "*"
            elif sum(pix[x, y]) in range(400, 500):
                grid[y][x] = "+"
            elif sum(pix[x, y]) in range(500, 600):
                grid[y][x] = "/"
            elif sum(pix[x, y]) in range(600, 700):
                grid[y][x] = "("
            elif sum(pix[x, y]) in range(700, 750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "
    
    art = open(saveas, "w")
    for row in grid:
        art.write("".join(row)+"\n")
    
    art.close()
    
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    image_path = os.path.join(script_dir, "Sample_Images\\mona_lisa.jpg")
    
    image = Image.open(image_path)
    type = image.format
    
    output_dir = os.path.join(script_dir, "Output")
    saveas = os.path.join(output_dir, "mona_lisa.txt")
    
    scale = 4
    
    w, h = image.size
    resized_dir = os.path.join(script_dir, "Resized_Images")
    resized_image_path = os.path.join(resized_dir, f"resized.{type.lower()}")
    image.resize((w//scale, h//scale)).save(resized_image_path)
    
    resized_img = Image.open(resized_image_path)
    
    convertAscii(resized_img, type, saveas, scale)

if __name__ == '__main__':
    main()