from django.shortcuts import render

from bboard.models import Bb, Rubric

def index(request):
   bbs = Bb.objects.order_by('-published')
   return render(request, 'bboard/index.html', {'bbs': bbs})
   #
   #
   # template = loader.get_template('bboard/index.html')
   # bbs = Bb.objects.order_by('-published')
   # context = {'bbs': bbs}
   # return HttpResponse(template.render(context, request))

    # s = 'Список объявлений\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    #
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')

def by_rubric(request, rubric_id):
   bbs = Bb.objects.filter(rubric=rubric_id)
   rubrics = Rubric.objects.all
   current_rubric = Rubric.objects.get(pk=rubric_id)
   context = {
      "bbs": bbs,
      "rubrics": rubrics,
      "current_rubric": current_rubric
   }

