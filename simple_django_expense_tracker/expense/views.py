from django.shortcuts import render, redirect
from django.db.models import Sum
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import JsonResponse
import random


from . models import *
from . forms import *

def index(request):
	expense_label = []
	expense_total = []
	label_color = []
	r = lambda: random.randint(0,255)
	queryset = Expense.objects.values('expense_type').annotate(total=Sum('expense_amount'))
	for result in queryset:
		expense_type = ExpenseType.objects.get(id=result['expense_type'])
		expense_label.append(expense_type.expense_type_name)
		expense_total.append(float(result['total']))
		label_color.append('#{:x}{:x}{:x}'.format(r(),r(),r()))
	print(label_color)
	print("Expense................")
	context = {'pie_label': expense_label,
				'pie_data': expense_total,
				'pie_color':label_color}
	
	return render(request, 'expense/index.html', context)


#def index(request):
	
	#context = {'data':'Good Morning'}
	#return render(request, 'expense/index.html', context)

def list_expense_type(request):
	""" Functionality
		Add the new expense type
		List all the expense type in paginator format
	"""
	
	context = {}
	expense_type_object = ExpenseType.objects.get_queryset().order_by('id')
	paginator = Paginator(expense_type_object,5)
	pages = request.GET.get('page')
	page_object = paginator.get_page(pages)

	expense_type_form = ExpenseTypeForm()

	if request.method == "POST":
		expense_type_form = ExpenseTypeForm(request.POST)

		if expense_type_form.is_valid():
			expense_type_form.save()
			saved_data = expense_type_form.cleaned_data['expense_type_name']
			messages.success(request, '"{}" added successfully'.format(saved_data))
		return redirect("/expense_type/")

	context['form'] = expense_type_form
	context['expense_types'] = page_object
	context['action'] = 'list'
	print(context)
	return render(request, 'expense/list_expense_type.html', context)

def update_expense_type(request, pk):
	"""Functionality
	   	Update the expene type	
	"""
	try:
		expense_object = ExpenseType.objects.get(id=pk)
		expense_type_form = ExpenseTypeForm(instance = expense_object)
		
		if request.method == "POST":
			expense_type_form = ExpenseTypeForm(request.POST, instance = expense_object)
			
			if expense_type_form.is_valid():
				expense_type_form.save()
				saved_data = expense_type_form.cleaned_data['expense_type_name']
				messages.success(request, '"{}" updated successfully'.format(saved_data))
			return redirect("/expense_type")

		context = {'form':expense_type_form, 'action':'update'}
		return render(request, 'expense/list_expense_type.html', context)

	except Exception as error:
		messages.error(request, 'Expense Type not found. May be it is already deleted')
		return redirect("/expense_type")
		

def delete_expense_type(request, pk):
	try:
		expense_object = ExpenseType.objects.get(id=pk)
		expense_type_form = ExpenseTypeForm(instance = expense_object)
		
		if request.method == "POST":
			expense_type_form = ExpenseTypeForm(request.POST)

			if expense_type_form.is_valid():
				expense_object.delete()
				saved_data = expense_type_form.cleaned_data['expense_type_name']
				messages.success(request, '"{}" deleted successfully'.format(saved_data))
			return redirect("/expense_type")

		context = {'form':expense_type_form, 'action':'delete'}
		return render(request, 'expense/list_expense_type.html', context)

	except Exception as error:
		messages.error(request, 'Expense Type not found. May be it is already deleted')
		return redirect("/expense_type")


def list_expense(request):
	""" Functionality
		Add the new transaction
		List all the expense in paginator format
	"""
	context = {}

	expense_object = Expense.objects.get_queryset().order_by('id')
	paginator = Paginator(expense_object,5)
	pages = request.GET.get('page')
	page_object = paginator.get_page(pages)

	expense_form = ExpenseForm()

	if request.method == "POST":
		expense_form = ExpenseForm(request.POST)

		if expense_form.is_valid():
			expense_form.save()
			saved_data = expense_form.cleaned_data['expense_type']
			messages.success(request, '"{}" added successfully'.format(saved_data))			

	context['form'] = expense_form
	context['expenses'] = page_object
	context['action'] = 'list'
	print(context)
	return render(request, 'expense/list_expense.html', context)


def update_expense(request, pk):
	try:
		expense_object = Expense.objects.get(id=pk)
		expense_form = ExpenseForm(instance = expense_object)
		
		if request.method == "POST":
			expense_form = ExpenseForm(request.POST, instance = expense_object)
			
			if expense_form.is_valid():
				expense_form.save()
				saved_data = expense_form.cleaned_data['expense_type']
				messages.success(request, '"{}" updated successfully'.format(saved_data))
			return redirect("/expense")
		context = {'form':expense_form, 'action':'update'}
		return render(request, 'expense/list_expense.html', context)
	except Exception as error:
		messages.error(request, 'Expense not found. May be it is already deleted')
		return redirect("/expense")

def delete_expense(request, pk):
	try:
		expense_object = Expense.objects.get(id=pk)
		expense_form = ExpenseForm(instance = expense_object)
		
		if request.method == "POST":
			expense_form = ExpenseForm(request.POST)
			if expense_form.is_valid():
				expense_object.delete()
				saved_data = expense_form.cleaned_data['expense_type']
				messages.success(request, '"{}" deleted successfully'.format(saved_data))
			return redirect("/expense")
		context = {'form':expense_form, 'action':'delete'}
		return render(request, 'expense/list_expense.html', context)
	except Exception as error:
		messages.error(request, 'Expense Type not found. May be it is already deleted')
		return redirect("/expense")
