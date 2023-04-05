from django import forms
from .models import signup_model,members_model,chairmans_model,events_model,notices_view_model,notices_model,transactions_model,user_model,visitors_model,watchmans_model

class chairmans_form (forms.ModelForm):

    class Meta :

        model = chairmans_model
        fields = '__all__'

class events_form (forms.ModelForm):

    class Meta :

        model = events_model
        fields = '__all__'

class editevent_form (forms.ModelForm):

    class Meta :

        model = events_model
        fields = ['event_name','event_time','event_img','event_information','comments']

class notices_form (forms.ModelForm):

    class Meta :

        model = notices_model
        fields = '__all__'

class notices_view_form (forms.ModelForm):

    class Meta :

        model = notices_model
        fields = ['notice_title','notice_img','notice','comments']

class transactions_form (forms.ModelForm):

    class Meta :

        model = transactions_model
        fields = '__all__'

class user_form (forms.ModelForm):

    class Meta :

        model = user_model
        fields = '__all__'

class watchmans_form (forms.ModelForm):

    class Meta :

        model = watchmans_model
        fields = '__all__'

class editwatchmans_form (forms.ModelForm):

    class Meta :

        model = watchmans_model
        fields = ['firstname','lastname','username','password','address','city','state','Mobile']

class visitors_form (forms.ModelForm):

    class Meta :

        model = visitors_model
        fields = '__all__'

class visitors_list_form (forms.ModelForm):

    class Meta :

        model = visitors_model
        fields = ['name','vehicle_no','total_visitor','visit_house_no','out_time']

class signup_form (forms.ModelForm):

    class Meta :

        model = signup_model
        fields = '__all__'

class signup_update_form (forms.ModelForm):

    class Meta :

        model = signup_model
        fields = ['username','password']


class members_form (forms.ModelForm):

    class Meta :

        model = members_model
        fields = '__all__'

class editmembers_form (forms.ModelForm):

    class Meta :

        model = members_model
        fields = ['firstname','lastname','username','password','city','state','Mobile','bhk']