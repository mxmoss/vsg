from django.db import models

class Customer(models.Model):
    custId_text = models.CharField(max_length=200)
    custName_text = models.CharField(max_length=200)
    licenseId_text = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added')

class Node(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    nodeId = models.CharField(max_length=200)
    macAddress = models.CharField(max_length=200)
    ioMode = models.IntegerField(default=0)
    programId = models.CharField(max_length=200)
    programName = models.CharField(max_length=200)
    bridgeIP = models.CharField(max_length=200)
    bridge = models.CharField(max_length=200)

