from typing import Any, Dict, Type, List
from django.db.models import Model, F, QuerySet
from django.shortcuts import get_object_or_404


class BaseRepository:
    model: Type[Model] = None

    @classmethod
    def base_queryset(cls, select_related: List[str]=[], prefetch_related: List[Any]=[]) -> QuerySet:
        """Base queryset with related loading"""
        queryset = cls.model.objects.all()
        if select_related:
            queryset = queryset.select_related(*select_related)
        if prefetch_related:
            queryset = queryset.prefetch_related(*prefetch_related)
        return queryset
    
    @classmethod
    def all(cls,select_related: List[str]=[], prefetch_related: List[Any]=[]) -> QuerySet:
        return cls.base_queryset(select_related, prefetch_related)

    @classmethod
    def filter(cls,select_related: List[str]=[], prefetch_related: List[Any]=[],  **filters) -> QuerySet:
        return cls.base_queryset(select_related, prefetch_related).filter(**filters)

    @classmethod
    def get_by_id(cls, select_related: List[str]=[], prefetch_related: List[Any]=[], **kwargs) -> Model:
        return get_object_or_404(cls.base_queryset(select_related, prefetch_related), **kwargs)

    @classmethod
    def create(cls, data: Dict[str, Any]) -> Model:
        return cls.model.objects.create(**data)

    @classmethod
    def update(cls, pk: int, data: Dict[str, Any]) -> Model:
        instance = cls.get_by_id(pk)
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    @classmethod
    def delete(cls, pk: int) -> None:
        instance = cls.get_by_id(pk)
        instance.delete()
    
    @classmethod
    def increment_field(cls, field_name: str, select_related: List[str]=[], prefetch_related: List[Any]=[], **kwargs) -> Model:
        """
        Har qanday sonli maydonni xavfsiz inkrement qiladi (F() bilan).
        :param pk: obyekt primary key
        :param field_name: maydon nomi (masalan 'total_views')
        :param step: qadam (default=1)
        """
        pk = kwargs.get('pk')
        cls.model.objects.filter(pk=pk).update(**{
            field_name: F(field_name) + 1
        })
        return cls.get_by_id(select_related, prefetch_related, **kwargs)
