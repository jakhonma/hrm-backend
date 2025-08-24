from apps.organization.serializers import OrganizationSerializer
from apps.organization.services import OrganizationService


class BaseOrganization:
    serializer_class = OrganizationSerializer
    services = OrganizationService()
