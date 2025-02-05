import graphene
from graphene_django.types import DjangoObjectType
from .models import PartnerApplication

# Define GraphQL Type
class PartnerApplicationType(DjangoObjectType):
    class Meta:
        model = PartnerApplication

# Define Query Type
class Query(graphene.ObjectType):
    all_applications = graphene.List(PartnerApplicationType)

    def resolve_all_applications(self, info, **kwargs):
        return PartnerApplication.objects.all()

# Define Mutation for Creating a New Application
class CreatePartnerApplication(graphene.Mutation):
    class Arguments:
        company_name = graphene.String(required=True)
        company_field = graphene.String(required=True)
        company_size = graphene.String(required=True)
        company_linkedin = graphene.String()
        company_website = graphene.String()
        contact_person_name = graphene.String(required=True)
        contact_person_email = graphene.String(required=True)
        contact_person_phone = graphene.String(required=True)
        reason_for_applying = graphene.String(required=True)

    application = graphene.Field(PartnerApplicationType)

    def mutate(self, info, company_name, company_field, company_size, contact_person_name, contact_person_email, contact_person_phone, reason_for_applying, company_linkedin=None, company_website=None):
        application = PartnerApplication(
            company_name=company_name,
            company_field=company_field,
            company_size=company_size,
            company_linkedin=company_linkedin,
            company_website=company_website,
            contact_person_name=contact_person_name,
            contact_person_email=contact_person_email,
            contact_person_phone=contact_person_phone,
            reason_for_applying=reason_for_applying
        )
        application.save()
        return CreatePartnerApplication(application=application)

# Define Mutation Type
class Mutation(graphene.ObjectType):
    create_partner_application = CreatePartnerApplication.Field()

# Define the Schema
schema = graphene.Schema(query=Query, mutation=Mutation)
