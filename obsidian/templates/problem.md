---
tags:
  - "#template"
---
<%*
// Получаем данные от пользователя
const title = await tp.system.prompt("Название задачи (как на LeetCode)");
const difficulty = await tp.system.suggester(["Легкий", "Средний", "Сложный"], ["Easy", "Medium", "Hard"]);
const topicsStr = await tp.system.prompt("Топики через запятую");
const time = await tp.system.prompt("Time complexity (O)") || "<сложность>";
const space = await tp.system.prompt("Space complexity (O)") || "<сложность>";

// Изменяем название файла и заголовок
await tp.file.rename(title);

// Обрабатываем топики
const topics = topicsStr?.split(",").map(t => t.trim());

// Генерируем название для URL
const urlName = title
  .toLowerCase()
  .replace(/['’]/g, '')               // убрать апострофы
  .replace(/[^a-z0-9]+/g, '-')       // заменить все кроме букв и цифр на дефис
  .replace(/^-+|-+$/g, '');          // убрать ведущие и конечные дефисы

// Формируем YAML-заголовок
const yaml = `---
title_rus: "<заголовок на русском языке>"
difficulty: "${difficulty}"
leetcode_url: "https://leetcode.com/problems/${urlName}/"
topics: [${topics.map(t => `"${t}"`).join(", ")}]
time: "O(${time})"
space: "O(${space})"
grind75: False
tags: ["problem"]
---
`;

// Формируем тело заметки с многострочными вставками
const body = `
## Решение

\`\`\`python
# Место для вставки кода
\`\`\`

## 🇺🇸 Условие

<!-- Место для вставки перевода на английском языке -->

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

<!-- Место для вставки примеров -->

\`\`\`json
# Место для вставки примеров в формате JSON
\`\`\`

## Ограничения

<!-- Место для вставки ограничений -->

## Потребление ресурсов
### ⏱ Time complexity: \`O(${time})\`

- <!-- Место для вставки разбора -->

**Итог:** \`O(${time})\`

### 🧠 Space complexity: \`O(${space})\`

- <!-- Место для вставки разбора -->

**Итог:** \`O(${space})\`
`;

// Добавляем теги в конец файла
const tags = `
${"#" + difficulty.toLowerCase()} ${topics.map(t => "#" + t.toLowerCase().replace(/\s+/g, "-")).join(" ")}
`;

tR = yaml + body + tags;
%>