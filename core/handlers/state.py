from aiogram.fsm.state import StatesGroup, State


class AddProductAdminState(StatesGroup):
    MAIN = State()


class AddProductAdminBsState(StatesGroup):
    NAME = State()
    PRICE = State()


class AddProductAdminCocState(StatesGroup):
    NAME = State()
    PRICE = State()


class AddProductAdminPmState(StatesGroup):
    NAME = State()
    PRICE = State()


class AddProductAdminCrState(StatesGroup):
    NAME = State()
    PRICE = State()


class AddProductAdminCodmState(StatesGroup):
    NAME = State()
    PRICE = State()


class DeletedProductAdminState(StatesGroup):
    MAIN = State()
    ID = State()


class DisplayProductInCatalogState(StatesGroup):
    MAIN = State()


class EmailState(StatesGroup):
    EMAIL = State()
