import graphene
from crm.schema import Mutation as CRMMutation, CustomerType, ProductType, OrderType

class Query(CRMQuery, graphene.ObjectType):
    # optional: add queries here
    pass

class Mutation(CRMMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
