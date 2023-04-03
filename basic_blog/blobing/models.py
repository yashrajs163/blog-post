from django.db import models
import readtime



# Create your models here.

# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png", blank=True )
    # status = models.IntegerField(choices=STATUS, default=1)
    
    

    def __str__(self):
        return self.title


    def snippet(self):
        return self.body[:100] + '...'   
    
    def get_readtime(self):
        result = readtime.of_text(self.body)
        return result.text