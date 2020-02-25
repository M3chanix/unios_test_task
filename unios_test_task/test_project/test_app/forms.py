from django.forms import ModelForm, TextInput
from test_app.models import State

class StateForm(ModelForm):
    class Meta:
        model = State
        fields = ['Id', 'Title', 'Code']
        #widgets = {
            #'Id': TextInput(),
            #'Title': TextInput(attrs={'disabled': True}),
            #'Code': TextInput(attrs={'disabled': True})
            #}
        #def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop("request")
        #super(StateForm, self).__init__(*args, **kwargs)
        #self.fields['Id'].queryset = State.objects.all()
        #self.fields["Title"].queryset = State.objects.all()
        #self.fileds["Code"].queryset = State.objects.all()
