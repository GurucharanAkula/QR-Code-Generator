# 🔳 QR Code Generator

A lightweight **Python-based QR Code Generator** that converts user-provided URLs into QR codes. The application validates user input, generates a QR code instantly, displays it, and optionally saves it as a PNG image.

This project demonstrates the use of Python libraries for QR code generation, image handling, and basic file operations through a simple command-line interface.

---

## ✨ Features

- 🔗 Generate QR codes from URLs
- ✅ Validates user input to prevent empty URLs
- 🖼️ Displays the generated QR code instantly
- 💾 Option to save the QR code as a PNG image
- 📝 Allows users to specify a custom filename
- 📂 Displays the location where the QR code is saved
- ⚡ Simple and easy-to-use command-line interface

---

## 🛠 Tech Stack

### Programming Language

- Python

### Libraries

- qrcode
- os (Built-in Python Module)

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 📁 Project Structure

```text
QR-Code-Generator/
│
├── qrcodegenerator.py
├── requirements.txt
├── README.md
├── LICENSE
└── Screenshots.pdf
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/GuruCharanAkula/QR-Code-Generator.git
```

### Navigate to the Project Directory

```bash
cd QR-Code-Generator
```

### Install Required Library

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Execute the following command:

```bash
python qrcodegenerator.py
```

---

## 📌 How It Works

1. The application prompts the user to enter a valid URL.
2. The entered URL is validated to ensure it is not empty.
3. A QR code is generated based on the provided URL.
4. The generated QR code is displayed on the screen.
5. The user is prompted to choose whether to save the QR code.
6. If **Yes** is selected:
   - The user enters a filename.
   - The QR code is saved as a PNG image.
   - The application displays the directory where the image is stored.
7. If **No** is selected:
   - The QR code is displayed without being saved.

---

## 📷 Project Workflow

### Step 1: Enter URL

The user enters a valid URL for QR code generation.

### Step 2: Generate QR Code

The application processes the input and generates the corresponding QR code.

### Step 3: Save Confirmation

The user chooses whether to save the generated QR code.

### Step 4: Enter File Name

If saving is selected, the user enters a custom filename.

### Step 5: QR Code Saved Successfully

The application saves the QR code as a PNG image and displays the file location.

---

## 📸 Screenshots

Project screenshots demonstrating the complete workflow are available in **Screenshots.pdf**.

---

## 📌 Future Improvements

- 🎨 Custom QR code colors
- 🖼️ Logo embedding within QR codes
- 🖥️ Graphical User Interface (Tkinter/PyQt)
- 🌐 Generate QR codes for text, email, phone numbers, and Wi-Fi credentials
- 📥 Support for multiple output formats (PNG, SVG, PDF)
- 📜 QR code generation history

---

## 👨‍💻 Author

**GuruCharan Akula**

GitHub: https://github.com/GuruCharanAkula

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project helpful, consider giving it a **Star ⭐** on GitHub.
