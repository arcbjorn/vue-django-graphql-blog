import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphql_relay.node.node import from_global_id
from graphene_django.filter import DjangoFilterConnectionField

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['category_name']
        interfaces = (graphene.relay.Node,)

class LanguageNode(DjangoObjectType):
    class Meta:
        model = Language
        filter_fields = ['language_name']
        interfaces = (graphene.relay.Node,)

class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = [
              'post_name',
              'post_category__category_name',
              'post_language__language_name'
               ]
        interfaces = (graphene.relay.Node,)

class CreateCategory(graphene.relay.ClientIDMutation):
    category = graphene.Field(CategoryNode)

    class Input:
        category_name = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        category = Category(
            category_name=input.get('category_name')
        )
        category.save()
        return CreateCategory(category=category)

class CreatePost(graphene.relay.ClientIDMutation):
    post = graphene.Field(PostNode)

    class Input:
        post_name = graphene.String()
        post_category = graphene.String()
        post_language = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        post = Post(
            post_name=input.get('post_name'),
            post_city=Category.objects.get(
                city_name=input.get('post_category')),
            post_title=Language.objects.get(
                title_name=input.get('post_language'))
        )
        post.save()
        return CreatePost(post=post)

class Query(object):
    category = graphene.relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    language = graphene.relay.Node.Field(LanguageNode)
    all_languages = DjangoFilterConnectionField(LanguageNode)

    post = graphene.relay.Node.Field(PostNode)
    all_posts = DjangoFilterConnectionField(PostNode)

class UpdatePost(graphene.relay.ClientIDMutation):
    post = graphene.Field(PostNode)

    class Input:
        id = graphene.String()
        post_name = graphene.String()
        post_category = graphene.String()
        post_language = graphene.String()
    
    def mutate_and_get_payload(root, info, **input):
        post = Post.objects.get(
            pk=from_global_id(input.get('id'))[1])
        post.post_name = input.get('post_name')
        post.post_category = Category.objects.get(
            category_name=input.get('post_category'))
        post.post_language = Language.objects.get(
            language_name=input.get('post_language'))
        post.save()
        return UpdatePost(post=post)

class DeletePost(graphene.relay.ClientIDMutation):
    post = graphene.Field(PostNode)

    class Input:
        id = graphene.String()
    
    def mutate_and_get_payload(root, info, **input):
        post = Post.objects.get(
            pk=from_global_id(input.get('id'))[1])
        post.delete()
        return DeletePost(post=post)

class Mutation(graphene.AbstractType):
    create_category = CreateCategory.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()