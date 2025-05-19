
from django.contrib.auth.models import User  # 1 
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    def create(self, validated_data):  # 2 
        user = User.objects.create_user(      # user 객체를 생성한다. ⬇️ ⬇️
            username = validated_data['username'], # 유효한 username 과
            password = validated_data['password'], # 유효한 password 로 
        )
        return user  # 생성된 user 객체 반환
    class Meta: # 3
        model = User
        fields = [ 'username', 'password' ] # 두 필드를 직렬화