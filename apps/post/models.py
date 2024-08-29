from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Название категории',max_length=100)
    slug = models.SlugField('Слаг',max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField('Название тега', max_length=100)
    slug = models.SlugField('Слаг', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'



class Post(models.Model):
    title = models.CharField('Название поста', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    image = models.ImageField('Изображение', upload_to='posts')
    text = models.TextField('Текст поста')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_likes_count(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey('account.User', on_delete=models.CASCADE,
                               related_name='comments_author')
    text = models.TextField('Текст комментария')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'




posts1 = [# {'title':'Olimpic', 'Sport', 'https://example.com/image.jpg', 100, 'This is a sample post text.'})
# object2 = Post('Everest cool','Life','dfsdf',23,64)
# object3 = Post('Everest cool', 'Life', 'dfsdf', 23, 64)
# object4 = Post('Everest cool', 'Life', 'dfsdf', 23, 64)
# object5 = Post('Everest cool', 'Life', 'dfsdf', 23, 64)
]





