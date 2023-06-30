from django.shortcuts import render
from .models import Product


def show_product_form(request):
    """show the product form and show all the available product in dropdown from the database

    Args:
        request (HttpRequest): Incoming client Http Request

    Returns:
        HttpResponse: On success render the show_product page with list of the products available in the database
        On error render the error page with the message

    """
    try:
        # get all the products
        products = Product.objects.all()
        print(products)
        return render(request, "show_product.html", {"products": products})
    except Exception as ex:
        return render(request, "error.html", {"message": f"Exception occur: {ex}"})


def show_update_form(request):
    """show the update form and show all the available product in dropdown from the database so easily can update the product

    Args:
        request (HttpRequest): Incoming client Http Request

    Returns:
        HttpResponse: On success render the update_product page with list of the products available in the database
        On error render the error page with the message
    """
    try:
        # get all the products
        products = Product.objects.all()
        return render(request, "update_product.html", {"products": products})
    except Exception as ex:
        return render(request, "error.html", {"message": f"Exception occur: {ex}"})


def show_delete_form(request):
    """show the delete form and show all the available product in dropdown from the database so easily can delete the product

    Args:
        request (HttpRequest): Incoming client Http Request

    Returns:
        HttpResponse: On success render the delete_product page with list of the products available in the database
        On error render the error page with the message
    """
    try:
        # get all the products
        products = Product.objects.all()
        return render(request, "delete_product.html", {"products": products})
    except Exception as ex:
        return render(request, "error.html", {"message": f"Exception occur: {ex}"})


def remove_product(request):
    """deleting the product by the provided name

    Args:
        request (HttpRequest): Incoming Http Request made by the client

    Returns:
        HttpResponse: On success return success.html and on error return the error.html
    """
    try:
        try:
            # get the product form the database using name
            product = Product.objects.get(name=request.POST["name"])
        except Product.DoesNotExist:
            # render error.html if product not found from the database
            return render(request, "error.html", {"message": "Product Not Exist"})
        # delete the product
        product.delete()
        return render(
            request, "success.html", {"message": "product deleted successfully"}
        )
    except Exception as ex:
        return render(request, "error.html", {"message": f"Exception occur {ex}"})


def show_product(request):
    """searching one product form the database using name

    Args:
        request (HttpRequest): Incoming Http Request made by the client

    Returns:
        HttpResponse: On Success render html page with that product on error return error.html with message
    """
    try:
        try:
            # get the product form the database using name
            product = Product.objects.get(name=request.POST["name"])
        except Product.DoesNotExist:
            # render error.html if product not found from the database
            return render(request, "error.html", {"message": "Product Not Exist"})

        return render(request, "show_products.html", {"products": [product]})
    except Exception as ex:
        return render(request, "error.html", {"message": f"Exception occur {ex}"})


def show_products(request):
    """show all the products available in the database

    Args:
        request (HttpRequest): Incoming Http Request made by the client

    Returns:
        HttpResponse: On success return the show_all_product.html and show
        all the product available in the database, On error return the error.html
    """
    try:
        # get all the products
        products = Product.objects.all()
        return render(request, "show_products.html", {"products": products})
    except Exception as ex:
        return render(request, "error.html", {"message": f"Exception occur: {ex}"})


def insert_product(request):
    """Inserting the product in the database

    Args:
        request (HttpRequest): Incoming Http Request made by the client

    Returns:
        HttpResponse: On successfully added to the database render success.html and on error render error.html
    """
    try:
        if request.method == "POST":
            # getting the information of the product from the form
            name = request.POST["name"]
            price = request.POST["price"]
            quantity = request.POST["quantity"]
            product = Product(name=name, price=price, quantity=quantity)
            # saving the product in database
            product.save()
            return render(
                request, "success.html", {"message": "product added successfully"}
            )
        # return the error.html if error in the request
        return render(
            request,
            "error.html",
            {"message": f"error in request \n request method :{request.method}"},
        )
    # return the error.html with message if any exception raised
    except Exception as ex:
        return render(request, "error.html", {"message": f"exception occur: {ex}"})


def update_product(request):
    """update the product by the provided information in the form

    Args:
        request (HttpRequest): Incoming Http Request made by the client

    Returns:
        HttpResponse: On success return the success.html and On error return the error.html with proper message
    """
    try:
        name = request.POST["product"].split(";")[2]
        try:
            # get the product from the database using name
            product = Product.objects.get(name=name)
        # raise exception if product not found in database
        except Product.DoesNotExist:
            return render(request, "error.html", {"message": "Product Not Exist"})

        # getting the information to update in the product form the from
        product.price = request.POST["price"]
        product.quantity = request.POST["quantity"]

        # saving the product in the database
        product.save()
        return render(
            request, "success.html", {"message": f"Product {name} updated successfully"}
        )

    # return the error.html with message if any exception raised
    except Exception as ex:
        return render(request, "error.html", {"message": f"exception occur: {ex}"})
