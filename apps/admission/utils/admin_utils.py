from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


def get_admin_url(obj: admin.ModelAdmin, view_name: str) -> str:
    opts = obj._meta
    return reverse(
        f"admin:{opts.app_label}_{opts.model_name}_{view_name}", args=[obj.pk]
    )


def get_view_link(obj: admin.ModelAdmin, text: str ="View", css_class: str ="viewlink") -> str:
    return get_link(obj, "change", text, css_class)


def get_delete_link(obj: admin.ModelAdmin, text: str ="Delete", css_class: str ="deletelink") -> str:
    return get_link(obj, "delete", text, css_class)


def get_link(obj: admin.ModelAdmin, action: str , text: str , css_class: str ) -> str:
    url = get_admin_url(obj, action)
    return format_html("<a class='{}' href='{}'>{}</a>", css_class, url, text)


@admin.display(description="Operations")
def entry_operations(obj: admin.ModelAdmin) -> str:
    return format_html("<span>{}</span> | <span>{}</span>", get_view_link(obj), get_delete_link(obj))
