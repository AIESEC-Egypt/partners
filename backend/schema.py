import graphene
import api.schema

class Query(api.schema.Query):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass
  
class Mutation(api.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)