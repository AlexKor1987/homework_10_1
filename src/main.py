
list_of_id = [
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]


new_list_of_id = []
for number in range(len(list_of_id)):
     if list_of_id[number]["state"] == "EXECUTED":
          new_list_of_id.append(list_of_id[number])
         #print(list_of_id[number])
print(new_list_of_id)



