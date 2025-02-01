# MNIST LeNet-5 Implementation
![image](https://github.com/user-attachments/assets/8a046c63-7f55-487e-86fd-fdeb8490fd5e)

# Dataset
The MNIST dataset consists of 60,000 training images and 10,000 test images of handwritten digits (0-9). Each image is 28x28 pixels in grayscale.

# Model Architecture (LeNet-5)
- **Input Layer**: 28×28 grayscale images  
- **Conv Layer 1**: 32 filters (5×5), ReLU activation  
- **MaxPooling Layer 1**: 2×2 pooling  
- **Conv Layer 2**: 64 filters (5×5), ReLU activation  
- **MaxPooling Layer 2**: 2×2 pooling  
- **Flatten Layer**  
- **Fully Connected Layer 1**: 120 neurons, ReLU activation  
- **Fully Connected Layer 2**: 84 neurons, ReLU activation  
- **Output Layer**: 10 neurons (Softmax for classification)
  
# Features
- Implemented LeNet-5 architecture using TensorFlow/Keras
- Trained on the MNIST dataset (28×28 grayscale images)
- Utilizes CNNs for feature extraction and classification
- Evaluates model performance using accuracy metrics
- Developed a user-friendly interface using Streamlit for real-time digit recognition

# Prerequisites
- Python 3.x
- NumPy
- Matplotlib
- Seaborn
- Pillow
- TensorFlow
- Keras
- Streamlit
- Streamlit-Drawable-Canvas

# Getting Started
1. Clone the repository:
   ```bash
   https://github.com/Sam783/LeNet-MNIST.git
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
