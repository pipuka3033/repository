from django.shortcuts import render
import random

def index(request):
    return render(request, "core/index.html")


def sign_up(request):
    return render(request, "core/sign_up.html")

def magic(request):
    if request.method == "POST":
        guess_number = int(request.POST["user_guess"])
        random_number = random.randint(0,100)
        if random_number == guess_number:
            result = "You won"
        else:
            result = f"You looose, the number was {random_number}"
        return render(request, "core/magic.html", {"result": result})
    return render(request, "core/magic.html")