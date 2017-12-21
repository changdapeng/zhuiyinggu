"""
data_manage/models.py

Data: 资料管理 模型
"""
from django.db import models



# 游戏模型
# --------
class Game(models.Model):
    GAME_TYPE = [
        ('game_type1','射击'),
        ('game_type2','第一人称射击'),
        ('game_type3','第三人称射击'),
        ('game_type4','动作'),
        ('game_type5','角色扮演'),
        ('game_type6','动作角色扮演'),
        ('game_type7','策略'),
        ('game_type8','竞速'),
        ('game_type9','模拟器'),
        ('game_type10','休闲'),
    ]
    GAME_STEP = [
        ('movie_step1','待下载'),
        ('movie_step2','已下载'),
        ('movie_step3','已审核'),
    ]
    SEED_ADDRESS = [
        ('seed_address1','百度云'),
        ('seed_address2','迅雷'),
    ]

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, help_text="请填写相关描述信息和备注")
    game_type = models.CharField(choices=GAME_TYPE, blank=True, max_length=20)
    game_step = models.CharField(choices=GAME_STEP, blank=True, max_length=20)
    seed_address = models.CharField(blank=True, max_length=200)
    seed_type = models.CharField(choices=SEED_ADDRESS, blank=True, max_length=50)
    creator = models.CharField(max_length=100)  # 该字段需为自动创建
    # 想要使下面两个字段可以修改，可以使用default=date.today代替auto_now_add=True和auto_now=True
    create_date = models.DateField(blank=True, null=True, auto_now_add=True)  # 该字段在实力第一次创建时自动创建，不可以修改
    update_date = models.DateField(blank=True, null=True, auto_now=True)  # 该字段在调用Model.save()时自动创建和更新，不可以修改
    
        
    def __str__(self):
        
        return self.name



# 影视资料模型
# ------------
class Movie(models.Model):
    MOVIE_TYPE = [
        ['电影', [
            ('movie_type1','大陆'),
            ('movie_type2','香港'),
            ('movie_type3','美国'),
            ('movie_type4','欧洲'),
            ('movie_type5','日韩'),
            ('movie_type6','东南亚'),
            ('movie_type7','其他'),
            ],
        ],
        ['电视剧',[
            ('movie_type8','大陆'),
            ('movie_type9','香港'),
            ('movie_type10','美国'),
            ('movie_type11','欧洲'),
            ('movie_type12','日韩'),
            ('movie_type13','其他'),
            ],
        ]
    ]
    MOVIE_STEP = [
        ('movie_step1','待下载'),
        ('movie_step2','已下载'),
        ('movie_step3','已审核'),
    ]
    SEED_ADDRESS = [
        ('seed_address1','百度云'),
        ('seed_address2','迅雷'),
    ]

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(blank=True, max_length=200, help_text="请填写相关描述信息")
    movie_type = models.CharField(choices= MOVIE_TYPE, blank=True, max_length=20)
    movie_step = models.CharField(choices=MOVIE_STEP, blank=True, max_length=20)
    seed_address = models.CharField(blank=True, max_length=200)
    seed_type = models.CharField(choices=SEED_ADDRESS, blank=True, max_length=50)
    creator = models.CharField(max_length=100)  # 该字段需为自动创建
    # 想要使下面两个字段可以修改，可以使用default=date.today代替auto_now_add=True和auto_now=True
    create_date = models.DateField(blank=True, null=True, auto_now_add=True)  # 该字段在实力第一次创建时自动创建，不可以修改
    update_date = models.DateField(blank=True, null=True, auto_now=True)  # 该字段在调用Model.save()时自动创建和更新，不可以修改
    
        
    def __str__(self):
        
        return self.name



