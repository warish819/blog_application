from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

from blog_app.models import Blog, Contact

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # self.fields["username"].widget.attrs
        self.fields["username"].widget.attrs["Placeholder"] = " Your Username" 
        self.fields["email"].widget.attrs["Placeholder"] = " Your email"    
        self.fields["password1"].widget.attrs["Placeholder"] = " Your password"    
        self.fields["password2"].widget.attrs["Placeholder"] = " Your confirm password"       

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # self.fields["username"].widget.attrs
        self.fields["username"].widget.attrs["Placeholder"] = " Your Username" 
        self.fields["password"].widget.attrs["Placeholder"] = " Your password"    


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'  
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["Placeholder"] = " Your Name" 
        self.fields["email"].widget.attrs["Placeholder"] = " Your Email"   
        self.fields["description"].widget.attrs["Placeholder"] = " Your message" 

class BlogsForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['title','slug','text']
 
    def __init__(self, *args, **kwargs):
        super(BlogsForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["Placeholder"] = " Your Title" 
        self.fields["slug"].widget.attrs["Placeholder"] = " Your Slug"   
        self.fields["text"].widget.attrs["Placeholder"] = " Your message"                    
                 
                
        
