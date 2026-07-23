from django.urls import path

from cocktails.views import (
    PuntoVenditaCreateView,
    PuntoVenditaDetailView,
    PuntoVenditaListView,
    PuntoVenditaUpdateView,
    PuntoVenditaDeleteView,
)

urlpatterns = [
    path("punto-vendita/", PuntoVenditaListView.as_view(), name="puntovendita_list"),
    path(
        "punto-vendita/<int:pk>/",
        PuntoVenditaDetailView.as_view(),
        name="puntovendita_detail",
    ),
    path(
        "punto-vendita/<int:pk>/edit/",
        PuntoVenditaUpdateView.as_view(),
        name="puntovendita_edit",
    ),
    path(
        "punto-vendita/new/",
        PuntoVenditaCreateView.as_view(),
        name="puntovendita_new",
    ),
    path(
            "punto-vendita/<int:pk>/delete/",
            PuntoVenditaDeleteView.as_view(),
            name="puntovendita_delete",
        ),
]
