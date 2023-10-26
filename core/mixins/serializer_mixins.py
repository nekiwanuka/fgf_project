from core.package_imports.rest_framework import serializers
#from core.package_imports.rest_framework_friendly_errors import mixins

class BaseSerializer(serializers.Serializer):
    pass

class ModelSerializer(serializers.ModelSerializer):
    pass

#mixins.FriendlyErrorMessagesMixin

# class ModelSerializer(mixins.FriendlyErrorMessagesMixin, serializers.ModelSerializer):
#     pass

