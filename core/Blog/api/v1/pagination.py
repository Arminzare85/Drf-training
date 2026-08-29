from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 3
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'meta': {
                'total_objects': self.page.paginator.count,
                'page_count': self.page.paginator.num_pages,
                'current_page': self.page.number,
                'page_size': self.page.paginator.per_page
            },
            'data': data
        })