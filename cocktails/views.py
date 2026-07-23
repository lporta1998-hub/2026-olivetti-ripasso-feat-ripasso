from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from cocktails.models import PuntoVendita

__all__ = [
    "PuntoVenditaCreateView",
    "PuntoVenditaDetailView",
    "PuntoVenditaListView",
    "PuntoVenditaUpdateView",
]


class PuntoVenditaDetailView(DetailView):
    model = PuntoVendita


class PuntoVenditaListView(ListView):
    model = PuntoVendita


class PuntoVenditaCreateView(CreateView):
    model = PuntoVendita
    fields = [
        "nome",
        "indirizzo",
        "telefono",
        "capienza",
        "è_un_bar",
    ]
    template_name = "cocktails/puntovendita_new.html"

    def get_success_url(self):
        return reverse("puntovendita_detail", kwargs={"pk": self.object.pk})


class PuntoVenditaUpdateView(UpdateView):
    model = PuntoVendita
    fields = [
        "nome",
        "indirizzo",
        "telefono",
        "capienza",
        "è_un_bar",
    ]
    template_name = "cocktails/puntovendita_edit.html"

    def get_success_url(self):
        return reverse("puntovendita_detail", kwargs={"pk": self.object.pk})
