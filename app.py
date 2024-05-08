from flask import Flask, render_template, request, send_file
import os
from pdftotext import client_info_dict, preferrence_info_dict, payment_info_dict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def convert_pdf_to_word(pdf_file):
    # Save the uploaded PDF file temporarily
    pdf_path = "temp.pdf"
    pdf_file.save(pdf_path)
    
    # Call your existing Python code to convert PDF to Word
    os.system("python pdftotext.py")
    
    # Return the path to the generated Word file
    return "output.docx"

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        if pdf_file:
            word_file = convert_pdf_to_word(pdf_file)
            return send_file(word_file, as_attachment=True, attachment_filename='converted_word.docx')

if __name__ == '__main__':
    app.run(debug=True)