# 音乐模型
# --------
class Music(models.Model):
    # choice 参数使用列表格式，为了可以动态的构建；
    # 列表元素使用元祖，防止后期修改列表内容时，导致已存数据的类型发生混淆；
    MUSIC_FORMAT = [
        ('music_format1','FLAC'),
        ('music_format2','APE'),
        ('music_format3','mp3'),
        ('music_format4','WAV'),
        ('music_format5','其他'),
    ]
    MUSIC_TYPE = [
        ('music_type1','轻音乐'),
        ('music_type2','流行歌曲'),
        ('music_type3','其他'),
    ]
    MUSIC_STEP = [
        ('book_step1','待下载'),
        ('book_step2','已下载'),
        ('book_step3','已审核'),
    ]

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(blank=True, max_length=200, help_text="请填写相关描述信息")
    singer = models.CharField(blank=True, max_length=50)
    album = models.CharField(blank=True, max_length=100)
    music_format = models.CharField(choices= MUSIC_FORMAT, blank=True, max_length=20)
    music_type = models.CharField(choices= MUSIC_TYPE, blank=True, max_length=20)
    music_step = models.CharField(choices=MUSIC_STEP, blank=True, max_length=20)
    # 经过认证的用户，方可进行上传文件
    music_file = models.FileField(upload_to='date_manage/music/')  # 文件上传到MEDIA_ROOT/date_manage/music/路径下
    creator = models.CharField(max_length=100)  # 该字段需为自动创建
    # 想要使下面两个字段可以修改，可以使用default=date.today代替auto_now_add=True和auto_now=True
    create_date = models.DateField(blank=True, null=True, auto_now_add=True)  # 该字段在实力第一次创建时自动创建，不可以修改
    update_date = models.DateField(blank=True, null=True, auto_now=True)  # 该字段在调用Model.save()时自动创建和更新，不可以修改
    
        
    def __str__(self):
        
        return self.name



# 书籍、文档模型
# --------------
class Book(models.Model):
    # choice 参数使用列表格式，为了可以动态的构建；
    # 列表元素使用元祖，防止后期修改列表内容时，导致已存数据的类型发生混淆；
    BOOK_TYPE = [
        ['Hacker', [
            ('book_type1','Python'),
            ('book_type2','Linux'),
            ('book_type3','网络'),
            ('book_type4','运维'),
            ('book_type5','数据库'),
            ('book_type6','前端'),
            ('book_type7','测试'),
        ]],
        ('book_type7','历史'),
        ('book_type8','人物传记'),
        ('book_type9','技能、训练'),
        ('book_type10','思想哲学'),
        ('book_type11','IT行业'),
        ('book_type12','小说'),
        ('book_type13','其他'),
    ]
    BOOK_STEP = [
        ('book_step1','待下载'),
        ('book_step2','已下载'),
        ('book_step3','已审核'),
        ('book_step4','阅读中'),
        ('book_step5','已读完'),
    ]

    name = models.CharField(max_length=50, unique=True)  # 该字段不可以重复,并自动为该字段创建数据库索引（不需要单独设置db_index参数）
    description = models.CharField(blank=True, max_length=200, help_text="请填写相关描述信息")
    author = models.CharField(blank=True, max_length=50)
    book_type = models.CharField(choices=BOOK_TYPE, max_length=20)
    book_step = models.CharField(choices=BOOK_STEP, max_length=20)
    # 经过认证的用户，方可进行上传文件
    book_file = models.FileField(upload_to='date_manage/book/')  # 文件上传到MEDIA_ROOT/date_manage/book/路径下
    creator = models.CharField(max_length=100)  # 该字段需为自动创建
    # 想要使下面两个字段可以修改，可以使用default=date.today代替auto_now_add=True和auto_now=True
    create_date = models.DateField(blank=True, null=True, auto_now_add=True)  # 该字段在实力第一次创建时自动创建，不可以修改
    update_date = models.DateField(blank=True, null=True, auto_now=True)  # 该字段在调用Model.save()时自动创建和更新，不可以修改
    
        
    def __str__(self):
        
        return self.name




# 视频资料模型
# ------------
class Video(models.Model):
    VIDEO_TYPE = [
        ('video_type1','IT'),
        ('video_type2','社会'),
        ('video_type3','演讲'),
        ('video_type4','科教'),
        ('video_type5','纪录片'),
        ('video_type6','其他'),
    ]
    VIDEO_STEP = [
        ('video_step1','待下载'),
        ('video_step2','已下载'),
        ('video_step3','已审核'),
    ]
    SEED_ADDRESS = [
        ('seed_address1','百度云'),
        ('seed_address2','迅雷'),
    ]

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(blank=True, max_length=200, help_text="请填写相关描述信息")
    video_type = models.CharField(choices= VIDEO_TYPE, blank=True, max_length=20)
    video_step = models.CharField(choices=VIDEO_STEP, blank=True, max_length=20)
    seed_address = models.CharField(blank=True, max_length=200)
    seed_type = models.CharField(choices=SEED_ADDRESS, blank=True, max_length=50)
    creator = models.CharField(max_length=100)  # 该字段需为自动创建
    # 想要使下面两个字段可以修改，可以使用default=date.today代替auto_now_add=True和auto_now=True
    create_date = models.DateField(blank=True, null=True, auto_now_add=True)  # 该字段在实力第一次创建时自动创建，不可以修改
    update_date = models.DateField(blank=True, null=True, auto_now=True)  # 该字段在调用Model.save()时自动创建和更新，不可以修改
    
        
    def __str__(self):
        
        return self.name

