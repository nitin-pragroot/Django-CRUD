from django.urls import path
from .import views

urlpatterns = [
    path('',views.Insert,name="home"),
    path('insert/',views.InsertData,name="insert"),
    path('showpage/',views.Showpage,name="showpage"),
    path('editpage/<int:pk>',views.EditPage,name="editpage"),
    path('update/<int:pk>',views.UpdateData,name="update"),
    path('delete/<int:pk>',views.DeleteData,name="delete"),

]
