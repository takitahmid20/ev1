from rest_framework import serializers
# from rest_framework.serializers import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

SERVICES= [
    ('photography', 'Photography'),
    ('cinematography', 'Cinematography'),
    ('decoration', 'Decoration'),
    ('printing & press', 'Printing & Press'),
    ('gift items', 'Gift Items'),
    ('dj/musician', 'DJ/Musician'),
    ('mehedi artist', 'Mehedi Artist'),
    ('makeup artist', 'Makeup Artist'),
    ('brand promoter', 'Brand Promoter'),
    ('rental', 'Rental'),
    ('photography', 'Photography'),
    ]

# def name_validate(self, fname):
#         if fname['first_name'] == ' ':
#             raise serializers.ValidationError({"first_name": "You must add first name"})
#         # return fname

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):

    def fname(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise serializers.ValidationError("F name is required")
        return first_name


    first_name = serializers.CharField(required=True, 
    # validators=[fname]
    )
    last_name = serializers.CharField(required=False)
    
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    confirm_password = serializers.CharField(write_only=True, required=True)

    services= serializers.ChoiceField(label='Select a service', choices=SERVICES)

    # image = serializers.ImageField(max_length=None, allow_empty_file=False)

    class Meta:
        model = User
        fields = ('services','first_name','last_name', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match..."})
        if attrs['first_name'] == ' ':
            raise serializers.ValidationError(
                {"first_name": "You must add first name"})

        
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
        # validated_data['username'], 
        validated_data['email'], 
        validated_data['password']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user