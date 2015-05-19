from django import template
import modal


register = template.Library()


def fm_version():
    return modal.__version__


register.simple_tag(fm_version)