import graphene
from .models import Customer
from .types import CustomerType  # Make sure you have this defined in types.py


class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)

    def resolve_all_customers(root, info):
        return Customer.objects.all()


schema = graphene.Schema(query=Query)
