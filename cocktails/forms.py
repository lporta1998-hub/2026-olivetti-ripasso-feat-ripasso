from django.forms import ModelForm, CharField, TextInput
from cocktails.models import PuntoVendita

class PuntoVenditaPartialForm(ModelForm):
    indirizzo = CharField(widget=TextInput(), max_length=1024, required=True, label="Indirizzo")
    telefono = CharField(max_length=20, required=False)

    class Meta:
        model = PuntoVendita
        fields = [
            "indirizzo",
            "telefono",
        ]