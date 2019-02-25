from django.shortcuts import render
from .forms import ExtensionForm, ResearchFellowForm, MaterialForm, OtherForm

def extension_view(request):
    ext_form = ExtensionForm
    res_fell_form = ResearchFellowForm
    mat_form = MaterialForm
    other_form = OtherForm
    if request.POST:
        ext_form = ExtensionForm(request.POST)
        res_fell_form = ResearchFellowForm(request.POST)
        mat_form = MaterialForm(request.POST)
        other_form = OtherForm(request.POST)

        if ext_form.is_valid() and res_fell_form.is_valid() and mat_form.is_valid() and other_form.is_valid():
            be1 = ext_form.save(commit=False)
            be2 = res_fell_form.save(commit=False)
            be3 = mat_form.save(commit=False)
            be4 = other_form.save(commit=False)

            be1.save()
            be2.save()
            be3.save()
            be4.save()
    context = {'form1': ext_form,
               'form2': res_fell_form,
               'form3': mat_form,
               'form4': other_form}
    return render(request, "budget_extension.html", context)
