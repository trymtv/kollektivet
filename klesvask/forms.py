from django import forms

washTypes = [
    ('hvitvask', 'Hvitvask'),
    ('fargetvask', 'Fargetvask'),
    ('ullvask', 'Ullvask'),
    ('kokvask', 'Kokvask'),
    ('syntetisk', 'Syntetisk'),
]

class RegWash(forms.Form):
    washType = forms.CharField(label='Type vask', max_length=100, widget=forms.Select(choices=washTypes, attrs={'class': 'form-control'}))
    degrees = forms.IntegerField(label='Grader', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    washLength = forms.IntegerField(label='Lengde i minutter', min_value=0, max_value=120,widget=forms.NumberInput(attrs={'class': 'form-control'}))

class RegQueue(forms.Form):
    washType = forms.CharField(label='Type vask', max_length=100, widget=forms.Select(choices=washTypes, attrs={'class': 'form-control'}))