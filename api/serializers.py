from rest_framework import serializers
from .models import CustomTest, TrainingCenter, TrainingCenterCourse
from .models import CandidateRegistration, AppUser, JobRole
from .models import SectorSkillCouncil
from .models import CourseInfo, BatchInfo, StudentCourseRegistration
from .models import CourseFeedbackDetail

class CustomTestSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomTest
		fields = '__all__'

class TrainingCenterSerializer(serializers.ModelSerializer):

	class Meta:
		model = TrainingCenter
		fields = ('id','center_id','training_center_name','address','training_center_district', 'training_center_state','center_poc_name','center_poc_email','training_partner')		

class CandidateRegistrationSerializer(serializers.ModelSerializer):

	class Meta:
		model = CandidateRegistration
		fields = '__all__'

class AppUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = AppUser
		fields = '__all__'

class LoginCheckSerializer(serializers.ModelSerializer):

	class Meta:
		model = AppUser
		fields = ('user_email','user_password')

class JobRoleSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = JobRole
		fields = '__all__'
		depth = 1

class CourseInfoSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = CourseInfo
		fields = '__all__'
		depth = 1

class BatchInfoSerializer(serializers.ModelSerializer):

	class Meta:
		model = BatchInfo
		fields = '__all__'

class TrainingCenterCourseSerializer(serializers.ModelSerializer):

	class Meta:
		model = TrainingCenterCourse
		fields = '__all__'
		depth = 2

class StudentCourseRegistrationSerializer(serializers.ModelSerializer):

	class Meta:
		model = StudentCourseRegistration
		fields = '__all__'
		depth = 1

class CourseFeedbackDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = CourseFeedbackDetail
		fields = '__all__'
		depth = 1