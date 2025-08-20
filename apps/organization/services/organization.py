from apps.organization.repository import OrganizationRepository
from orm import BaseService


class OrganizationService(BaseService):
    repository = OrganizationRepository
