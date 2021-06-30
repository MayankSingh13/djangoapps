from django import forms

class BioForm(forms.Form):
    first_name = forms.CharField(max_length=25,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your first name',
                        'class':'form-control',
                        }
                    )
                )

    last_name = forms.CharField(max_length=25,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your last name',
                        'class':'form-control',
                        }
                    )
                )

    contact = forms.IntegerField(
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

    address = forms.CharField(max_length=100,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your Postal Address',
                        'class':'form-control',
                        }
                    )
                )

    city = forms.CharField(max_length=25,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your current city',
                        'class':'form-control',
                        }
                    )
                )

    state = forms.CharField(max_length=25,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your current state',
                        'class':'form-control',
                        }
                    )
                )

    pincode = forms.IntegerField(
                    widget=forms.NumberInput(
                    attrs={
                        'required':'required',
                        'placeholder':'pincode',
                        'class':'form-control',
                        }
                    )
                )

    gender = forms.CharField(max_length=25,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'gender',
                        'class':'form-control',
                        }
                    )
                )

    education = forms.CharField(max_length=25,
                    widget=forms.TextInput(
                    attrs={
                        'required':'required',
                        'placeholder':'Your highest degree',
                        'class':'form-control',
                        }
                    )
                )
