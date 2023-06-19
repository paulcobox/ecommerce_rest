from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        """ Aca uso fields all solo para los metodos update e insert"""
        
    def to_representation(self, instance):
        """ To representation es para retornar los valores para el GET"""
        # data = super().to_representation(instance)
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'name': instance.name,
        }
    
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    def validate_name(self, value):
        """
        validate_name
        """
        if value is None and '' in value:
            raise serializers.ValidationError('Error, el nombre no puede estar vacio')
        print(value)
        return value
    def validate_email(self, value):
        """
        validate_email
        """
        if value == "":
            raise serializers.ValidationError('Error, el email no puede estar vacio')
        name = self.initial_data.get('name')
        if name in value:
            raise serializers.ValidationError('Error, el nombre de usuario no puede estar dentro del email')
        print(value)
        return value
    def validate(self, attrs):
        print(attrs)
        return attrs
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance