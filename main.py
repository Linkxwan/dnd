import os

# Список всех директорий и файлов
structure = {
    "src": {
        "core": [
            "__init__.py",
            "entities.py",
            "rules_engine.py",
            "game_state.py",
            "event_bus.py",
            "turn_manager.py",
        ],
        "agents": [
            "__init__.py",
            "agent.py",
            "npc_agent.py",
            "player_agent.py",
            "memory.py",
        ],
        "llm": [
            "__init__.py",
            "llm_adapter.py",
            "openai_adapter.py",
        ],
        "storage": [
            "__init__.py",
            "storage_adapter.py",
            "json_storage.py",
        ],
        "ui": [
            "__init__.py",
            "console_ui.py",
            "prompts.py",
        ],
    },
    "tests": [
        "__init__.py",
        "test_game_state.py",
        "test_agents.py",
        "test_rules_engine.py",
        "test_llm.py",
        "test_storage.py",
    ],
    "requirements.txt": None,
    "README.md": None,
}

# Функция для создания структуры проекта
def create_project_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, list):
            # Создаем файлы внутри текущей директории
            os.makedirs(path, exist_ok=True)
            for file in value:
                with open(os.path.join(path, file), "w") as f:
                    # Здесь можно писать шаблон в файл (например, заголовок, описание)
                    f.write(f"# {file}\n")
        elif isinstance(value, dict):
            # Рекурсивный вызов для создания вложенных директорий
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, value)
        else:
            # Создаем файлы на верхнем уровне (requirements.txt, README.md)
            with open(path, "w") as f:
                if path.endswith("requirements.txt"):
                    f.write("# Зависимости проекта\n")
                elif path.endswith("README.md"):
                    f.write("# Описание проекта\n")
                else:
                    f.write(f"# {name}\n")

# Путь, где будет создан проект (можно изменить)
base_path = "game_project"

# Создаем структуру проекта
os.makedirs(base_path, exist_ok=True)
create_project_structure(base_path, structure)

print("Структура проекта создана успешно!")
