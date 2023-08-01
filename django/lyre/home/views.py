from django.shortcuts import render
from django.http import JsonResponse
from fuzzywuzzy import fuzz
from .models import Lyre
from django.core.serializers.json import DjangoJSONEncoder

def dataReq(request):
    try:
        query = request.GET.get('q')
        print(query)
        songs = Lyre.objects.filter(lyrics__icontains=query)
        matches = sorted(songs, key=lambda x: fuzz.partial_ratio(x.lyrics, query), reverse=True)[:10]
        results = [{'name': data.name, 'lyrics': data.lyrics, 'song': data.song.url if data.song else None} for data in matches]
        print(results)
        return JsonResponse(results, safe=False)
    except Exception as e:
        # Handle the exception here
        print(str(e))
        return JsonResponse({'error': 'An error occurred'}, status=500)


def search_songs(request):
    return render(request,'index.html')