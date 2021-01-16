from django.forms import ModelForm, ModelChoiceField, CharField, DateField, DateInput
from . models import *
from . forms import *

class DateInput(DateInput):
    input_type = 'date'

class ExpenseTypeForm(ModelForm):
    class Meta:
        model = ExpenseType
        fields = ['expense_type_name', 'expense_name_description']

class ExpenseForm(ModelForm):
    expense_type = ModelChoiceField(queryset=ExpenseType.objects.all())
    expense_date = DateField(widget = DateInput)
    expense_amount = CharField()
    expense_description = CharField()

    class Meta:
        model = Expense
        fields = ['expense_type', 'expense_date', 'expense_amount', 'expense_description']

