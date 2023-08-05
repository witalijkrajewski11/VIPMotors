import os

from django.template import Library
from django.template.loader import render_to_string
from django.templatetags.static import StaticNode

from main import models, constants

register = Library()


@register.filter
def hash(h, key):
    if not h or not key:
        return
    if isinstance(key, str) and hasattr(h, key):
        return getattr(h, key)
    if hasattr(h, 'get'):
        if result := h.get(key):
            return result
        if result := h.get(str(key)):
            return result


@register.filter
def getitem(h, key):
    return h[key]


@register.inclusion_tag("main/emails/components/emaillink.html", takes_context=True)
def emaillink(context, href, align="center", font_size=16):
    full_url = href if href.startswith('http') else "{}{}".format(context['frontend_url'], href)
    return dict(full_url=full_url,
                align=align,
                font_size=font_size)


@register.inclusion_tag("main/emails/components/endemaillink.html")
def endemaillink():
    return {}


@register.inclusion_tag("main/emails/components/bottom_link.html", takes_context=True)
def bottom_link(context, href, title=None, font_size=18):
    full_url = href if href.startswith('http') else "{}{}".format(context['frontend_url'], href)
    return dict(full_url=full_url,
                title=title or "View on VIPMotors",
                font_size=font_size)


@register.simple_tag(takes_context=True)
def email_link(context, href, title, align="center", font_size=16):
    full_url = href if href.startswith('http') else "{}{}".format(context['frontend_url'], href)
    return render_to_string("main/emails/components/email_link.html", context=dict(
        full_url=full_url,
        title=title,
        align=align,
        font_size=font_size,
    ))


@register.simple_tag()
def email_static(path):
    if os.getenv('FILE_STORAGE') == 's3':
        return StaticNode.handle_simple(path)
    else:
        return '{}{}'.format(os.getenv('BACKEND_URL'), StaticNode.handle_simple(path))


@register.simple_tag()
def group_tasks_by_legislative(tasks):
    lego_company_lookup = {}
    for task in tasks:
        if task.legislative_company_id not in lego_company_lookup:
            task.legislative_company.tasks_list = []
            lego_company_lookup[task.legislative_company_id] = task.legislative_company
        lego_company_lookup[task.legislative_company_id].tasks_list.append(task)

    return list(lego_company_lookup.values())


@register.simple_tag()
def group_tasks_by_report(tasks):
    report_company_lookup = dict()
    for task in tasks:
        if task.report_company_id not in report_company_lookup:
            task.report_company.report_source_tasks_list = []
            report_company_lookup[task.report_company_id] = task.report_company
        report_company_lookup[task.report_company_id].report_source_tasks_list.append(task)

    return list(report_company_lookup.values())