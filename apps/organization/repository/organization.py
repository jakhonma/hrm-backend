from orm import BaseRepository
from apps.organization.models import Organization


class OrganizationRepository(BaseRepository):
    model = Organization
