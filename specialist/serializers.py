from rest_framework.serializers import  ModelSerializer
from .models import Profile, Experience, Skill, Education

class ExperienceSlz(ModelSerializer):
    class Meta:
        model=Experience
        fields = ('__all__')

class SkillSlz(ModelSerializer):
    class Meta:
        model=Skill
        fields = ('__all__')

class EducationSlz(ModelSerializer):
    class Meta:
        model=Education
        fields = ('__all__')

class ProfileSlz(ModelSerializer):
    experience = ExperienceSlz()
    education = EducationSlz()
    skill = SkillSlz()
    class Meta:
        model=Profile
        fields = ('__all__')


