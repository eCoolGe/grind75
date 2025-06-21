## Все задачи
```dataview
TABLE title_rus, difficulty, topics, time, space
FROM "problems"
```

### Задачи типа `Array`
```dataview
LIST
FROM "problems"
WHERE contains(topics, "Array")
SORT difficulty DESC
```
==P.S. Для примера, чтобы я не забыл, как это делается, позже поправлю==

## Легенда

- `tags:` - для большого обозначения, что это (`#problem` - задача, `#template` - шаблон)
- `#теги-в-конце-файла` - для типа задач, например
- чекбокс `grind75` - для обозначения, что задача входит в лист [Grind75](https://www.techinterviewhandbook.org/grind75/)