from tortoise.models import Model
from tortoise import fields

class Links(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)

    def __str__(self):
        return self.title


class Answers_On_Requests(Model):
    id = fields.IntField(pk=True)
    body = fields.CharField(max_length=1000)
    link = fields.ForeignKeyField('models.Links', related_name='answers')

    def __str__(self):
        return self.body

    def __int__(self):
        return self.link