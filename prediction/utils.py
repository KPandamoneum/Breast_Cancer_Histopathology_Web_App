from PIL import Image
import torch
import pickle

# Load the saved model
saved_model_path = "breast_cancer_model_full.pth"
model = torch.load(saved_model_path)

# Load the saved transform
transform_path = "breast_cancer_transform.pkl"
with open(transform_path, "rb") as f:
    transform = pickle.load(f)

def process_image(image_path, transform):
    image = Image.open(image_path).convert("RGB")
    if transform is not None:
        image = transform(image)
    return image

def predict_image(image_path):
    # Process the image
    image = process_image(image_path, transform)
    
    # Add a batch dimension and move to the same device as the model
    image = image.unsqueeze(0).to(next(model.parameters()).device)
    
    # Set the model to evaluation mode
    model.eval()
    
    # Disable gradient calculation
    with torch.no_grad():
        # Forward pass to get the predictions
        outputs = model(image)
    
    # Get the predicted class index
    _, predicted = torch.max(outputs.data, 1)
    
    # Map the class index to the corresponding label (e.g., cancer or non-cancer)
    label = "cancer" if predicted.item() == 1 else "non-cancer"
    
    return label
