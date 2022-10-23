from api.services.crud import CrudService


class UserService(CrudService):
    def __init__(self, collection_name):
        super().__init__(collection_name)


UserServiceImpl = UserService("users")
