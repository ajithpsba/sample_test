def image_to_binary():
    with open(r"C:\Users\admin\python_projects\sample_test\binary\test.png", "rb") as f:
        binary_data = f.read()

    with open("image.bin", "wb") as f:
        f.write(binary_data)

    print("Image converted to binary successfully!")


image_to_binary()