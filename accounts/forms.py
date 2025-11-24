from django import forms

from accounts.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'balance')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            classes = 'w-full rounded-xl border border-zinc-700 bg-zinc-900 px-4 py-3 text-slate-100 placeholder:text-slate-500 focus:border-indigo-500 focus:ring-0'
            field.widget.attrs.setdefault('class', classes)
        self.fields['name'].label = 'Nome da conta'
        self.fields['balance'].label = 'Saldo atual'
        self.fields['balance'].widget.attrs.setdefault('step', '0.01')
