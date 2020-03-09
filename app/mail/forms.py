from django import forms


class Mail(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email