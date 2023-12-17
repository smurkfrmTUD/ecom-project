# Generated by Django 4.2.6 on 2023-11-28 20:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0001_initial'),
        ('transaction', '0002_rename_orderitem_transactionitem_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='transactionitem',
            old_name='product',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='transactionitem',
            old_name='order',
            new_name='transaction',
        ),
        migrations.AddField(
            model_name='transaction',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='transaction',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='vouchers.voucher'),
        ),
        migrations.AlterModelTable(
            name='transaction',
            table='Transaction',
        ),
    ]
