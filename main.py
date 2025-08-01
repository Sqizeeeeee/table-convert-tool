from pathlib import Path
import pandas as pd

def convert_csv_to_excel(df: pd.DataFrame, output_path: Path):
    df.to_excel(output_path, index=False)
    print(f"✅ Successfully saved as Excel: {output_path}")

def convert_csv_to_json(df: pd.DataFrame, output_path: Path):
    df.to_json(output_path, orient="records", indent=2)
    print(f"✅ Successfully saved as JSON: {output_path}")

def convert_csv_to_pickle(df: pd.DataFrame, output_path: Path):
    df.to_pickle(output_path)
    print(f"✅ Successfully saved as Pickle: {output_path}")

def main():
    sample_folder = Path("sample_data")
    output_folder = Path("output_data")
    output_folder.mkdir(exist_ok=True)

    filename = input("Enter CSV filename (e.g., input.csv): ").strip()
    input_path = sample_folder / filename

    if not input_path.exists():
        print(f"❌ File {input_path} not found.")
        return

    # Read CSV
    try:
        df = pd.read_csv(input_path)
        print(f"📥 Loaded: {input_path} ({df.shape[0]} rows)")
    except Exception as e:
        print(f"⚠️ Error loading CSV: {e}")
        return

    # Choose format
    fmt = input("Enter output format (xlsx/json/pickle): ").strip().lower()

    output_file = output_folder / (input_path.stem + f".{fmt}")

    if fmt == "xlsx":
        convert_csv_to_excel(df, output_file)
    elif fmt == "json":
        convert_csv_to_json(df, output_file)
    elif fmt == "pickle":
        convert_csv_to_pickle(df, output_file)
    else:
        print("❌ Unsupported format!")

if __name__ == "__main__":
    main()