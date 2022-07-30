from rest_framework import filters
from datetime import date

# class salaryfilter(filters.BaseFilterBackend):
#     """
#     Filter that only allows users to see their own objects.
#     """
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(soqqa__gte = value1, soqqa__lte=value2)
#

def filter_salary(queryset, value1, value2):
        if not value1 and not value2:
            return queryset

        queryset = queryset.filter(salary1__lte = value1, salary2__gte = value2 )
        return queryset



def filter_created_at(queryset, value):
        if not value:
            return queryset

        queryset = queryset.filter(create_at__gte = value)
        return queryset
