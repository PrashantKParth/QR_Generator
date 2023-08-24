# QR_Generator
Generate a QR code and also Generate a red-and-white QR code using qrcode and PIL libraries to Convert the link to a QR code image and save it as '.png' for easy sharing and access. Customizable version, error correction, and visual styles ensure efficient and appealing output.

# Step-by-step explanation of the code:

1. **Importing Libraries**: The code starts by importing the necessary libraries.
   - `qrcode`: This library is used for generating QR codes.
   - `PIL` (Python Imaging Library): This library is used for creating and manipulating images.

2. **Creating QR Code Generator Object**:
   ```python
   qr = qrcode.QRCode(version=1,
                      error_correction=qrcode.constants.ERROR_CORRECT_H,
                      box_size=10, border=4)
   ```
   Here, a `QRCode` object is created from the `qrcode` library. The parameters passed to the object have the following meanings:
   - `version=1`: Specifies the QR code version. In this case, it's version 1.
   - `error_correction=qrcode.constants.ERROR_CORRECT_H`: Sets the error correction level to high.
   - `box_size=10`: Defines the size of each box (or module) in the QR code.
   - `border=4`: Specifies the width of the border around the QR code.

3. **Adding Data to QR Code**:
   ```python
   qr.add_data("https://www.linkedin.com/in/prashant-kumar-parth-246245253")
   qr.make(fit=True)
   ```
   The `add_data` method is used to provide the data you want to encode in the QR code. In this case, it's a LinkedIn profile URL. The `make` method with `fit=True` is called to generate the QR code with the provided data.

4. **Generating QR Code Image**:
   ```python
   img = qr.make_image(fill_color="red", back_color="white")
   ```
   This code generates the QR code image using the `make_image` method. The `fill_color` parameter sets the color of the QR code modules (boxes), and the `back_color` parameter sets the background color.

5. **Saving the Image**:
   ```python
   img.save("LinkedIn_Prashant.png")
   ```
   Finally, the generated QR code image is saved as a PNG file named "LinkedIn_Prashant.png" in the current working directory.

In summary, this code snippet creates a QR code containing the provided LinkedIn profile URL and saves it as an image with red modules and a white background.
