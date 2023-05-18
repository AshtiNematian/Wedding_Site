from rest_framework import serializers

from partner.models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'title', 'description', 'category', 'phone_number']
