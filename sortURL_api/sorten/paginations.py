from rest_framework.pagination import CursorPagination

class IdPagination(CursorPagination):
    ordering = ['-id']
    page_size = 2