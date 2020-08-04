from django.shortcuts import render

# Create your views here.
from product.models import Product
from category.models import Category

def get_active_product():
    product = Product.objects.filter(active='Y')
    return product

def welcome(req):
    return render(req,'base.html')


def welcome_product_page(req):
    # return HttpResponse("This is customer welcome page")
    return render(req, 'product.html',
                  {"note": "Welcome to Product Portal", "prod": dummy_product(),"categories":Category.objects.all(),
                   "products": get_active_product()})


def get_list_product():
    return Product.objects.all()


def dummy_product():        
    return Product(id=0, name='')


def save_or_update(req):
    msg = ''
    if req.method == 'POST':
        catid=int(req.POST["type"])
        if catid==0:
            msg="Category selection is mandetory..."
            return render(req, 'product.html',
                          {"prod": Product(id=req.POST["id"],name=req.POST["name"]),
                           "note": msg, "categories":Category.objects.all(),"products": get_active_product()})
        if int(req.POST["id"]) > 0:
            product = Product(id=req.POST["id"], name=req.POST["name"], category=Category.objects.get(id=catid))
            msg = "Updation Operation Successfully...!"
            product.save()
        else:
            product = Product(name=req.POST["name"], category=Category.objects.get(id=catid))
            msg = "Add Operation Successfully...!"
            product.save()

    return render(req, 'product.html',
                  {"prod": dummy_product(),
                   "note": msg, "categories":Category.objects.all(), "products": get_active_product()})


def delete_product(req, pid):
    prodob = Product.objects.get(id=pid)
    prodob.active = 'N'
    prodob.save()
    return render(req, 'product.html',
                  {"prod": dummy_product(),
                   "note": "Product Removed Successfully...!",
                   "categories": Category.objects.all(),
                   "products": get_active_product()})


def fetch_product(req, pid):
    prodob = Product.objects.get(id=pid)
    return render(req, 'product.html',
                  {"prod": prodob,
                   "cat":prodob,
                   "note": "Product Fetched Successfully...!",
                   "products": get_active_product(),
                   "categories":Category.objects.all()})
