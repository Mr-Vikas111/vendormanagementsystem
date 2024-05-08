from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):
        
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        
        if fields is not None and exclude is not None:
            serializers.ValidationError("fields and serializers simultaneously not allowed")
        super().__init__(*args, **kwargs)
        
        if fields:
            for field in set(self.fields.keys()) - set(fields):
                self.fields.pop(field, None)
        if exclude:
            for field in set(exclude):
                self.fields.pop(field, None)
    class Meta:
        abstract =True
