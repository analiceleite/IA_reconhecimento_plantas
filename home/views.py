from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings


@csrf_exempt
def home(request):
    if request.method == "POST":
        plant_file = request.FILES.get("plant")
        if plant_file:
            print(f'IMAGEMMMM: {plant_file}')
            print(f'IMAGEMMMM NAMMEEEE: {plant_file.name}')
            return post_plant_classify(request, plant_file)
        return render(request, 'homepage.html', {"status":"Imagem não encontrada!"})
    return render(request, 'homepage.html')


def post_plant_classify(request, image_file):
    if not image_file:
        return JsonResponse({'error': 'No image uploaded'}, status=400)

    file_path = os.path.join(settings.MEDIA_ROOT, 'images', image_file.name)

    with open(file_path, 'wb+') as media:
        for chunk in image_file.chunks():
            media.write(chunk)
    
    if os.path.exists(file_path):
        print(settings.MEDIA_URL)
        return render(request, 'homepage.html', {
            "image":{"class":"sunflower", 
            "src":image_file.name
        }})

    # image_bytes = image_file.read()
    # class_id = classify_image(image_bytes)
    
    # classes = ['Apple scab', 'Apple rot', 'Apple healthy', 'Cedar rust']
    # return JsonResponse({'class_id': class_id, 'class_name': classes[class_id]})



        