from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdminCreationForm(forms.ModelForm):
    """
    یک فرم کامل برای ساخت کاربر که شامل تمام فیلدهای اجباری میباشد
    """
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # بررسی یکسان بودن دو رمز ورود
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        # ذخیره رمز ورود به صورت هش شده
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """
    فرمی برای به روزرسانی کاربران. شامل همه فیلدهای مربوط به کاربر می باشد
    اما قسمت رمز عبور مدیر را با رمز هش شده نمایش می دهد
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'staff', 'superuser')

    def clean_password(self):
        # صرف نظر از آنچه کاربر ارائه می دهد ، مقدار اولیه را بازگردانید.
        # این کار به جای فیلد در اینجا انجام می شود ، زیرا فیلد به مقدار اولیه دسترسی ندارد
        return self.initial["password"]


