from django.contrib.syndication.views import Feed
from django.urls import reverse
from backend.models import BlogsPost

class BlogRssFeed(Feed):

    title = "yzd的博客"
    link = "/rss/"
    def items(self):
        return BlogsPost.objects.all()
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.content
    def item_link(self, item):
        return reverse('blog_id', args=[item.id,])