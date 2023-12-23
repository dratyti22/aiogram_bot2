from aiogram.fsm.state import StatesGroup, State


class AddProductAdminState(StatesGroup):
    MAIN = State()
    NAME = State()
    PRICE = State()
