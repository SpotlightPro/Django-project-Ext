from django import forms
from .models import Member, Audit


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname', 'lname', 'email', 'qmo_level', 'passwd', 'passwd2']


# ChoiceField
class AuditsForm(forms.ModelForm):
    class Meta:
        model = Audit
        fields = ['audit_loc', 'loc_name', 'store_01', 'store_02', 'store_03', 'playground_01',
                  'playground_02', 'parents_rm_01', 'parents_rm_02', 'office_01', 'office_02',
                  'office_03', 'doctors_office_01', 'doctors_office_01']
