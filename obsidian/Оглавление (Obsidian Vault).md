## Все задачи
> [!EXAMPLE]  
> ```dataview
> TABLE title_rus AS "Название", difficulty AS "Сложность", time AS "Время", space AS "Память"
> FROM "problems"
> SORT file.name ASC 
> ```


### Сортировка задач по сложности
#### `Easy` сложность
> [!DONE]  
> ```dataview
> TABLE title_rus AS "Название", time AS "Время", space AS "Память"
> FROM "problems"
> WHERE difficulty = "Easy"
> SORT file.name ASC 
> ```

#### `Medium` сложность 
> [!ATTENTION]  
> ```dataview
> TABLE title_rus AS "Название", time AS "Время", space AS "Память"
> FROM "problems"
> WHERE difficulty = "Medium"
> SORT file.name ASC 
> ```

#### `Hard` сложность
> [!FAIL]  
> ```dataview
> TABLE title_rus AS "Название", time AS "Время", space AS "Память"
> FROM "problems"
> WHERE difficulty = "Hard"
> SORT file.name ASC 
> ```

### Сортировка задач по категориям
> [!INFO]  
> ```dataview
> TABLE rows.file.link AS "🇺🇸    Указатель", rows.title_rus AS "🇷🇺    Название"
> FROM "problems"
> FLATTEN topics AS topic 
> GROUP BY topic AS "\#"
> ```

### Задачи не из `Grind75`
> [!TIP]  
> ```dataview
> TABLE title_rus, difficulty, time, space
> FROM "problems"
> WHERE grind75 = False
> SORT file.name ASC
> ```

## Легенда

- `tags:` - для большого обозначения, что это (`#problem` - задача, `#template` - шаблон)
- `#теги-в-конце-файла` - для типа задач, например
- чекбокс `grind75` - для обозначения, что задача входит в лист [Grind75](https://www.techinterviewhandbook.org/grind75/)

