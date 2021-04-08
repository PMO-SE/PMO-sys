# Generated by Django 3.1.4 on 2021-02-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Region', models.CharField(choices=[('North', 'North'), ('South', 'South'), ('East&West', 'East&West'), ('WuXi', 'WuXi')], default='No region', max_length=30)),
                ('Project_name', models.TextField(max_length=100)),
                ('Project_leader', models.CharField(blank=True, choices=[('Caiqin LI', 'Caiqin LI'), ('Chenghai WANG', 'Chenghai WANG'), ('Fiona ZHANG', 'Fiona ZHANG'), ('Hui FENG', 'Hui FENG'), ('HuLin-Alex Cai', 'HuLin-Alex Cai'), ('Karen', 'Karen'), ('Kathyn Ye', 'Kathyn Ye'), ('KOU Lifang', 'KOU Lifang'), ('LI Ang', 'LI Ang'), ('LIU Hui', 'LIU Hui'), ('Luo Wei', 'Luo Wei'), ('MAO Haixing', 'MAO Haixing'), ('Mark Yu', 'Mark Yu'), ('Mike ZHOU', 'Mike ZHOU'), ('Pan Wen', 'Pan Wen'), ('Pending', 'Pending'), ('Qihui Zhou', 'Qihui Zhou'), ('Quanguo-Michael Li', 'Quanguo-Michael Li'), ('Sheng BI', 'Sheng BI'), ('Shengjie SHEN', 'Shengjie SHEN'), ('SUN Xiaodong', 'SUN Xiaodong'), ('Tony LU', 'Tony LU'), ('Weiwei-Eric Zhang', 'Weiwei-Eric Zhang'), ('Xi ming', 'Xi ming'), ('Xinye LUO', 'Xinye LUO'), ('Yiping-Patrick.Feng', 'Yiping-Patrick.Feng'), ('YuE-Peggy Zhu', 'YuE-Peggy Zhu'), ('ZHANG Chunxin', 'ZHANG Chunxin'), ('ZHANG Na', 'ZHANG Na'), ('NA', 'NA')], max_length=30, null=True)),
                ('Cluster', models.CharField(blank=True, choices=[('MTS-MTO', 'MTS-MTO'), ('MTO-CTO', 'MTO-CTO'), ('MTS-CTO', 'MTS-CTO'), ('ETO-MV', 'ETO-MV'), ('NA', 'NA')], max_length=40, null=True)),
                ('Plant', models.CharField(blank=True, choices=[('AVX-E', 'AVX-E'), ('AVXP', 'AVXP'), ('SBG', 'SBG'), ('SBMLV', 'SBMLV'), ('SCD', 'SCD'), ('SEEE', 'SEEC'), ('SELV', 'SELV'), ('SEMC', 'SEMC'), ('SEMW', 'SEMW'), ('SITX', 'SITX'), ('SSAM', 'SSAM'), ('SSAP', 'SSAP'), ('SSIC', 'SSIC'), ('SSLVTA', 'SSLVTA'), ('SWD', 'SWD'), ('SWEEC', 'SWEEC'), ('WPF', 'WPF'), ('NA', 'NA')], max_length=30, null=True)),
                ('BU', models.CharField(blank=True, choices=[('Digital Energy', 'Digital Energy'), ('Home & Distribution', 'Home & Distribution'), ('Industrial & Automation', 'Industrial & Automation'), ('Power Products', 'Power Products'), ('Power System Primary', 'Power System Primary'), ('Power System Secondary', 'Power System Secondary'), ('Secure Power', 'Secure Power'), ('ALL', 'ALL'), ('NA', 'NA')], max_length=30, null=True)),
                ('Lob', models.CharField(blank=True, choices=[('DBPRD', 'DBPRD'), ('DPENP', 'DPENP'), ('DPSOL', 'DPSOL'), ('IDEUR', 'IDEUR'), ('IDHMI', 'IDHMI'), ('IDMST', 'IDMST'), ('IDSDS', 'IDSDS'), ('IDSIG', 'IDSIG'), ('IDVSD', 'IDVSD'), ('IDWDA', 'IDWDA'), ('INMCP', 'INMCP'), ('INMVE', 'INMVE'), ('INMVP', 'INMVP'), ('PTACB', 'PTACB'), ('PTCCB', 'PTCCB'), ('PTCTR', 'PTCTR'), ('PTEQP', 'PTEQP'), ('PTFDA', 'PTFDA'), ('PTFDB', 'PTFDB'), ('PTLTVB', 'PTLTVB'), ('PTSOL', 'PTSOL'), ('PTWDA', 'PTWDA'), ('SP3PH', 'SP3PH'), ('SPMDC', 'SPMDC'), ('ALL', 'ALL'), ('NA', 'NA')], max_length=30, null=True)),
                ('Project_type', models.CharField(blank=True, choices=[('BCP', 'BCP'), ('Capacity', 'Capacity'), ('LTIP', 'LTIP'), ('Others', 'Others'), ('PEP', 'PEP'), ('PMP', 'PMP'), ('PWP', 'PWP'), ('Rebalancing', 'Rebalancing'), ('Transfer', 'Transfer'), ('NA', 'NA')], max_length=30, null=True)),
                ('Project_code', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16')], max_length=30, null=True)),
                ('Additional_COGS', models.FloatField(blank=True, max_length=10, null=True)),
                ('Productivity', models.FloatField(blank=True, max_length=10, null=True)),
                ('CAPEX', models.FloatField(blank=True, max_length=10, null=True)),
                ('Current_status', models.CharField(blank=True, choices=[('Closed', 'Closed'), ('Feasibility Study', 'Feasibility Study'), ('Ongoing', 'Ongoing')], max_length=30, null=True)),
                ('Space_needed', models.FloatField(blank=True, max_length=10, null=True)),
                ('Produce_date', models.DateField(blank=True, null=True)),
                ('Time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workload',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Year', models.CharField(max_length=5)),
                ('Quarter', models.CharField(choices=[('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q4', 'Q4')], max_length=10)),
                ('Workload', models.FloatField(choices=[('0.0', '0.0'), ('0.1', '0.1'), ('0.2', '0.2'), ('0.3', '0.3'), ('0.4', '0.4'), ('0.5', '0.5'), ('0.6', '0.6'), ('0.7', '0.7'), ('0.8', '0.8'), ('0.9', '0.9'), ('1.0', '1.0')], null=True)),
            ],
        ),
    ]