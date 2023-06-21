from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm
from .utils import predict_image
from pathlib import Path

# Create your views here.

def index(request):
    result = None
    image_url = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_path = Path(settings.MEDIA_ROOT) / image.name
            with open(image_path, 'wb') as f:
                f.write(image.read())
            result = predict_image(image_path)
            image_url = settings.MEDIA_URL + image.name
    else:
        form = ImageUploadForm()

    context = {'form': form, 'result': result, 'image_url': image_url}
    return render(request, 'prediction/index.html', context)
