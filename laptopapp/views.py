from django.shortcuts import render, HttpResponse, redirect
from .models import LaptopModel

from .models import BankAccount


# Create your views here.
def index(request):
    return HttpResponse("Hello Main")


def sbi(request):
    return render(request, "sbi.html")


def create(request):
    print("Create")
    sno = ""
    company_name = ""
    Ram = ""
    Rom = ""
    Model_name = ""
    price = ""
    if request.GET:
        sno = request.GET["sno"]
        company_name = request.GET["Company_name"]
        Ram = request.GET["Ram"]
        price = request.GET["price"]
        Rom = request.GET["Rom"]
        Model_name = request.GET["Model_name"]
        l = LaptopModel()
        l.sno = sno
        l.Company_name = company_name
        l.Ram = Ram
        l.Price = price
        l.Rom = Rom
        l.Model_name = Model_name
        l.save()
        print(sno, company_name, Ram, Rom, Model_name, price)

    return render(request, "create.html",
                  {"company_name": company_name, "Model_name": Model_name, "price": price, "sno": sno, "Ram": Ram,
                   "Rom": Rom, })


def search(request):
    sno = ""
    company_name = ""
    Ram = ""
    Rom = ""
    Model_name = ""
    price = ""
    if request.GET:
        price = request.GET["price"]
        laptops = LaptopModel.objects.filter(Price=price)
        n = len(laptops)
        if n <= 0:
            company_name = "not found"
            Ram = "not found"
            Rom = "not found"
            Model_name = "not found"
        else:
            l = laptops[0]
            company_name = l.Company_name
            Model_name = l.Model_name
            Ram = l.Ram
            Rom = l.Rom
        print(price)

    return render(request, "search.html",
                  {"company_name": company_name, "Model_name": Model_name, "price": price, "sno": sno, "Ram": Ram,
                   "Rom": Rom, })


def update(request):
    return render(request, "update.html")


def delete(request):
    Company_name = ""
    result = "Not deleted"
    if request.GET:
        Company_name = request.GET["company_name"]
        laptops = LaptopModel.objects.filter(Company_name=Company_name)
        n = len(laptops)
        if n > 0:
            Laptop = laptops[0]
            Laptop.delete()
            result = "Deleted"
        # Book.delete(bookname)
    return render(request, "delete.html", {"Company_name": Company_name, "result": result})


def Alllaptops(request):
    price
    laptops = LaptopModel.objects.all()
    print(laptops)
    return render(request, "All laptops.html", {"laptops": laptops})


def Price(request):
    Price = ""
    if request.GET:
        price = request.GET["price"]
        laptops = LaptopModel.objects.all().filter(Price=price)
        # print(laptops, Price)
    return render(request, "All laptops.html", {"laptops": laptops, "price": price})


def between(request):
    minprice = ""
    maxprice = ""
    laptops = LaptopModel.objects.all()
    if request.GET:
        minprice = request.GET["minprice"]
        maxprice = request.GET["maxprice"]
        laptops = LaptopModel.objects.all().filter(Price__gt=minprice) & LaptopModel.objects.all().filter(
            Price__lt=maxprice)
    return render(request, "between.html", {"laptops": laptops, "maxprice": maxprice, "minprice": minprice})


def account(request):
    accountno = ""
    name = ""
    balance = ""
    result = "Fill the details"
    if request.GET:
        try:
            accountno = request.GET["accountno"]
            name = request.GET["name"]
            balance = request.GET["balance"]
            a = BankAccount()
            a.accountno = accountno
            a.name = name
            a.balance = balance
            a.save()
            result = "Successfully account created"
        except  Exception as e:
            result = "Error" + str(e)
        # return redirect(sbi)
        print(accountno, name, balance)
    return render(request, "account.html", {"accountno": accountno, "name": name, "balance": balance, "result": result})


def deposit(request):
    result = ""
    accountno = ""
    amounttodeposit = 0
    balance = ""
    if request.GET:
        accountno = request.GET["accountno"]
        # accountno=1
        amounttodeposit = int(request.GET["amount_deposit"])
        accounts = BankAccount.objects.filter(accountno=accountno)
        # amounttodeposit=900
        if len(accounts) <= 0:
            result = "Failed"
            return render(request, "deposit.html",
                          {"result": result, "accountno": accountno, "amounttodeposit": amounttodeposit})

        account = accounts[0]
        account.balance += amounttodeposit
        account.save()
        # if request <= 0:
        #     new_balance = deposit + balance
        result = "Success"

    return render(request, "deposit.html",
                  {"result": result})


def withdraw(request):
    result = ""
    accountno = ""
    withdraw = 0
    if request.GET:
        accountno = request.GET["accountno"]
        withdraw = int(request.GET["withdraw"])
        accounts = BankAccount.objects.filter()
        if len(accounts) <= 0:
            result = "Failed"
            return render(request, "withdraw.html",
                          {"result": result, "aaccountno=accountno": accountno, "withdraw": withdraw})
        account = accounts[0]
        account.balance -= withdraw
        account.save()
        result = "Success"

    return render(request, "withdraw.html",
                  {"result": result})


def details(request):
    accountno = ""
    account=[]
    if request.GET:
        accountno = request.GET["accountno"]
        accounts = BankAccount.objects.filter(accountno=accountno)
        if len(accounts) <= 0:
            account = BankAccount()
        else:
            account = accounts[0]
        # a.accountno = accountno
        print(accounts)
    return render(request, "details.html", {"account": account, "accountno": accountno})
