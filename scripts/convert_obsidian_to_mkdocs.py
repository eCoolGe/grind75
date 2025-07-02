import os
import shutil
import yaml
from pathlib import Path

# Пути
ROOT = Path(__file__).parent.parent
README = ROOT / 'README.md'
OBSIDIAN = ROOT / 'obsidian'
DOCS = ROOT / 'docs'

# Какие папки копировать из Obsidian
SELECTED_DIRS = ['problems']

# --- Шаг 1: README.md → docs/index.md
DOCS.mkdir(exist_ok=True)
index_md = DOCS / 'index.md'
shutil.copyfile(README, index_md)

# --- Шаг 2: копирование выбранных папок
for subdir in SELECTED_DIRS:
    src = OBSIDIAN / subdir
    dst = DOCS / subdir
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

# --- Шаг 3: конвертация метаданных в теги
def process_file(path: Path):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return
    parts = text.split('---', 2)
    if len(parts) < 3:
        return
    header = parts[1]
    content = parts[2].lstrip()

    meta = yaml.safe_load(header)
    tags = meta.get('tags', [])
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

# Обработка всех .md файлов в docs/problems
for subdir in SELECTED_DIRS:
    for file in (DOCS / subdir).rglob("*.md"):
        process_file(file)
