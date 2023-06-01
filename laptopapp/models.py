from django.db import models


# Create your models here.
class LaptopModel(models.Model):
    sno = models.IntegerField()
    Company_name = models.CharField(max_length=50)
    Ram = models.CharField(max_length=200)
    Rom = models.CharField(max_length=200)
    Model_name = models.CharField(max_length=20)
    Price = models.IntegerField()

    def __str__(self):
        return "sno={0},Company_name={1},Ram{2},Ram{3},Model_name{4},Price{5}".format(self.sno, self.Company_name,
                                                                                      self.Ram, self.Rom,
                                                                                      self.Model_name, self.Price)


class BankAccount(models.Model):
    accountno = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    balance = models.IntegerField()

    def __str__(self):
        return "accountno={0},name={1},balance={2}".format(self.accountno, self.name, self.balance)
