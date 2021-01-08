from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class CheckAnswers(forms.Form):
    answer_1 = forms.CharField(required=False)
    answer_2 = forms.CharField(required=False)
    answer_3 = forms.CharField(required=False)
    answer_4 = forms.CharField(required=False)
    answer_5 = forms.CharField(required=False)
    answer_6 = forms.CharField(required=False)
    answer_7 = forms.CharField(required=False)
    answer_8 = forms.CharField(required=False)
    
    answer_9 = forms.CharField(required=False)
    answer_10 = forms.CharField(required=False)
    answer_11 = forms.CharField(required=False)
    answer_12 = forms.CharField(required=False)
    answer_13 = forms.CharField(required=False)
    answer_14 = forms.CharField(required=False)
    answer_15 = forms.CharField(required=False)
    answer_16 = forms.CharField(required=False)

    answer_17 = forms.CharField(required=False)
    answer_18 = forms.CharField(required=False)
    answer_19 = forms.CharField(required=False)
    answer_20 = forms.CharField(required=False)
    answer_21 = forms.CharField(required=False)
    answer_22 = forms.CharField(required=False)
    answer_23 = forms.CharField(required=False)
    answer_24 = forms.CharField(required=False)
    
    answer_25 = forms.CharField(required=False)
    answer_26 = forms.CharField(required=False)
    answer_27 = forms.CharField(required=False)
    answer_28 = forms.CharField(required=False)
    answer_29 = forms.CharField(required=False)
    answer_30 = forms.CharField(required=False)
    answer_31 = forms.CharField(required=False)
    answer_32 = forms.CharField(required=False)
    
    answer_33 = forms.CharField(required=False)
    answer_34 = forms.CharField(required=False)
    answer_35 = forms.CharField(required=False)
    answer_36 = forms.CharField(required=False)
    answer_37 = forms.CharField(required=False)
    answer_38 = forms.CharField(required=False)
    answer_39 = forms.CharField(required=False)
    answer_40 = forms.CharField(required=False)
    
    def clean_answer_1(self):
        data = self.cleaned_data['answer_1']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_2(self):
        data = self.cleaned_data['answer_2']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_3(self):
        data = self.cleaned_data['answer_3']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_4(self):
        data = self.cleaned_data['answer_4']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_5(self):
        data = self.cleaned_data['answer_5']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_6(self):
        data = self.cleaned_data['answer_6']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_7(self):
        data = self.cleaned_data['answer_7']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_8(self):
        data = self.cleaned_data['answer_8']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_9(self):
        data = self.cleaned_data['answer_9']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_10(self):
        data = self.cleaned_data['answer_10']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_11(self):
        data = self.cleaned_data['answer_11']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_12(self):
        data = self.cleaned_data['answer_12']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_13(self):
        data = self.cleaned_data['answer_13']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_14(self):
        data = self.cleaned_data['answer_14']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_15(self):
        data = self.cleaned_data['answer_15']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_16(self):
        data = self.cleaned_data['answer_16']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_17(self):
        data = self.cleaned_data['answer_17']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_18(self):
        data = self.cleaned_data['answer_18']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_19(self):
        data = self.cleaned_data['answer_19']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_20(self):
        data = self.cleaned_data['answer_20']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_21(self):
        data = self.cleaned_data['answer_21']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_22(self):
        data = self.cleaned_data['answer_22']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_23(self):
        data = self.cleaned_data['answer_23']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_24(self):
        data = self.cleaned_data['answer_24']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_25(self):
        data = self.cleaned_data['answer_25']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_26(self):
        data = self.cleaned_data['answer_26']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_27(self):
        data = self.cleaned_data['answer_27']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_28(self):
        data = self.cleaned_data['answer_28']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_29(self):
        data = self.cleaned_data['answer_29']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_30(self):
        data = self.cleaned_data['answer_30']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_31(self):
        data = self.cleaned_data['answer_31']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_32(self):
        data = self.cleaned_data['answer_32']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_33(self):
        data = self.cleaned_data['answer_33']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_34(self):
        data = self.cleaned_data['answer_34']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_35(self):
        data = self.cleaned_data['answer_35']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_36(self):
        data = self.cleaned_data['answer_36']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_37(self):
        data = self.cleaned_data['answer_37']
        
        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data

    def clean_answer_38(self):
        data = self.cleaned_data['answer_38']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_39(self):
        data = self.cleaned_data['answer_39']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
    
    def clean_answer_40(self):
        data = self.cleaned_data['answer_40']

        if len(data) > 4:
            raise ValidationError("Illegal behavior detected.".format(data))

        if len(data.split(' ')) > 2:
            raise ValidationError("Illegal behavior detected.".format(data))
        
        return data
