# from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
# from rest_framework.response import Response


# class MyPagination(PageNumberPagination, LimitOffsetPagination):
#     page_size = 2
#     max_page_size = 20
#     def get_pagination(self, data):
#         # response = super().get_pagination(data)
#         # response.data['offset'] = self.get_offset(self.request)
#         return Response({
#             'links': {
#               'next': self.get_next_link(),
#               'previous': self.get_previous_link()
#             },
#             'count': self.page.paginator.count,
#             'results': data,
#             'offset': self.get_offset(),
#         })