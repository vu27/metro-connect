from django.shortcuts import render

# Create your views here.
def home_view(request):

    pass_this_data = {
        "hello_world": "Hello World!",
        "message_from_backend": "This is how you pass data to an html page from the backend.",
    }

    return render(request, "index.html", pass_this_data)


def submitted_form_view(request):

    # Do stuff to submitted data from form
    firstName = request.POST.get("fname")
    lastName = request.POST.get("lname")

    firstAndLast = firstName + " " + lastName
    backwards = ""

    # Reverse name
    for i in range(len(firstAndLast) - 1, -1, -1):
        backwards += firstAndLast[i]

    pass_this_data = {"backwards_name": backwards}

    return render(request, "submitted-form.html", pass_this_data)