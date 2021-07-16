from django import forms

class ApplyForm(forms.Form):
    full_name = forms.CharField(max_length=30,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your Full Name',
                        'class':'form-control',
                        }
                    )
                )

    parent_name = forms.CharField(max_length=30,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your Father/Husband name',
                        'class':'form-control',
                        }
                    )
                )

    dob = forms.DateField(
                    widget=forms.DateInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your BirthDate',
                        'class':'form-control',
                        'type':'date',
                        }
                    )
                )

    gender = forms.CharField(max_length=12,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'gender',
                        'class':'form-control',
                        }
                    )
                )

    category = forms.CharField(max_length=15,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'category',
                        'class':'form-control',
                        }
                    )
                )

    mob_no = forms.IntegerField(
                    widget=forms.NumberInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your Mobile Number',
                        'class':'form-control',
                        }
                    )
                )

    email = forms.EmailField(
                    widget=forms.EmailInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your EmailID',
                        'class':'form-control',
                        }
                    )
                )

    nationality = forms.CharField(max_length=20,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your Nationality',
                        'class':'form-control',
                        }
                    )
                )
