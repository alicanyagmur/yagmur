from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı adını veya parolayı yanlış girdiniz') #

            return  super(LoginForm,self).clean()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(max_length=60)
    password2 = forms.CharField(max_length=60)
    email = forms.EmailField(max_length=60)
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parola eşleşmiyor')
        return password2

    #def clean_username(self):
    #   username = self.cleaned_data['username']
    #    if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
    #        raise forms.ValidationError('Kullanıcı adı kayıtlı') # django kontrol ediyormuş
    #    return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('Bu mail adresi kayıtlı')
        return email