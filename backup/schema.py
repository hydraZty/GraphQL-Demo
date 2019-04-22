import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from database import db_session
from models import Department as DepartmentModel
from models import Employee as EmployeeModel
from models import Role as RoleModel


class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel


class Query(graphene.ObjectType):
    who_am_i = graphene.String(name=graphene.String(default_value="stranger"))
    employees = graphene.List(Employee, name=graphene.String(),
                              id=graphene.Int())
    departments = graphene.List(Department,id=graphene.Int())

    def resolve_who_am_i(self, info, name):
        return 'Hello ' + name

    def resolve_employees(self, info, **args):
        query = Employee.get_query(info)
        for field, value in args.items():
            if field == 'name':
                query = query.filter(value == getattr(EmployeeModel, 'name'))
            if field == 'id':
                query = query.filter(value == getattr(EmployeeModel, 'id'))
        return query

    def resolve_departments(self,info, **args):
        return Department.get_query(info)


schema = graphene.Schema(query=Query)
