from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

# Create your views here.
def home_view(request, *args,**kwargs):
    
    return HttpResponse("<h1>Hello Brian</h1>")

def tweet_detail_view(request, tweet_id, *args,**kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift or Java or iOS/Android
    return json data
    
    """
    
    data = {
        'id': tweet_id,
        # 'image_path': tweet.image.url
    }
    status = 200
    try:
        tweet = Tweet.objects.get(id=tweet_id)
        data['content'] = tweet.content
    except:
        data['message'] = 'Not Found'
        status = 404
    return JsonResponse(data,status=status) # json.dumps content='application.json'
    # return HttpResponse(f"<h1>Hello {tweet_id} - {tweet.content}</h1>")