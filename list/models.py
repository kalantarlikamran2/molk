from django.db import models
from django.urls import reverse


class Telebe(models.Model):
    SHIRT_SIZESD = (
        ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),
        ('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12'),
        ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'),
        ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'),
        ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'),('31', '31')
    )
    SHIRT_SIZESM = (
        ('yanvar', 'yanvar'),
        ('fevral','fevral'),
        ('mart','mart'),
        ('aprel','aprel'), ('may','may'), ('iyun','iyun'),
        ('iyul','iyul'), ('avgust','avgust'), ('sentyabr','sentyabr'), ('oktyabr','oktyabr'), ('noyabr','noyabr'),
                                                                     ('dekabr','dekabr')

    )
    SHIRT_SIZESY = (
        ('1995', '1995'),
        ('1996', '1996'),
        ('1997', '1997'),
        ('1998', '1998'),
        ('1999', '1999'),
        ('2000', '2000'),
        ('2001', '2001'),
        ('2002', '2002'),
        ('2003', '2003'),
        ('2004', '2004'),
        ('2005', '2005'),
        ('2006', '2006')

    )

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    adi = models.CharField(max_length=80,verbose_name="adi")
    soyad = models.CharField(max_length=80,verbose_name="soyad")
    ata = models.CharField(max_length=80,verbose_name="ata adi")
    doguldugu = models.CharField(max_length=80,verbose_name="doguldugu yer")
    gun = models.CharField(max_length=80, choices=SHIRT_SIZESD)
    ay = models.CharField(max_length=80, choices=SHIRT_SIZESM)
    il = models.CharField(max_length=80, choices=SHIRT_SIZESY)
    yasayis = models.CharField(max_length=80, verbose_name="yasayis yeri")
    fakulte = models.CharField(max_length=80, verbose_name="fakulte")
    ixtsas = models.CharField(max_length=80, verbose_name="ixtisas")
    grup = models.CharField(max_length=80,verbose_name="grup")
    melumat=models.TextField(blank=True , verbose_name="melumat")
    publish = models.DateTimeField(auto_now= True, verbose_name="Tarix")
    image = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id': self.id})


    class Meta:
        ordering= ['publish' , 'id']