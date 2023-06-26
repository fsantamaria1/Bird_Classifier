

# Bird Classifier

This repository contains a bird species classification application that allows users to upload an image of a bird and get the predicted species using a trained machine learning model. The application utilizes Streamlit, a Python library for creating interactive web apps, to provide a user-friendly graphical user interface (GUI) for the bird classification functionality.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Introduction

The Bird Classifier application is designed to identify the species of a bird based on an input image. It leverages a pre-trained machine learning model that has been fine-tuned on bird species data. The application provides an intuitive user interface where users can upload an image and receive the predicted bird species.

## Getting Started

To get started with the Bird Classifier application, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/your-username/Bird_Classifier.git
```

2. Navigate to the repository directory:

```shell
cd Bird_Classifier
```

3. Install the required dependencies by running:

```shell
pip install -r requirements.txt
```

4. Launch the application locally using the following command:

```shell
streamlit run main.py
```

5. Access the application by visiting `http://localhost:8501` in your web browser.

## Usage

Once the Bird Classifier application is running, you can follow these steps to classify bird species:

1. Upload an image of a bird using the file upload widget provided.
2. Click the "Get Bird Species" button to initiate the classification process.
3. Wait for the application to process the image and display the predicted bird species.
4. The predicted bird species will be shown under the "Predicted Bird Species" section.

Please note that the accuracy of the predictions may vary based on the quality of the input image and the performance of the trained model.

## Folder Structure

The repository follows a specific folder structure to organize the necessary data and models. Here is an overview of the folders and files:

- `data/birds.csv`: Contains data about the bird classes, including class, file paths, labels, data set, and scientific names.
- `data/models/original_bird_model`: Saved model from the original [Bird Classification repository](https://github.com/fsantamaria1/Bird_Classification.git).
- `data/models/improved_bird_model`: Saved model from the improved [Bird Classification repository](https://github.com/fsantamaria1/Bird_Classification.git).
- `data/test_images/`: Directory containing sample images of birds that can be used for testing purposes.

Please make sure to organize your data and models according to this structure to ensure the application can access them correctly.

## Dependencies

The Bird Classifier application relies on the following dependencies:

- streamlit==1.23.1
- pandas==1.0.2
- numpy==1.23.5
- matplotlib==3.7.1
- tensorflow==2.12.0

These dependencies are specified in the `requirements.txt` file. You can install them using the command mentioned in the "Getting Started" section.

## Contributing

Contributions to the Bird Classifier application are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request. Your contributions can help enhance the accuracy, usability, and performance of the bird species classification functionality.
