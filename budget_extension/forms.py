from django import forms
from .models import Extension, Research_fellow, Material, Other
from bootstrap_datepicker_plus import DatePickerInput

class ExtensionForm(forms.ModelForm):
    class Meta:
        model = Extension
        fields = ['Research_fellows', 'Extension_weeks', 'Project_completion', 'Reason_of_extension', 'Detail_remaining_work', 'Progress_report']
        widgets = {
            'Project_completion' :DatePickerInput()
        }
        labels = {'Research_fellows':'Research Fellows(All fellows presently working and who had worked on the project)',
                  'Extension_weeks':'Period of extension requested (in weeks)',
                  'Project_completion':'Projected Date of completion',
                  'Reason_of_extension':'Reasons/justification for extension of the study - (in details)',
                  'Detail_remaining_work':'Provide timed schedule to complete the remaining work',
                  'Progress_report':'Submit progress report of Research activity'}

class ResearchFellowForm(forms.ModelForm):
    class Meta:
        model = Research_fellow
        fields = ['Bud_utilize', 'Additional_bud', 'Justify']
        labels ={'Bud_utilize':'Budget Utilized',
                 'Additional_bud':'Additional Budget requested',
                 'Justify':'Justification for Additional Budget requested'
                 }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['Bud_utilize', 'Additional_bud', 'Justify']
        labels = {'Bud_utilize': 'Budget Utilized',
                  'Additional_bud': 'Additional Budget requested',
                  'Justify': 'Justification for Additional Budget requested'
                  }

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ['Bud_utilize', 'Additional_bud', 'Justify']
        labels = {'Bud_utilize': 'Budget Utilized',
                  'Additional_bud': 'Additional Budget requested',
                  'Justify': 'Justification for Additional Budget requested'
                  }