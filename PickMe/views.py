from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from bookings.models import rideBook
from services.models import service
from vehicles.models import vehicles

import random
from django.contrib import messages


def main(request):
    return render(request, "loading.html")


def about(request):
    return render(request, "about.html")


def home(request):
    print(request)
    return render(request, "home.html")


def user_login(request):
    data = {"msg": "Incorrect User Name or Password"}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home/", user)
        else:
            return render(request, "login.html", data)

    return render(request, "login.html")


def myrides(request):
    rides = rideBook.objects.filter(booked_by=request.user.username)
    return render(request, "myrides.html", {"user_rides": rides})


# def registration(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         print(username)
#         print(email)
#         print(password)
#         user = User.objects.create_user(
#             username=username, email=email, password=password
#         )
#         user.save()
#         return redirect("/login/")

#     return render(request, "registration.html")


def registration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            user.save()
            messages.success(request, "Registration successful.")
            return redirect("/login/")
        else:
            messages.error(request, "Username already exists.")

    return render(request, "registration.html")


def ride(request):
    print("Hello")
    if request.method == "POST":
        pick_loc = request.POST.get("pick_loc")
        drop_loc = request.POST.get("drop_loc")
        ride = request.POST.get("rtype")
        vehicle = request.POST.get("vtype")
        userob = request.user.username
        if ride != "-" and vehicle != "=":
            print("Checking availbility")
            availability = vehicles.objects.filter(available=True, vehicle_class=ride)
            if availability.exists():
                print("Storing data")
                car = random.choice(availability)
                data = rideBook(
                    pick_loc=pick_loc,
                    drop_loc=drop_loc,
                    vehicle_class=ride,
                    vehicle_type=vehicle,
                    booked_by=userob,
                    car=car.reg_num,
                )
                data.save()
                car_data = get_object_or_404(vehicles, reg_num=car.reg_num)
                car_data.available = False
                car_data.save()
            else:
                print("Not storing data")
                redirect("/home/", {"msg": "No vehicles available"})
    return render(
        request,
        "ridebooking.html",
    )


def terms(request):
    return render(request, "terms_and_conditions.html")


def services(request):
    user = service.objects.all()
    data = {"service": user}
    return render(request, "rideservices.html", data)


def contact(request):
    return render(request, "contact.html")
