from pathlib import Path
import pandas as pd

def convert_csv_to_excel(df: pd.DataFrame, output_path: Path):
    df.to_excel(output_path, index=False)
    print(f"✅ Успешно сохранено в Excel: {output_path}")

def convert_csv_to_json(df: pd.DataFrame, output_path: Path):
    df.to_json(output_path, orient="records", indent=2)
    print(f"✅ Успешно сохранено в JSON: {output_path}")

def convert_csv_to_pickle(df: pd.DataFrame, output_path: Path):
    df.to_pickle(output_path)
    print(f"✅ Успешно сохранено в Pickle: {output_path}")

def main():
    sample_folder = Path("sample_data")
    output_folder = Path("output_data")
    output_folder.mkdir(exist_ok=True)

    filename = input("Введите имя CSV-файла (например, input.csv): ").strip()
    input_path = sample_folder / filename

    if not input_path.exists():
        print(f"❌ Файл {input_path} не найден.")
        return

    # Читаем CSV
    try:
        df = pd.read_csv(input_path)
        print(f"📥 Загружено: {input_path} ({df.shape[0]} строк)")
    except Exception as e:
        print(f"⚠️ Ошибка при загрузке CSV: {e}")
        return

    # Выбор формата
    fmt = input("Введите формат для конвертации (xlsx/json/pickle): ").strip().lower()

    output_file = output_folder / (input_path.stem + f".{fmt}")

    if fmt == "xlsx":
        convert_csv_to_excel(df, output_file)
    elif fmt == "json":
        convert_csv_to_json(df, output_file)
    elif fmt == "pickle":
        convert_csv_to_pickle(df, output_file)
    else:
        print("❌ Неподдерживаемый формат!")

if __name__ == "__main__":
    main()