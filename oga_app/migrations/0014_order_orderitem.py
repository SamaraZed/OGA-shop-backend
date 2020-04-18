# Generated by Django 3.0.5 on 2020-04-18 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oga_app', '0013_profile_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_order', models.BooleanField(null=True)),
                ('items', models.ManyToManyField(to='oga_app.Item')),
                ('user_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_num', models.PositiveIntegerField(null=True)),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='oga_app.Item')),
                ('order_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_owner', to='oga_app.Order')),
            ],
        ),
    ]
