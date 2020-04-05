# Hack diary DB (just for learning purposes!)

Using these scripts you can fix marks (change 2 and 3 to 5), remove chastisements and create random commendations.

## Description

There are three useful functions in the module:

- `fix_marks` — specified school kid's marks (2 and 3) will be changed to 5.
- `remove_chastisements` — remove all chastisements of the required school kid.
- `create_commendation` — create commendation for the required school kid and subject on the last lesson.

## Requirements

In order to use these scripts you need to download [this repo](https://github.com/devmanorg/e-diary/tree/master) and put
`scripts.py` in the root of the folder.

## How to run

* Run Django Shell by printing `python manage.py shell` in terminal.

* Then import the module by using `import scripts`.

## How to use

#### Fix marks
```
fix_marks("Фролов Иван")
```

#### Remove chastisements
```
remove_chastisements("Семенова Ева")
```

#### Сreate commendation
```
fix_marks("Крахман Алевтин", "Музыка")
```

All functions are decorated by the function, 
which checks if the required school kid exists and she/he is only one. 
If not, the error message will be printed.

## Project's goal

The code is written for educational purposes in the online course for web developers [Devman](https://dvmn.org).
