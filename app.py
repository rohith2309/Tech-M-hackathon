from flask import Flask, render_template
from flask import request
from PIL import Image   
import pytesseract
import os
from Generation import generate_summary
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

    
    if request.method == 'POST':
        try:
            # Check if an image was uploaded
            if 'image' not in request.files:
                error = "No image uploaded"
                return render_template('index.html', error=error)
            
            image = request.files['image']
            
            # Check if the file is actually uploaded
            if image.filename == '':
                error = "No image selected"
                return render_template('index.html', error=error)
            
            # Save the image temporarily
            image_path = os.path.join('uploads', image.filename)
            os.makedirs('uploads', exist_ok=True)
            image.save(image_path)
            
            # Process the image with OCR
            img = Image.open(image_path)
            gen = pytesseract.image_to_string(img)
            text=generate_summary(gen)
            
            # Clean up - remove the temporary file
            os.remove(image_path)
            
            result = text if text.strip() else "No text detected in the image"
            
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    
    return render_template('index.html', result=result, error=error)
if __name__ == '__main__':
    app.run(debug=True)