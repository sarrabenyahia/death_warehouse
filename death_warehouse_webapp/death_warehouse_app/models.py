from django.db import models
from django.core import exceptions
from dateutil.parser import parse as parse_date
from datetime import datetime

class CustomDateField(models.DateField):
    def to_python(self, value):
        if value is None:
            return value
        if isinstance(value, str):
            try:
                parsed = parse_date(value)
                if parsed is not None:
                    return parsed.date()
            except ValueError:
                pass

        raise exceptions.ValidationError(
            self.error_messages["invalid"],
            code="invalid",
            params={"value": value},
        )

    def get_prep_value(self, value):
        if value is None:
            return value
        if isinstance(value, datetime):
            return value.date()
        return value

    def formfield(self, **kwargs):
        defaults = {'input_formats': ['%Y/%m/%d']}
        defaults.update(kwargs)
        return super().formfield(**defaults)


class RecherchePatient(models.Model):
    nom = models.TextField(max_length=100)
    prenom = models.TextField(max_length=100)
    date_naiss = CustomDateField(validators=[])
    pays_naiss = models.CharField(max_length=100, blank=True)
    lieu_naiss = models.CharField(max_length=100, blank=True)
    code_naiss = models.CharField(max_length=10, blank=True)
    date_deces = CustomDateField(validators=[], blank=True)
