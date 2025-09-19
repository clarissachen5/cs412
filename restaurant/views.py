# File: restaurant/view.py
# Author: Clarissa Chen (clchen5@bu.edu), 9/19/2025
# Description: Views specific to restaurant app
from django.shortcuts import render

import random
import time


def main_page(request):
    """Respond to the URL 'main', delegate work to main template."""

    template_name = "restaurant/main.html"

    context = {
        "name": "Clarissa's Cafe",
        "location": "33 Harry Agganis Way, \nBoston, MA 02215",
        "hours": [  # array of arrays to easily display in table in hmtl
            ["Sunday", "8am-5pm"],
            ["Monday", "8am-2pm"],
            ["Tuesday", "8am-2pm"],
            ["Wednesday", "8am-5pm"],
            ["Thursday", "8am-5pm"],
            ["Friday", "8am-10pm"],
            ["Saturday", "10am-10pm"],
        ],
        "images": [
            "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-1273516682.jpg?c=original",
        ],
    }

    return render(request, template_name, context)


specials = [
    "Beef BBQ Ribs",
    "Brisket",
    "Deviled Eggs",
    "Mac and Cheese",
    "Smoked Turkey",
    "Tallow Mashed Potatoes",
    "Fish and Chips",
]  # daily specials


def order_page(request):
    """Respond to the URL 'order', delegate work to order template."""

    template_name = "restaurant/order.html"

    context = {
        "special": specials[random.randint(0, len(specials) - 1)]
        # picks a random special
    }

    return render(request, template_name, context)


def confirmation_page(request):
    """Process the order form submission, and generate a confirmation,
    delegate work to confirmation template."""

    template_name = "restaurant/confirmation.html"
    print(request)

    if request.POST:

        order = request.POST.getlist("order")
        # gets the list of order checkboxes that are checked

        orderSelected = []
        pricesSelected = []

        # separates ordered dish names and prices and converts prices to ints
        for o in order:
            orderSelected.append(o.split("|")[0])
            if o.split("|")[0] in specials:
                pricesSelected.append(20)
            else:
                pricesSelected.append(int(o.split("|")[1]))

        totalPrice = sum(pricesSelected)

        # combines ordered dish names and int prices
        pairs = []
        for p in range(len(orderSelected)):
            pairs.append((orderSelected[p], pricesSelected[p]))

        special_instructions = request.POST["special_instructions"]
        name = request.POST["name"]
        phone_number = request.POST["phone_number"]
        email = request.POST["email"]

        # create pick up time
        current_time = time.time()
        seconds = 60 * random.randint(30, 60)
        pick_up_time = time.ctime(current_time + seconds)

        context = {
            "pairs": pairs,
            "total": totalPrice,
            "special_instructions": special_instructions,
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "time": pick_up_time,
        }

    return render(request, template_name=template_name, context=context)
