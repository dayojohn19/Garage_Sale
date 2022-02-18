[{ "model": "ApplicationGarage.listing", "pk": 1, "fields": { "owner": "", "title": "again", "description": "asd", "price": 2, "category": "Hayop", "link": "/formImages/pngwing.com-5_7o4fnD4.png", "time": "Thursday 17 February 2022 09:42:41 " } }, { "model": "ApplicationGarage.listing", "pk": 2, "fields": { "owner": "", "title": "again", "description": "asd", "price": 2, "category": "Hayop", "link": "/formImages/pngwing.com-5_7o4fnD4.png", "time": "Thursday 17 February 2022 09:43:55 " } }, { "model": "ApplicationGarage.listing", "pk": 3, "fields": { "owner": "", "title": "again", "description": "asd", "price": 2, "category": "Hayop", "link": "/formImages/pngwing.com-5_7o4fnD4.png", "time": "Thursday 17 February 2022 09:44:27 " } }]


arr = [{ 'aaa': 1 }, { 'bbb': 2 }, { 'ccc': 3 }, 'ddd', 'eee']

console.log(
    // arr.remove(1),
    arr[1], '-----', arr.indexOf(arr[1])
)
console.log(arr.splice(2,1))
console.log('Current: ',arr)