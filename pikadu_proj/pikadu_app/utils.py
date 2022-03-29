from django.shortcuts import render

from .models import Post, Tag, Comment


class ObjectListMixin:
    object_model = None
    title = None
    template = None

    def get(self, request):
        objects = self.object_model.objects.all()
        print(objects)
        return render(request, self.template,
                  context={'objects': objects,
                           'title' : self.title})

class CreateMixin:
    model = None
    form = None
    title = None
    form_template = None

    def get(self, request):
        render(request, self.template, context={'title':self.title,
                                                'form':self.form})
    def post(self, request):
        if self.form.is_valid():
            pass
