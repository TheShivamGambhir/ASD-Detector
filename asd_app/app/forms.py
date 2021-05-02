from django import forms

NUMS= [
    ('q1', 0),
    ('q2', 0),
    ('q4', 1),
    ('q5', 1),
    ]
class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))