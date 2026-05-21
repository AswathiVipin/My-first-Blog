
from django.shortcuts import render


def home(request):
   posts = [
   {
   "title": "First Blog Post",
   "content": "This is my first Django blog post."
   },
   {
    "title": "Learning Django",
    "content": "Django makes web development easy."
   },
   {
    "title": "Templates in Django",
    "content": "Django templates help separate logic and HTML."
   },
   {
    "title": "Templates in Django",
    "content": "Django templates help separate logic and HTML."
   }
  ]
   return render(request, "home.html", {"posts": posts})
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
