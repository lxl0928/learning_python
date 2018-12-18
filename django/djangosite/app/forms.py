from django.forms import ModelForm
from app.models import Moment

class MomentForm(ModelForm):
    class Meta:
        """ 声明与本表单关联的模型类及其字段
        """
        model = Moment
        fields = '__all__' # fields=('content', 'user_name', 'kind')
