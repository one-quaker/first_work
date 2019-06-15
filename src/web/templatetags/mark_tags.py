from django import template
import markdown


register = template.Library()


@register.filter
def mark2(text):
    # safe_mode governs how the function handles raw HTML
    if text:
        return markdown.markdown(text, safe_mode='escape', extensions=['markdown.extensions.nl2br', ])
