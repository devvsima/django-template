from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название")

    class Meta:
        db_table = "tag"
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self) -> str:
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название")
    description = models.CharField(max_length=3000, unique=True, verbose_name="Описание")
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name="Категория")
    preview_photo = models.ImageField(upload_to="project_preview/", null=True, verbose_name="Превью")
    tags = models.ManyToManyField(to=Tags, verbose_name="Теги")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    project_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на проект")
    github_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на GitHub")

    class Meta:
        db_table = "projects"
        verbose_name = "проект"
        verbose_name_plural = "прокты"

    def __str__(self) -> str:
        return self.name
    
class ProjectImage(models.Model):
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE, related_name="images", verbose_name="Проект")
    preview = models.BooleanField(verbose_name="Поставить как превью портфолио?")
    image = models.ImageField(upload_to="project_images/", verbose_name="Фото")
    description = models.CharField(max_length=300, blank=True, verbose_name="Описание фото")