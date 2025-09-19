from django.shortcuts import render

# Create your views here.

import random
import time


def main_page(request):
    """Respond to the URL '', delegate work to a template."""

    template_name = "restaurant/main.html"

    context = {
        "name": "Clarissa's Cafe",
        "location": "33 Harry Agganis Way, \nBoston, MA 02215",
        "hours": [
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
]


def order_page(request):
    """Respond to the URL '', delegate work to a template."""

    template_name = "restaurant/order.html"

    context = {"special": specials[random.randint(0, len(specials) - 1)]}

    return render(request, template_name, context)


def confirmation_page(request):
    """Process the form submission, and generate a confirmation."""

    template_name = "restaurant/confirmation.html"
    print(request)

    if request.POST:

        order = request.POST.getlist("order")
        # gets the list of order checkboxes that are checked
        # note to self: research getlist
        orderSelected = []
        pricesSelected = []
        for o in order:
            orderSelected.append(o.split("|")[0])
            if o.split("|")[0] in specials:
                pricesSelected.append(20)
            else:
                pricesSelected.append(int(o.split("|")[1]))

        totalPrice = sum(pricesSelected)

        pairs = []
        for p in range(len(orderSelected)):
            pairs.append((orderSelected[p], pricesSelected[p]))

        instructions = request.POST["special_instructions"]
        name = request.POST["name"]
        phoneNumber = request.POST["phone_number"]
        email = request.POST["email"]

        sendTime = time.time()
        seconds = 60 * random.randint(30, 60)
        pickUpTime = time.ctime(sendTime + seconds)

        context = {
            "pairs": pairs,
            "total": totalPrice,
            "instructions": instructions,
            "name": name,
            "phone_number": phoneNumber,
            "email": email,
            "time": pickUpTime,
        }

    return render(request, template_name=template_name, context=context)
