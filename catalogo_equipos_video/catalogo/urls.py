from django.urls import path

from . import views

app_name = 'catalogo'

urlpatterns = [
    path("", views.index, name="index"),
    path("VHSs/", views.VHSs, name="VHSs"),
    path("Video_Equipments/<int:VideoEquipments_id>/", views.Video_Equipments, name="Video_Equipments"),
    path("add_DVD/", views.add_DVD, name="add_DVD"),
    path("edit_DVD/<int:DVD_id>", views.edit_DVD, name="edit_DVD"),
    path("delete_DVD/<int:DVD_id>", views.delete_DVD, name="delete_DVD"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]