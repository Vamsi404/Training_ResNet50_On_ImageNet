# 🚀 Multi-Class Image Classification with ResNet50

Welcome to the **Multi-Class Image Classification** project! This repository contains Python scripts for preprocessing and preparing a dataset of cat, dog, horse, and human images for training a ResNet50 model using the Inmagent dataset.

## 📝 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview
This project involves preparing a dataset for multi-class image classification. The script handles:
- Loading and extracting the dataset.
- Preprocessing images (resizing to 224x224).
- Assigning labels for multiple classes: Cats, Dogs, Horses, and Humans.
- Shuffling the data for training.
- Training a ResNet50 model using the Inmagent dataset.

## 📁 Project Structure
```
.
├── data/
│   ├── cats/
│   ├── dogs/
│   ├── horses/
│   └── humans/
├── models/
│   └── resnet50.h5
├── scripts/
│   └── image_preprocessing.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- TensorFlow/Keras
- OpenCV
- NumPy
- Matplotlib

### Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/Vamsi404/Training_ResNet50_On_ImageNet.git
cd Training_ResNet50_On_ImageNet.git
pip install -r requirements.txt
```

## 🛠️ Usage
Run the preprocessing script:
```bash
python scripts/image_preprocessing.py
```
This will load, preprocess, and shuffle the image data, ready for training.

## 📊 Dataset
The dataset includes images of four categories:
- 🐱 Cats
- 🐶 Dogs
- 🐴 Horses
- 👤 Humans

### Downloading the Dataset
Ensure the dataset is organized in the `data/` directory as shown in the structure.

## 🎯 Model Training
The ResNet50 model is trained using the processed dataset. You can find the model in the `models/` directory:
```bash
python scripts/train_resnet.py
```

## 📈 Results
Stay tuned for the detailed performance metrics and accuracy charts!

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.