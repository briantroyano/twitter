from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

# Create your views here.
def home_view(request, *args,**kwargs):
    
    # return HttpResponse("<h1>Hello Brian</h1>")
    return render(request, 'pages/home.html', context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift or Java or iOS/Android
    return json data
    """
    qs = Tweet.objects.all()
    tweets_list = [{'id': x.id, 'content': x.content} for x in qs]
    data = {
        'isUser': False,
        'response':tweets_list
    }
    return JsonResponse(data)


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