from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.

status = (("Draft","Draft"),("Schedule","Schedule"),("Active","Active"),("Inactive","Inactive"),("Delete","Delete"))


class Category(models.Model):
	"""docstring for Category"""
	category = models.ForeignKey("self", on_delete=models.PROTECT, related_name="category_name", blank=True,null=True)
	title = models.CharField(max_length=100)
	slug = AutoSlugField(populate_from=['title'], unique=True, editable=True)
	# content = RichTextUploadingField()
	content = models.TextField()
	keyword = models.CharField(max_length=160)
	meta_title = models.CharField(max_length=160)
	meta_description = models.TextField()
	thumbnail = models.ImageField(upload_to='blog/category/thumbnail', blank=True)	
	cover = models.ImageField(upload_to='blog/category/cover', blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, editable=False)
	utimestamp = models.DateTimeField(auto_now=True, editable=False)
	track = models.TextField(blank=True)
	utrack = models.TextField(blank=True)
	status = models.CharField(max_length=20, choices=status, default='Active')

	def __str__(self):
		return (self.title)

	def get_absolute_url(self):
		return reverse('blog:category', args=[str(self.slug)])

	class Meta:
		verbose_name_plural = 'Categories'
