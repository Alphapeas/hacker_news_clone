from rest_framework.pagination import PageNumberPagination


class PostApiPagination(PageNumberPagination):
    """News post`s pagination"""
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 150

