from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
 
class AdvancedEditor(forms.Textarea):
	class Media:
		js = (settings.MEDIA_URL + 'js/tiny_mce/tiny_mce.js',)
 
	def __init__(self, language=None, attrs=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		self.attrs = {'class': 'advancededitor'}
		if attrs: self.attrs.update(attrs)
		super(AdvancedEditor, self).__init__(attrs)
 
	def render(self, name, value, attrs=None):
		rendered = super(AdvancedEditor, self).render(name, value, attrs)
		return rendered + mark_safe(u'''
		<script type="text/javascript" src="%sjs/tiny_mce/tiny_mce.js"></script>
		<script type="text/javascript">
		tinyMCE.init({
			mode: "textareas",
			theme: "advanced",
			plugins: "advhr,table,emotions,media,insertdatetime,directionality",
			theme_advanced_toolbar_align: "left",
			theme_advanced_toolbar_location: "top",
			theme_advanced_buttons1:"bold,italic,underline,strikethrough,sub,sup,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,formatselect,fontselect,fontsizeselect",
			theme_advanced_buttons2:"bullist,numlist,outdent,indent,ltr,rtl,separator,link,unlink,anchor,image,separator,table,insertdate,inserttime,advhr,emotions,media,charmap,separator,undo,redo",
			theme_advanced_buttons3: "",
			content_css: "images/style.css",
			height: "350px",
			width: "653px"
		});
		</script>''' % settings.MEDIA_URL)
