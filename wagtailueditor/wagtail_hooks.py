import json

from django.core.urlresolvers import reverse
from django.templatetags.static import static
from django.utils import translation
from django.utils.html import escape
from django.utils.html import format_html
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from wagtail.admin.templatetags.wagtailadmin_tags import hook_output
from wagtail.core import hooks


def to_js_primitive(string):
    return mark_safe(json.dumps(escape(string)))


@hooks.register('insert_editor_css')
def insert_editor_css():
    css_files = [
        'UEditor/themes/iframe.css',
        'UEditor/themes/default/css/ueditor.css',
    ]
    css_includes = format_html_join(
        '\n',
        '<link rel="stylesheet" href="{0}">',
        ((static(filename),) for filename in css_files),
    )
    return css_includes + hook_output('insert_Ueditor_css')



@hooks.register('insert_editor_js')
def insert_editor_js():
    js_files = [
        'UEditor/ueditor.config.js',
        'UEditor/ueditor.all.js',
        'UEditor/ueditor.parse.js',
        'UEditor/ueditor.init.js',
    ]

    js_includes = format_html_join(
        '\n',
        '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files)
    )
    return js_includes + hook_output('insert_Ueditor_js')


# @hooks.register('insert_tinymce_js')
# def images_richtexteditor_js():
#     return format_html(
#         """
#         <script>
#             registerMCEPlugin("wagtailimage", {}, {});
#             window.chooserUrls.imageChooserSelectFormat = {};
#         </script>
#         """,
#         to_js_primitive(static('wagtailtinymce/js/tinymce-plugins/wagtailimage.js')),
#         to_js_primitive(translation.to_locale(translation.get_language())),
#         to_js_primitive(reverse('wagtailimages:chooser_select_format', args=['00000000']))
#     )


# @hooks.register('insert_tinymce_js')
# def embeds_richtexteditor_js():
#     return format_html(
#         """
#         <script>
#             registerMCEPlugin("wagtailembeds", {}, {});
#         </script>
#         """,
#         to_js_primitive(static('wagtailtinymce/js/tinymce-plugins/wagtailembeds.js')),
#         to_js_primitive(translation.to_locale(translation.get_language())),
#     )


# @hooks.register('insert_tinymce_js')
# def links_richtexteditor_js():
#     return format_html(
#         """
#         <script>
#             registerMCEPlugin("wagtaillink", {}, {});
#         </script>
#         """,
#         to_js_primitive(static('wagtailtinymce/js/tinymce-plugins/wagtaillink.js')),
#         to_js_primitive(translation.to_locale(translation.get_language())),
#     )


# @hooks.register('insert_tinymce_js')
# def docs_richtexteditor_js():
#     return format_html(
#         """
#         <script>
#             registerMCEPlugin("wagtaildoclink", {}, {});
#         </script>
#         """,
#         to_js_primitive(static('wagtailtinymce/js/tinymce-plugins/wagtaildoclink.js')),
#         to_js_primitive(translation.to_locale(translation.get_language())),
# )