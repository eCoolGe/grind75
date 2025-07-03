import logging
import re
import shutil
from pathlib import Path

import yaml

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Глобальные пути
ROOT = Path(__file__).resolve().parent.parent
README = ROOT / 'README.md'
OBSIDIAN = ROOT / 'obsidian'
DOCS = ROOT / 'docs'
SELECTED_DIRS = ['problems']


def inject_info_block(path: Path, meta: dict):
    """
    Вставляет блок [!INFO] после frontmatter (---) и до заголовка '## Решение'.
    """
    try:
        text = path.read_text(encoding='utf-8')
        parts = text.split('---', 2)
        if len(parts) < 3:
            logger.debug(f"{path}: отсутствует frontmatter")
            return

        frontmatter = f"---{parts[1]}---"
        body = parts[2].lstrip()

        # Поиск заголовка '## Решение'
        solution_match = re.search(r'^##\s+Решение\b', body, re.MULTILINE)
        if not solution_match:
            logger.debug(f"{path.relative_to(path.parents[1])}: нет заголовка '## Решение'")
            return

        insert_pos = solution_match.start()

        # Сборка данных
        title_rus = meta.get("title_rus", "Без названия")
        leetcode_url = meta.get("leetcode_url", "")
        time = meta.get("time", "?")
        space = meta.get("space", "?")

        leetcode_md = f"[{leetcode_url.split('/')[-2]}]({leetcode_url})" if leetcode_url else "—"

        # Формирование [!INFO] блока
        info_block = "\n\n> [!INFO]  \n"
        info_block += f"> **🇷🇺 Название:** {title_rus}  \n"
        info_block += f"> **LeetCode:** {leetcode_md}  \n"
        info_block += f"> **Временная сложность:** {time}  \n"
        info_block += f"> **Пространственная сложность:** {space}  \n\n"

        # Вставка блока
        body_new = body[:insert_pos] + info_block + body[insert_pos:]
        final_text = f"---\n{parts[1].strip()}\n---\n\n{body_new.lstrip()}"

        path.write_text(final_text, encoding='utf-8')
        logger.info(f"[INFO] блок вставлен в: {path.relative_to(path.parents[1])}")

    except Exception as e:
        logger.error(f"{path}: ошибка при вставке блока [!INFO]: {e}")


def copy_readme_to_index():
    """Копирует README.md в docs/index.md"""
    DOCS.mkdir(exist_ok=True)
    target = DOCS / 'index.md'
    if README.exists():
        shutil.copyfile(README, target)
        logger.info(f"README.md скопирован в {target}")
    else:
        logger.warning("README.md не найден — шаг пропущен")


def copy_selected_dirs():
    """Копирует выбранные папки из Obsidian в docs"""
    for name in SELECTED_DIRS:
        src = OBSIDIAN / name
        dst = DOCS / name
        if not src.exists():
            logger.warning(f"Папка {src} не найдена — пропущена")
            continue
        if dst.exists():
            shutil.rmtree(dst)
            logger.info(f"Старая папка удалена: {dst}")
        shutil.copytree(src, dst)
        logger.info(f"{src} скопирован в {dst}")


def convert_metadata_to_tags(path: Path):
    """
    Обновляет YAML frontmatter в .md файле:
    добавляет difficulty и topics к tags.
    Также вызывает вставку [!INFO] блока.
    """
    try:
        text = path.read_text(encoding='utf-8')
        if not text.startswith('---'):
            logger.debug(f"{path.relative_to(ROOT)}: нет frontmatter")
            return

        parts = text.split('---', 2)
        if len(parts) < 3:
            logger.warning(f"{path.relative_to(ROOT)}: ошибка разбора frontmatter")
            return

        header_raw, content = parts[1], parts[2].lstrip()
        meta = yaml.safe_load(header_raw)

        tags = meta.get('tags', [])
        if not isinstance(tags, list):
            tags = [tags]

        for key in ('difficulty', 'topics'):
            value = meta.get(key)
            if isinstance(value, str):
                tags.append(value)
            elif isinstance(value, list):
                tags.extend(value)

        meta['tags'] = sorted(set(tags))
        new_header = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
        new_text = f"---\n{new_header}\n---\n\n{content}"
        path.write_text(new_text, encoding='utf-8')
        logger.info(f"Обновлён frontmatter: {path.relative_to(ROOT)}")

        inject_info_block(path, meta)

    except Exception as e:
        logger.error(f"{path.relative_to(ROOT)}: ошибка при обработке: {e}")


def process_markdown_files():
    """Обрабатывает все .md файлы в скопированных директориях"""
    for subdir in SELECTED_DIRS:
        for path in (DOCS / subdir).rglob("*.md"):
            convert_metadata_to_tags(path)


def main():
    logger.info("=== Подготовка документации ===")
    copy_readme_to_index()
    copy_selected_dirs()
    process_markdown_files()
    logger.info("=== Завершено ===")


if __name__ == "__main__":
    main()
