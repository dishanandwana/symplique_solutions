`http://127.0.0.1:8000/reminders/`
To add reminder 

send a POST request with the required input data in JSON format:
```sh
{
  "user": 1,  // Assuming the user ID is 1
  "date": "2024-03-12",
  "time": "08:00:00",
  "message": "Remember to attend the meeting"
}
```
In return you will get a response

```sh
{
    "id": 1,
    "user": 1,
    "date": "2024-03-12",
    "time": "08:00:00",
    "message": "Remember to attend the meeting"
}
```
**Note**


**To Access Admin Panel**


**Username=admin**

**Password=admin**

