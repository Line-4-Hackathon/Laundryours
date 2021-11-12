from django import forms # 장고에서 제공하는 forms 기능을 사용하기 위해
from .models import Post,User # Post 모델을 사용하기 위해 import

class PostForm(forms.ModelForm): # PostForm이라는 이름의 모델폼 클래스 생성
    class Meta:
        model = Post # form에서 사용할 모델이 Post임을 명시
        fields = ['title','content']

        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'required' : False,
                    'placeholder' : '제목을 입력해주세요.',
                }
            ),
            'content' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'textarea',
                }
            ),

        }