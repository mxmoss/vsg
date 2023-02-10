from django.db import models
from datetime import datetime

class Customer(models.Model):
    cust_id = models.CharField(max_length=100)
    cust_name = models.CharField(max_length=100)
    add_date = models.DateTimeField('date added', default=datetime.now, blank=True)
    # Metadata
    class Meta:
        ordering = ['cust_name']
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.cust_name

class License(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    license_no = models.CharField(max_length=100)
    license_in_use = models.BooleanField()
    active_ind = models.BooleanField(default=True)
    replay_ind = models.BooleanField(default=True)
    studio_ind = models.BooleanField(default=True)
    review_ind = models.BooleanField(default=True)
    slomo_ind = models.BooleanField()
    dante_ind = models.BooleanField()
    uhd_ind = models.BooleanField()
    add_date = models.DateTimeField('date added', default=datetime.now, blank=True)
    # Metadata
    class Meta:
        ordering = ['license_no']
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.license_no

class Proxy(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    ip_in = models.GenericIPAddressField(blank=True, null=True)
    ip_out = models.GenericIPAddressField(blank=True, null=True)
    mac_address = models.CharField(max_length=32)
    program_id = models.CharField(max_length=100)
    program_name = models.CharField(max_length=100)
    io_mode = models.CharField(max_length=10)
    add_date = models.DateTimeField('date added', default=datetime.now, blank=True)
    # Metadata
    class Meta:
        ordering = ['program_name']
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id


