from django import template
import modal


register = template.Library()


def modal_version():
    return modal.__version__


register.simple_tag(modal_version)
