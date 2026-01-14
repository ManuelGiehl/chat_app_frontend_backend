from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Chat

@csrf_exempt
def chat_view(request):
    if request.method == 'GET':
        chats = Chat.objects.all().order_by('created_at')
        chat_list = [{
            'id': chat.id,
            'name': chat.name,
            'message': chat.message,
            'created_at': chat.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } for chat in chats]
        return JsonResponse(chat_list, safe=False)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            chat = Chat.objects.create(name=data['name'], message=data['message'])
            return JsonResponse({
                'id': chat.id,
                'name': chat.name,
                'message': chat.message,
                'created_at': chat.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }, status=201)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Unvalid Data'}, status=400)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
