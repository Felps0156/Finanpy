from django import forms

from categories.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            classes = 'w-full rounded-xl border border-zinc-700 bg-zinc-900 px-4 py-3 text-slate-100 placeholder:text-slate-500 focus:border-indigo-500 focus:ring-0'
            field.widget.attrs.setdefault('class', classes)
        self.fields['name'].label = 'Nome da categoria'
        self.fields['type'].label = 'Tipo'
