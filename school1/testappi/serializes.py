from rest_framework import serializers
from testing.models import Test

class QuizApiSerializer(serializers.ModelSerializer):

	class Meta:
		model = Test
		fields = '__all__'