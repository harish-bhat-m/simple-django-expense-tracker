from django.db import models

class ExpenseType(models.Model):
    expense_type_name = models.CharField("Expense Name", max_length=100)
    expense_name_description = models.TextField("Description")

    def __str__(self):
        return self.expense_type_name

    class Meta:
        ordering = ['-id']

class Expense(models.Model):
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    expense_date = models.DateField("Date")
    expense_amount = models.DecimalField("Spent", max_digits=8, decimal_places=2)
    expense_description = models.TextField("Description")
 
    def __str__(self):
        return self.expense_type.expense_type_name
