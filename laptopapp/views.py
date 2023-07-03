from django.shortcuts import render, HttpResponse, redirect

from .models import BankAccount


# Create your views here.
def index(request):
    return render(request, "sbi.html")


def sbi(request):
    return render(request, "sbi.html")



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
        accounts = BankAccount.objects.filter(accountno=accountno)
        if len(accounts) <= 0:
            result = "Failed"
            return render(request, "withdraw.html",
                          {"result": result, "aaccountno=accountno": accountno, "withdraw": withdraw})
        account = accounts[0]
        account.balance -= withdraw
        print("Withdraw " + withdraw)
        account.save()
        result = "Success"

    return render(request, "withdraw.html",
                  {"result": result})


def details(request):
    accountno = ""
    account = []
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

def check(request):
    return render(request, "check.html")
