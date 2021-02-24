from rest_framework import serializers
from posts.models import Post , Comment

class PostSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    poster_id = serializers.ReadOnlyField(source='user.id')
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta :
        model = Post
        fields = ('poster_id','user','body','slug','created')


class CommentSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    is_reply = serializers.BooleanField()
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    reply = serializers.ReadOnlyField()
    post = serializers.ReadOnlyField(source='post.body')
    




    class Meta :
        model = Comment
        fields = '__all__'




