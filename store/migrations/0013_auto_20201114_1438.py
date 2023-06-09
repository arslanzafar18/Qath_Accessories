# Generated by Django 3.1 on 2020-11-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20201114_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Accessories', 'Accessories'), ('Courtwear', 'Courtwear'), ('Ceremonial', 'Ceremonial')], default='Accessories', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='other_image',
            field=models.ManyToManyField(blank=True, to='store.OtherImages'),
        ),
    ]
