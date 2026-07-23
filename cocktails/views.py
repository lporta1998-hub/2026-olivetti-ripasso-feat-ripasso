from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from cocktails.models import PuntoVendita

__all__ = [
    "PuntoVenditaCreateView",
    "PuntoVenditaDetailView",
    "PuntoVenditaListView",
    "PuntoVenditaUpdateView",
    "PuntoVenditaDeleteView",
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

class PuntoVenditaDeleteView(DeleteView):
    model = PuntoVendita

    success_url = reverse_lazy("puntovendita_list")

