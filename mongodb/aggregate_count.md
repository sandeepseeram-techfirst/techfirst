# db.restaurants.aggregate([
  {
    $match: { "cuisine": "Chinese" }
  },
  {
    $count: "totalChinese"
  }
])    

[ { totalChinese: 2418 } ]
Atlas atlas-8iy36m-shard-0 [primary] sample_restaurants>