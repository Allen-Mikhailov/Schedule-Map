# Schedule Map

This is a simple python program that is designed to create a csv file 
that contains all of you and your friends schedules

## Requirments:
- pandas
- numpy

## Data:
This program takes data from a json file which by default is "./schedules.json"

This file must follow this data struct

```
{
    "name": [ [ "TeacherName", Period (int) ] ]
}
```

Ex:
```
{
    "Allen": [["Bishop", 5], ["Moncriffe", 4], ["Reyes", 1]],
}
```


## Use:
to use it run the command "py index.py" while in the directory
