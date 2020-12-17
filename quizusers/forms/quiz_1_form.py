from django import forms

#Django forms can be used to validate the response in the server side for two way protection(Front end and back end)

class PythonQuizForm(forms.Form):
    question_1 = forms.CharField('Question 1', )
    question_answer = forms.IntegerField('Question Correct Answer')
