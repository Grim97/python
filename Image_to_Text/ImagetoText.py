import pytesseract
try:
    from PIL import Image
except ImportError as e:
    print(e)
    import Image
# Import sequences along with exception handling

def convertor(path):
    try:
        converted = print(pytesseract.image_to_string(Image.open(path), lang= 'jpn+eng'))
        # Tesseract function that converts image to text
        print(converted)
    except FileNotFoundError as x:
        print("Mentioned file is not found -", x)
        # If mentioned file not found, this would handle that exception


def main():
    path = input("Enter the path of image with file name")
    # User enters path of image along with filename
    convertor(path)


if __name__ == "__main__":
    main()
