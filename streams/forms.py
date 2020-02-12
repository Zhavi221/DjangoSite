from django import forms

STREAMS_CHOICES= [
    ('hermon', 'Hermon'),
    ('bansko', 'Bansko'),
    ]

class DropDown(forms.Form):
    chosen_stream = forms.CharField(label='What site would you like to see?', widget=forms.Select(choices=STREAMS_CHOICES))
