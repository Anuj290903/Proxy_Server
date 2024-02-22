import requests
from django.http import HttpResponse

def proxy_view(request):
    try:
        # Make a request to the target URL
        response = requests.get('https://codingchallenges.substack.com/feed')

        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            return HttpResponse(response.content, content_type='text/xml')
        else:
            # Return an error response if the request was not successful
            return HttpResponse(status=response.status_code)

    except Exception as e:
        # Handle errors
        return HttpResponse({'error': str(e)}, status=500)
