from aiogram.fsm.state import StatesGroup, State


class AddProductAdminBsState(StatesGroup):
    MAIN = State()
    NAME = State()
    PRICE = State()


class AddProductAdminCocState(StatesGroup):
    MAIN = State()
    NAME = State()
    PRICE = State()


class AddProductAdminPmState(StatesGroup):
    MAIN = State()
    NAME = State()
    PRICE = State()


class AddProductAdminCrState(StatesGroup):
    MAIN = State()
    NAME = State()
    PRICE = State()


class AddProductAdminCodmState(StatesGroup):
    MAIN = State()
    NAME = State()
    PRICE = State()
