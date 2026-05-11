from import_export import resources
from lessons.models import Lessons

class LessonsResource(resources.ModelResource):
    class Meta:
        model = Lessons