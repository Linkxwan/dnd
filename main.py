import os

def print_dir_structure(path: str, indent: str = ""):
    if not os.path.exists(path):
        print(f"Путь {path} не существует.")
        return

    items = sorted(os.listdir(path))
    for index, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_dir = os.path.isdir(full_path)
        prefix = "├── " if index < len(items) - 1 else "└── "

        print(indent + prefix + item)
        if is_dir:
            # Для подпапок добавляем отступ с │ для визуализации дерева
            extension = "│   " if index < len(items) - 1 else "    "
            print_dir_structure(full_path, indent + extension)

if __name__ == "__main__":
    root_path = "src"  # Можно изменить на любую нужную папку
    print(root_path)
    print_dir_structure(root_path)
