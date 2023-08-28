# Generated by Django 4.2.4 on 2023-08-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='sub_category',
            new_name='subcategory',
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
    ]
