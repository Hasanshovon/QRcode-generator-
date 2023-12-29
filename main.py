import qrcode as qr
from PIL import Image


def main():
    img = qr.make("https://www.youtube.com/@kaggle")
    img.save("kaggle.png")
    Image.open('kaggle.png').show()


if __name__ == "__main__":
    main()
