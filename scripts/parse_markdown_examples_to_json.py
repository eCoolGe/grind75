import ast
import re


def parse_markdown_examples_to_json(text: str):
    examples = []
    raw_blocks = re.split(r"\*\*Example \d+:\*\*", text)

    for idx, block in enumerate(raw_blocks, 1):
        prefix = f"Example {idx}"

        # Убираем пробелы в конце строк
        block = "\n".join(line.rstrip() for line in block.splitlines())

        # Извлекаем блок Input
        input_match = re.search(r"\*\*Input:\*\*\s*(.*?)(?=\n\*\*|$)", block, re.DOTALL)
        if not input_match:
            continue
        input_text = input_match.group(1).strip()

        # Преобразуем значения в python-эквиваленты
        input_text = (
            input_text
            .replace("null", "None")
            .replace("true", "True")
            .replace("false", "False")
        )

        # Подготовка списка строк
        input_lines = [line.strip().rstrip(",") for line in input_text.splitlines() if line.strip()]

        try:
            if '=' in input_text:
                # Формат: key = [...]
                # Преобразуем к виду словаря: {"key": [...]}
                input_expr = "{" + re.sub(r"(\w+)\s*=", r'"\1":', input_text) + "}"
                input_data = ast.literal_eval(input_expr)
            else:
                # Формат: [...], [...]
                input_data = {"args": [ast.literal_eval(line) for line in input_lines]}
        except Exception as e:
            print(f"{prefix} ⚠ Ошибка в input: {e}")
            continue

        # Извлекаем Output
        output_match = re.search(r"\*\*Output:\*\*\s*(.*?)\s*(?:\n|$)", block)
        if not output_match:
            continue
        output_text = output_match.group(1).strip()
        output_text = (
            output_text
            .replace("null", "None")
            .replace("true", "True")
            .replace("false", "False")
        )

        try:
            output_data = ast.literal_eval(output_text)
        except Exception as e:
            print(f"{prefix} ⚠ Ошибка в output: {e}")
            continue

        examples.append({
            "input": input_data,
            "output": output_data
        })

    return {"examples": examples}
