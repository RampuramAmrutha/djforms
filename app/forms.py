from django import forms
g=[['male','male'],['female','female']]
c=[('python','python'),('sql','sql')]
class StudentForm(forms.Form):
    sname=forms.CharField()
    sid=forms.IntegerField()
    surl=forms.URLField()
    semail=forms.EmailField()
    spassword=forms.CharField(widget=forms.PasswordInput)
    saddress=forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':10}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect())
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple())

