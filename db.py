from mongoengine import *

connect('tumblelog')

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    content = StringField()

#ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
#post1 = Post(title='Fun with MongoEngine', author=ross)
#post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
#post1.save()


    
