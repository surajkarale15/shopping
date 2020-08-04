from django.shortcuts import render

# Create your views here.

from category.models import Category

def get_active_category():
    category = Category.objects.filter(active='Y')
    return category

def welcome(req):
    return render(req,'base.html')

def welcome_category_page(req):
    # return HttpResponse("This is customer welcome page")
    return render(req, 'category.html',
                  {"note": "Welcome to Category Portal", "cat": dummy_category(), "categories": get_active_category()})


def get_list_category():
    return Category.objects.all()


def dummy_category():
    return Category(id=0, type='')


def save_or_update(req):
    msg = ''
    if req.method == 'POST':
        if int(req.POST["id"]) > 0:
            category = Category(id=req.POST["id"], type=req.POST["type"])
            msg = "Updation Operation Successfully...!"
            category.save()
        else:
            category = Category(type=req.POST["type"])
            msg = "Add Operation Successfully...!"
            category.save()

    return render(req, 'category.html',
                  {"cat": dummy_category(),
                   "note": msg, "categories": get_active_category()})


def delete_category(req, cid):
    catob = Category.objects.get(id=cid)
    catob.active = 'N'
    catob.save()
    return render(req, 'category.html',
                  {"cat": dummy_category(),
                   "note": "Category Removed Successfully...!",
                   "categories": get_active_category()})


def fetch_category(req, cid):
    catob = Category.objects.get(id=cid)
    return render(req, 'category.html',
                  {"cat": catob,
                   "note": "Category Fetched Successfully...!"
                      , "categories": get_active_category()})
