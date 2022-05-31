import os
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        file_obj = request.FILES['file']
        file_name_suffix = file_obj.name.split(".")[-1]
        if file_name_suffix not in ["jpg", "png", "gif", "jpeg", ]:
            return JsonResponse({"message": "Wrong file format"})

        upload_time = timezone.now()
        path = os.path.join(
            settings.MEDIA_ROOT,
            'tinymce',
        )
        # If there is no such path, create
        if not os.path.exists(path):
            os.makedirs(path)

        suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
        file, ext = file_obj.name.split('.')
        file_name = file +  suffix + '.' + ext
        file_path = os.path.join(path, file_name)

        file_url = f'{settings.MEDIA_URL}tinymce/{file_name}'

        # if os.path.exists(file_path):
        #     return JsonResponse({
        #         "message": "file already exist",
        #         'location': file_url
        #     })

        with open(file_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': file_url
        })
    return JsonResponse({'detail': "Wrong request"})