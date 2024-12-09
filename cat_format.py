from PIL import Image
import os

def check_image(file_path):
    try:
        img = Image.open(file_path)
        print(f"Arquivo {file_path} é uma imagem válida do tipo {img.format}")
        return True
    except:
        print(f"Arquivo {file_path} não é uma imagem válida")
        return False

# Verifique todas as imagens na pasta
folder = "dataset/cat"
for filename in os.listdir(folder):
    check_image(os.path.join(folder, filename))