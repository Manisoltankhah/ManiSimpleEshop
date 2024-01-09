from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from product_module.models import Product, ProductCategory
from site_module.models import SiteSetting, FooterLinkBox, Slider
from utils.convertors import group_list


class HomeView(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider = Slider.objects.filter(is_active=True)
        context['slider'] = slider
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        most_viewed_products = Product.objects.filter(is_active=True, is_delete=False).annotate(visit_count=Count('productvisit')).order_by('-visit_count')[:12]
        context['latest_products'] = group_list(latest_products, 3)
        context['most_viewed_products'] = group_list(most_viewed_products, 3)

        categories = list(ProductCategory.objects.annotate(products_count=Count('products_categories')).filter(is_active=True, is_delete=False, products_count__gt=0)[:4])
        categories_products = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.products_categories.all()[:4])
            }
            categories_products.append(item)

        context['categories_products'] = categories_products
        return context


def contact_page(request):
    return render(request, 'home_module/contact_page.html')


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    return render(request, 'shared/site_header_component.html', {
        'site_setting': setting
    })


def site_footer_component(request):
    setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    return render(request, 'shared/site_footer_component.html', {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    })


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context

