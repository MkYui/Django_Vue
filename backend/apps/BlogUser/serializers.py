from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):

    """
    User Model Serializer
    """

    class Meta:
        model = User
        fields = ('username', 'point',)


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User Register
    """

    username = serializers.CharField(required=True, label="用户名", validators=[
                                    UniqueValidator(queryset=User.objects.all(),
                                                    message="用户已经存在")])

    password = serializers.CharField(
        style={'input_type': 'password'}, label="密码", write_only=True,
    )

    def create(self, validated_data):
        user = super(UserRegisterSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validated_username(self, username):
        username_match = re.match(r'^(?!_)(?!.*?_$)[a-zA-Z0-9_\u4e00-\u9fa5]+$', username)
        if not username_match:
            raise serializers.ValidationError("用户名只含有汉字、数字、字母、下划线, 不能以下划线开头或结尾!")

    class Meta:
        model = User
        fields = ("username", "email", "password")
