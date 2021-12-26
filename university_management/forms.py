from django import forms


class TimeInput(forms.TimeInput):
    input_type = 'time'
    
    def __init__(self, **kwargs):
        kwargs['format'] = "%H-%i"
        super().__init__(**kwargs)

class DateInput(forms.DateInput):
    input_type = 'date'
    
    def __init__(self, **kwargs):
        kwargs['format'] = "%d-%m-%y"
        super().__init__(**kwargs)