# Generated by Django 4.0.4 on 2022-05-17 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_authors_alter_book_bookshelves_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='format',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formats', to='books.book'),
        ),
    ]
