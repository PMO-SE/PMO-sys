from django.db import models
from rest_framework import reverse


class Project(models.Model):

    Name_category = (
        ('Caiqin LI', 'Caiqin LI'),
        ('Chenghai WANG', 'Chenghai WANG'),
        ('Fiona ZHANG', 'Fiona ZHANG'),
        ('Hui FENG', 'Hui FENG'),
        ('HuLin-Alex Cai', 'HuLin-Alex Cai'),
        ('Karen', 'Karen'),
        ('Kathyn Ye', 'Kathyn Ye'),
        ('KOU Lifang', 'KOU Lifang'),
        ('LI Ang', 'LI Ang'),
        ('LIU Hui', 'LIU Hui'),
        ('Luo Wei', 'Luo Wei'),
        ('MAO Haixing', 'MAO Haixing'),
        ('Mark Yu', 'Mark Yu'),
        ('Mike ZHOU', 'Mike ZHOU'),
        ('Pan Wen', 'Pan Wen'),
        ('Pending', 'Pending'),
        ('Qihui Zhou', 'Qihui Zhou'),
        ('Quanguo-Michael Li', 'Quanguo-Michael Li'),
        ('Sheng BI', 'Sheng BI'),
        ('Shengjie SHEN', 'Shengjie SHEN'),
        ('SUN Xiaodong', 'SUN Xiaodong'),
        ('Tony LU', 'Tony LU'),
        ('Weiwei-Eric Zhang', 'Weiwei-Eric Zhang'),
        ('Xi ming', 'Xi ming'),
        ('Xinye LUO', 'Xinye LUO'),
        ('Yiping-Patrick.Feng', 'Yiping-Patrick.Feng'),
        ('YuE-Peggy Zhu', 'YuE-Peggy Zhu'),
        ('ZHANG Chunxin', 'ZHANG Chunxin'),
        ('ZHANG Na', 'ZHANG Na'),
        ('Songyang XU', 'Songyang XU'),
        ('NA', 'NA')
    )

    Cluster_category = (
        ('MTS-MTO', 'MTS-MTO'),
        ('MTO-CTO', 'MTO-CTO'),
        ('MTS-CTO', 'MTS-CTO'),
        ('ETO-MV', 'ETO-MV'),
        ('NA', 'NA')
    )

    Plant_category = (
        ('AVX-E', 'AVX-E'),
        ('AVXP', 'AVXP'),
        ('SBG', 'SBG'),
        ('SBMLV', 'SBMLV'),
        ('SCD', 'SCD'),
        ('SEEE', 'SEEC'),
        ('SELV', 'SELV'),
        ('SEMC', 'SEMC'),
        ('SEMW', 'SEMW'),
        ('SITX', 'SITX'),
        ('SSAM', 'SSAM'),
        ('SSAP', 'SSAP'),
        ('SSIC', 'SSIC'),
        ('SSLVTA', 'SSLVTA'),
        ('SWD', 'SWD'),
        ('SWEEC', 'SWEEC'),
        ('WPF', 'WPF'),
        ('NA', 'NA')
    )

    BU_category = (
        ('Digital Energy', 'Digital Energy'),
        ('Home & Distribution', 'Home & Distribution'),
        ('Industrial & Automation', 'Industrial & Automation'),
        ('PP', 'Power Products'),
        ('PS', 'Power System Primary'),
        ('Power System Secondary', 'Power System Secondary'),
        ('SP', 'Secure Power'),
        ('ALL', 'ALL'),
        ('NA', 'NA')
    )

    Lob_category = (
        ('DBPRD', 'DBPRD'),
        ('DPENP', 'DPENP'),
        ('DPSOL', 'DPSOL'),
        ('IDEUR', 'IDEUR'),
        ('IDHMI', 'IDHMI'),
        ('IDMST', 'IDMST'),
        ('IDSDS', 'IDSDS'),
        ('IDSIG', 'IDSIG'),
        ('IDVSD', 'IDVSD'),
        ('IDWDA', 'IDWDA'),
        ('INMCP', 'INMCP'),
        ('INMVE', 'INMVE'),
        ('INMVP', 'INMVP'),
        ('PTACB', 'PTACB'),
        ('PTCCB', 'PTCCB'),
        ('PTCTR', 'PTCTR'),
        ('PTEQP', 'PTEQP'),
        ('PTFDA', 'PTFDA'),
        ('PTFDB', 'PTFDB'),
        ('PTLTVB', 'PTLTVB'),
        ('PTSOL', 'PTSOL'),
        ('PTWDA', 'PTWDA'),
        ('SP3PH', 'SP3PH'),
        ('SPMDC', 'SPMDC'),
        ('HDFDB', 'HDFDB'),
        ('ALL', 'ALL'),
        ('NA', 'NA')
    )

    Type_category = (
        ('BCP', 'BCP'),
        ('Capacity', 'Capacity'),
        ('LTIP', 'LTIP'),
        ('Others', 'Others'),
        ('PEP', 'PEP'),
        ('PMP', 'PMP'),
        ('PWP', 'PWP'),
        ('Rebalancing', 'Rebalancing'),
        ('Transfer', 'Transfer'),
        ('NA', 'NA')
    )

    Code_category = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16')
    )

    Status_category = (
        ('Open', 'Open'),
        ('Do', 'Do'),
        ('IMP', 'IMP'),
        ('Produce', 'Produce'),
        ('Sell', 'Sell'),
        ('Closed', 'Closed')
    )

    Region_category = (
        ('North', 'North'),
        ('South', 'South'),
        ('East&West', 'East&West'),
        ('WuXi', 'WuXi'),
    )

    Complexity_category = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    # Basics
    id = models.IntegerField(primary_key=True, auto_created=True)
    Region = models.CharField(max_length=30, choices=Region_category, null=False, default='No region')
    Project_name = models.CharField(max_length=100)
    Project_leader = models.CharField(max_length=30, choices=Name_category, blank=True, null=True)
    Project_type = models.CharField(max_length=30, choices=Type_category, blank=True, null=True)
    Project_code = models.CharField(max_length=30, choices=Code_category, blank=True, null=True)
    Complexity = models.IntegerField(max_length=30, choices=Complexity_category, blank=True, null=True)
    Comment = models.TextField(blank=True, null=True)

    # 不应该出现的
    Current_status = models.CharField(max_length=30, choices=Status_category, blank=True, null=True)

    # Category
    Cluster = models.CharField(max_length=40, choices=Cluster_category, blank=True, null=True)
    BU = models.CharField(max_length=30, choices=BU_category, blank=True, null=True)
    Lob = models.CharField(max_length=30, choices=Lob_category, blank=True, null=True)
    Plant = models.CharField(max_length=30, choices=Plant_category, blank=True, null=True)

    # KPI
    Additional_COGS = models.FloatField(max_length=10, blank=True, null=True)
    Productivity = models.FloatField(max_length=10, blank=True, null=True)
    CAPEX = models.FloatField(max_length=10, blank=True, null=True)
    Space_needed = models.FloatField(max_length=10, blank=True, null=True)
    Y_3_QTY = models.FloatField(max_length=10, blank=True, null=True)
    Expense = models.FloatField(max_length=10, blank=True, null=True)
    Payback = models.FloatField(max_length=10, blank=True, null=True)

    # Schedule
    Open_date = models.DateField(blank=True, null=True)
    Do_date = models.DateField(blank=True, null=True)
    IMP_date = models.DateField(blank=True, null=True)
    Produce_date = models.DateField(blank=True, null=True)
    Sell_date = models.DateField(blank=True, null=True)
    Close_date = models.DateField(blank=True, null=True)

    # 创建信息
    Time_created = models.DateTimeField(auto_now_add=True)


