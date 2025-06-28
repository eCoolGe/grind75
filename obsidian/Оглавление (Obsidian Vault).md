## Все задачи
> [!EXAMPLE]  
> ```dataview
> TABLE title_rus AS "Название", difficulty AS "Сложность", time AS "Время", space AS "Память"
> FROM "problems"
> SORT File ASC
> ```


### Сортировка задач по сложности
#### `Easy` сложность
> [!DONE]  
> ```dataview
> TABLE title_rus AS "Название", time AS "Время", space AS "Память"
> FROM "problems"
> WHERE difficulty = "Easy"
> SORT File ASC
> ```

#### `Medium` сложность 
> [!ATTENTION]  
> ```dataview
> TABLE title_rus AS "Название", time AS "Время", space AS "Память"
> FROM "problems"
> WHERE difficulty = "Medium"
> SORT File ASC
> ```

#### `Hard` сложность
> [!FAIL]  
> ```dataview
> TABLE title_rus AS "Название", time AS "Время", space AS "Память"
> FROM "problems"
> WHERE difficulty = "Hard"
> SORT File ASC
> ```

### Задачи типа `Array`
```dataview
LIST
FROM "problems"
WHERE contains(topics, "Array")
SORT difficulty DESC
```
==P.S. Для примера, чтобы я не забыл, как это делается, позже поправлю==

### Задачи не из `Grind75`
```dataview
TABLE title_rus, difficulty, time, space
FROM "problems"
WHERE grind75 = False
SORT File ASC
```

## Легенда

- `tags:` - для большого обозначения, что это (`#problem` - задача, `#template` - шаблон)
- `#теги-в-конце-файла` - для типа задач, например
- чекбокс `grind75` - для обозначения, что задача входит в лист [Grind75](https://www.techinterviewhandbook.org/grind75/)

