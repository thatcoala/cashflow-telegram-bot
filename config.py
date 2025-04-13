from aiogram.fsm.state import State, StatesGroup

# Категории расходов
CATEGORIES = {
    "🍔 Еда": "food",
    "🏠 Жилье": "house",
    "🚗 Транспорт": "transport",
    "👕 Одежда": "clothes",
    "💊 Здоровье": "health",
    "🎮 Развлечения": "entertainment",
    "📱 Связь": "communication",
    "📚 Образование": "education",
    "🎁 Подарки": "gifts",
    "💡 Другое": "other"
}

# Состояния FSM
class ExpenseStates(StatesGroup):
    waiting_for_amount = State()
    waiting_for_category = State()
    waiting_for_description = State()
    waiting_for_edit_field = State()
    waiting_for_edit_value = State()
    waiting_for_edit_id = State()
    waiting_for_delete_id = State() 