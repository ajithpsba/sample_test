def binary_to_image():
    with open("image.bin", "rb") as f:
        binary_data = f.read()

    with open("restored_image.jpg", "wb") as f:
        f.write(binary_data)

    print("Binary converted to image successfully!")


binary_to_image()