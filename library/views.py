from django.shortcuts import render, redirect
from django.views import View
from .models import Foods, Chefs, Contact


class HomeView(View):
    def get(self, request):
        foods = Foods.objects.all()
        chefs = Chefs.objects.all()
        context = {
            "foods": foods,
            "chefs": chefs
        }
        return render(request, "sign/index.html", context)


class AboutView(View):
    def get(self, request):
        return render(request, "sign/about.html")

class Services(View):
    def get(self, request):
        return render(request, "sign/services.html")

class Menu(View):
    def get(self, request):
        return render(request, "sign/menu.html")

class Booking(View):
    def get(self, request):
        return render(request, "sign/booking.html")

class Ourteam(View):
    def get(self, request):
        return render(request, "sign/team.html")

class Testimonials(View):
    def get(self, request):
        return render(request, "sign/testimonial.html")

class ContactView(View):
    def get(self, request):
        return render(request, "sign/contact.html")

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        return redirect('home_view')