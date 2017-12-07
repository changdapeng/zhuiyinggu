"""
data_manage/models.py

Data: 资料管理 模型
"""
from django.db import models

DATA_STEP = (
('setp1','待下载'),
('setp2', '已下载'),
('step3', '审核成功'),
)

DATA_TYPE = (
('type1','电影'),
('type2','电视剧'),
('type3','游戏'),
('type4','音乐'),
('type5','IT技术视频'),
('type6','IT技术文档'),
('type7','IT行业视频'),
('type8','书籍'),
)

# 资料管理 模型
# ----------------

class Data(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=200)
    step = models.CharField(choices=DATA_STEP, blank=True, max_length=50)
    data_type = models.CharField(choices= DATA_TYPE, blank=True, max_length=50)
    size = models.FloatField(blank=True, null=True)
    creator = models.CharField(max_length=200)
    create_date = models.DateField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=200)
    address_type = models.CharField(choices=(('BD','百度云'), ('BT', 'BT种子')), blank=True, max_length=50)
    path = models.CharField(blank=True, max_length=200)
    
        
    def __str__(self):
        
        return self.name



