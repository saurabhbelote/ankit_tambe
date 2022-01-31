from rest_framework import serializers
from user.models import NewUser

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['first_name','last_name','user_name','email','mobile_no','password']