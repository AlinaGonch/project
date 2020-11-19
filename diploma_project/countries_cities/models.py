from django.db import models


class Country(models.Model):


    def load_photo(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["{}_flag", file_type])
        return file_name.format(
            self.name,
        )


    name = models.CharField(max_length=150, verbose_name='Название Страны')
    description = models.TextField(verbose_name='Описание Страны')
    slug = models.SlugField(max_length=150, verbose_name='Ссылка')
    icon = models.ImageField(upload_to=load_photo, verbose_name="Флаг Страны")


    class Meta:
        db_table = "country"
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

class City(models.Model):
    
    
    def load_photo(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["{}/{}", file_type])
        return file_name.format(
            self.country,
            self.name,
        )



    name = models.CharField(max_length=150, verbose_name='Название Страны')
    foundation_date = models.IntegerField(verbose_name='Год основания')
    population = models.IntegerField(verbose_name='Население')
    description = models.TextField(verbose_name='Описание Города')
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='country', verbose_name='Название страны')
    image = models.ImageField(upload_to=load_photo, verbose_name="Фото Города")    
    slug = models.SlugField(max_length=150, verbose_name='Ссылка')


    def show_image(self):
        pass


    def get_links(self):
        pass


    def get_location(self):
        pass
    

    class Meta:
        db_table = "city"
        verbose_name = "Город"
        verbose_name_plural = "Города"

# Create your models here.
