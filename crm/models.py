from django.db import models

# Create your models here.

class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name="Status Name")


    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status names'

class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name="Name")
    order_phone = models.CharField(max_length=200, verbose_name="Phone")
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Status')


    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Proposal")
    comment_field = models.TextField(verbose_name='Comment')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name="Date of write comment")

    def __str__(self):
        return self.comment_field

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'