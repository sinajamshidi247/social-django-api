from django.shortcuts import render
from rest_framework import generics , permissions , mixins
from .serializer import PostSerializer , CommentSerializer
from posts.models import Post , Comment
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


class Posts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CreatePosts(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)



    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user = user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class CommentCreate(generics.ListCreateAPIView,mixins.DestroyModelMixin):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        post =get_object_or_404(Post, pk=self.kwargs['post_id'])
        return Comment.objects.filter(post=post,pk = self.kwargs['comment_id'],user=user)

    def perform_create(self, serializer):
            if self.get_queryset().exists():

                raise ValidationError('you have already comment for this post')
            else:

                serializer.save(user=self.request.user,post=Post.objects.get(pk=self.kwargs['post_id']))
        

    def delete(self,request,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('you never voted for this post loser')


class DeletePost(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def delete(self,request,*args,**kwargs):
        post = Post.objects.filter(pk=kwargs['pk'],user = self.request.user.id)
        if post.exists():
            return self.destroy(request,*args,**kwargs)
        else:
            raise ValidationError('this isnt your post')


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'],password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)},status=status.HTTP_200_OK)
        except IntegrityError:
            return JsonResponse({'error':'that user name has been already token'})
    else:
        return JsonResponse({'error':'you should post the info silly ! '})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error':'Could not login. Please check username and password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                token = Token.objects.get(user=user)
                # login(request,user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=status.HTTP_200_OK)