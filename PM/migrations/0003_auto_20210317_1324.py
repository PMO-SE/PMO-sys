# Generated by Django 3.1.4 on 2021-03-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0002_auto_20210227_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Comment',
            field=models.CharField(blank=True, choices=[('MTS-MTO', 'MTS-MTO'), ('MTOMTS', 'MTOMTS'), ('MTO-CTO', 'MTO-CTO'), ('MTS-CTO', 'MTS-CTO'), ('ETO-MV', 'ETO-MV'), ('NA', 'NA')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='Expense',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='Payback',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='Y_3_QTY',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
    ]