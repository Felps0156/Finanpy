from django import forms

from transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'category', 'amount', 'date', 'description')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            base = 'w-full rounded-xl border border-zinc-700 bg-zinc-900 px-4 py-3 text-slate-100 placeholder:text-slate-500 focus:border-indigo-500 focus:ring-0'
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = base
            else:
                field.widget.attrs.setdefault('class', base)
        self.fields['amount'].widget.attrs.setdefault('step', '0.01')
        self.fields['amount'].label = 'Valor'
        self.fields['account'].label = 'Conta'
        self.fields['category'].label = 'Categoria'
        self.fields['date'].label = 'Data'
        self.fields['description'].label = 'Descrição (opcional)'
        if user:
            self.fields['account'].queryset = user.accounts.all()
            self.fields['category'].queryset = user.categories.all()
