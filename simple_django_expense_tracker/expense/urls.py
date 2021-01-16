from django.urls import path
from . import views


urlpatterns = [
	#path('transaction-chart/', views.transaction_pie_chart, name='transaction-chart'),
	path('',views.index, name='expense'),
	path('expense_type/',views.list_expense_type, name='list_expense_type'),
	path('expense_type/update_expense_type/<str:pk>',views.update_expense_type,\
	 name='update_expense_type'),
	path('expense_type/delete_expense_type/<str:pk>',views.delete_expense_type,\
	 name='delete_expense_type'),
	path('expense/',views.list_expense, name='list_expense'),
	path('expense_type/update_expense/<str:pk>',views.update_expense,\
	 name='update_expense'),
	path('expense_type/delete_expense/<str:pk>',views.delete_expense,\
	 name='delete_expense'),
]

