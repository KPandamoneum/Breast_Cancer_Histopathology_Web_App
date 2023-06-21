# Breast Cancer Histopathology Web App

This is a simple web application built with Django that uses a PyTorch model to predict breast cancer from histopathology images.

## Dataset

The dataset used in this project is called "Breast Histopathology Images" and was obtained from Paul Mooney on Kaggle. The dataset can be found at [this link](https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images).

## Model

The PyTorch model used in this project was created by Laura Fink. You can find more information about the model and its training on [her Kaggle account](https://www.kaggle.com/allunia).

## Usage

1. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```
2. Start the Django development server:

   ```bash
   python manage.py runserver
   ```
3. Access the web application in your browser at `http://127.0.0.1:8000/`.
4. Upload a histopathology image and click the "Submit" button to get the prediction result.
5. Alternatively, you can run the `run.bat` file after you have installed the dependencies then go to the instructed link.

## License

This project is licensed under the [MIT License](LICENSE.md).
