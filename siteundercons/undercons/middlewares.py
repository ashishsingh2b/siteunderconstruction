from django.shortcuts import render,HttpResponse

class UnderConstruction:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Call from Middleware")
        # Render the under construction template
        response = render(request, 'siteuc.html')
        #response =HttpResponse("The site is under Construction")
        print("Call from middleware after View")
        return response
