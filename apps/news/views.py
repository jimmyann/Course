from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from apps.helpers import ajax_required
from apps.news.models import News


class NewsListView(LoginRequiredMixin, ListView):
    """首页动态"""
    model = News
    paginate_by = 20
    context_object_name = None
    template_name = 'news/news_list.html'

    def get_queryset(self):
        return News.objects.filter(reply=False)

@login_required
@ajax_required
@require_http_methods(['POST'])
def post_news(request):
    """发送动态，AJAX POST 请求"""
    post = request.POST['post'].strip()
    if post:
        posted = News.objects.create(user=request.user, content=post)
        html = render_to_string('news/news_single.html', {'news': posted, 'request': request})
        return HttpResponse(html)
