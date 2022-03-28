from django.shortcuts import render

from .models import Post, Tag



class ObjectListMixin:
    object_model = None
    title = None
    template = 'pikadu_app/object_list.html'

    def object_list(self, request):
        objects = self.object_model.objects.all()
        return render(request, self.template,
                  context={'objects': objects,
                           'title' : self.title})