class Workload(models.Model):
    Quarter_category = (
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
    )
    Ratio_category = (
        ('0.0', '0.0'),
        ('0.1', '0.1'),
        ('0.2', '0.2'),
        ('0.3', '0.3'),
        ('0.4', '0.4'),
        ('0.5', '0.5'),
        ('0.6', '0.6'),
        ('0.7', '0.7'),
        ('0.8', '0.8'),
        ('0.9', '0.9'),
        ('1.0', '1.0')
    )

    id = models.IntegerField(primary_key=True, auto_created=True)
    Project_ID = models.ForeignKey("Project", on_delete=models.CASCADE)
    Year = models.CharField(max_length=5, null=False)
    Quarter = models.CharField(max_length=10, choices=Quarter_category, null=False)
    Leader = models.CharField(max_length=30, choices=Project.Name_category, blank=True, null=True)
    Workload = models.FloatField(null=True, choices=Ratio_category)


class CardInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    Project_ID = models.ForeignKey("Project", on_delete=models.CASCADE)
    Update = models.DateField(blank=True, null=True)
    Summary = models.CharField(max_length=100, blank=True, null=True)
    Picture = models.BinaryField(blank=True, null=True)

    # KPI
    Additional_COGS = models.FloatField(max_length=10, blank=True, null=True)
    Productivity = models.FloatField(max_length=10, blank=True, null=True)
    CAPEX = models.FloatField(max_length=10, blank=True, null=True)
    Space_needed = models.FloatField(max_length=10, blank=True, null=True)
    Y_3_QTY = models.FloatField(max_length=10, blank=True, null=True)
    Expense = models.FloatField(max_length=10, blank=True, null=True)
    Payback = models.FloatField(max_length=10, blank=True, null=True)

    # Schedule
    Open_date = models.DateField(blank=True, null=True)
    Do_date = models.DateField(blank=True, null=True)
    IMP_date = models.DateField(blank=True, null=True)
    Produce_date = models.DateField(blank=True, null=True)
    Sell_date = models.DateField(blank=True, null=True)
    Close_date = models.DateField(blank=True, null=True)

    # Risk & Action
    Risk1 = models.CharField(max_length=100, blank=True, null=True)
    Risk2 = models.CharField(max_length=100, blank=True, null=True)
    Risk3 = models.CharField(max_length=100, blank=True, null=True)
    Risk4 = models.CharField(max_length=100, blank=True, null=True)
    Action1 = models.CharField(max_length=100, blank=True, null=True)
    Action2 = models.CharField(max_length=100, blank=True, null=True)
    Action3 = models.CharField(max_length=100, blank=True, null=True)
    Action4 = models.CharField(max_length=100, blank=True, null=True)

