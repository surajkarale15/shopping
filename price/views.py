from django.shortcuts import render

# Create your views here.
from product.models import Product
from price.models import Price


def get_active_price():
    price = Price.objects.filter(active='Y')
    return price



def welcome(req):
    return render(req,'base.html')


def welcome_price_page(req):
    # return HttpResponse("This is customer welcome page")
    return render(req, 'price.html',
                  {"note": "Welcome to Price Portal", "pri": dummy_price(), "products": Product.objects.all(),
                   "prices": get_active_price()})


def get_list_price():
    return Price.objects.all()


def dummy_price():
    return Price(id=0, prod_qty=0, prod_price=0.0, prod_price_qty=0.0)


def save_or_update(req):
    msg = ''
    if req.method == 'POST':
        productid = int(req.POST["name"])
        if productid == 0:
            msg = "Product selection is mandetory..."
            return render(req, 'price.html',
                          {"prod": Price(id=req.POST["id"], prod_qty=req.POST["quantity"],
                                         prod_price_qty=req.POST['pro_per_price'], prod_price=req.POST['price']),
                           "note": msg, "products": Product.objects.all(), "prices": get_active_price()})
        if int(req.POST["id"]) > 0:
            price = Price(id=req.POST["id"], prod_qty=req.POST["quantity"], prod_price_qty=req.POST['pro_per_price'],
                          prod_price=req.POST['price'], product=Product.objects.get(id=productid))
            msg = "Updation Operation Successfully...!"
            price.save()
        else:
            price = Price(prod_qty=req.POST["quantity"], prod_price_qty=req.POST['pro_per_price'],
                          prod_price=req.POST['price'], product=Product.objects.get(id=productid))
            msg = "Add Operation Successfully...!"
            price.save()

    return render(req, 'price.html',
                  {"pri": dummy_price(),
                   "note": msg, "products": Product.objects.all(), "prices": get_active_price()})


def delete_price(req, pid):
    priceob = Price.objects.get(id=pid)
    priceob.active = 'N'
    priceob.save()
    return render(req, 'price.html',
                  {"pri": dummy_price(),
                   "note": "Price Removed Successfully...!",
                   "products": Product.objects.all(),
                   "prices": get_active_price()})


def fetch_price(req, pid):
    priceob = Price.objects.get(id=pid)
    return render(req, 'price.html',
                  {"pri": priceob,
                   "cat": priceob,
                   "note": "Price Fetched Successfully...!",
                   "prices": get_active_price(),
                   "products": Product.objects.all()})
