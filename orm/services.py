from typing import Any, Dict
from django.db.models import Model, QuerySet
from .repository import BaseRepository


class BaseService:
    repository: BaseRepository = None

    def list(self, select_related=[], prefetch_related=[]) -> QuerySet:
        return self.repository.all(select_related, prefetch_related)

    def filter(self, select_related=[], prefetch_related=[], **filters) -> QuerySet:
        return self.repository.filter(select_related, prefetch_related, **filters)

    def get(self, select_related=[], prefetch_related=[], **kwargs) -> Model:
        return self.repository.get_by_id(select_related, prefetch_related, **kwargs)

    def create(self, validated_data: Dict[str, Any]) -> Model:
        return self.repository.create(validated_data)

    def update(self, pk: int, validated_data: Dict[str, Any]) -> Model:
        return self.repository.update(pk, validated_data)

    def delete(self, pk: int) -> None:
        return self.repository.delete(pk)
    
    def increment_field(self, field_name: str, select_related=[], prefetch_related=[], **kwargs) -> Model:
        return self.repository.increment_field(field_name, select_related, prefetch_related, **kwargs)
