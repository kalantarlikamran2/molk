# Generated by Django 2.2 on 2019-05-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20190516_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='telebe',
            name='il',
            field=models.CharField(choices=[('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006')], default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telebe',
            name='yasayis',
            field=models.CharField(default=1, max_length=80, verbose_name='yasayis yeri'),
            preserve_default=False,
        ),
    ]
