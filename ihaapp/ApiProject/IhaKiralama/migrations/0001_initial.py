# Generated by Django 4.2.4 on 2023-08-25 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IHA',
            fields=[
                ('iha_id', models.AutoField(primary_key=True, serialize=False)),
                ('marka', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('agirlik', models.DecimalField(decimal_places=2, max_digits=5)),
                ('kategori', models.CharField(choices=[('Küçük', 'Küçük'), ('Orta', 'Orta'), ('Büyük', 'Büyük')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kiralama',
            fields=[
                ('kiralama_id', models.AutoField(primary_key=True, serialize=False)),
                ('kiralama_tarihi', models.DateField()),
                ('kiralama_saati', models.TimeField()),
                ('iade_tarihi', models.DateField()),
                ('iha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IhaKiralama.iha')),
                ('kiralayan_uye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
