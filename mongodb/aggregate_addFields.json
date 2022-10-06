# db.restaurants.aggregate([
  {
    $addFields: {
      avgGrade: { $avg: "$grades.score" }
    }
  },
  {
    $project: {
      "name": 1,
      "avgGrade": 1
    }
  },
  {
    $limit: 5
  }
])    


[
  {
    _id: ObjectId("5eb3d668b31de5d588f4292a"),
    name: 'Riviera Caterer',
    avgGrade: 9
  },
  {
    _id: ObjectId("5eb3d668b31de5d588f4292b"),
    name: "Wilken'S Fine Food",
    avgGrade: 10
  },
  {
    _id: ObjectId("5eb3d668b31de5d588f4292c"),
    name: 'Kosher Island',
    avgGrade: 10.5
  },
  {
    _id: ObjectId("5eb3d668b31de5d588f4292d"),
    name: "Wendy'S",
    avgGrade: 13.75
  },
  {
    _id: ObjectId("5eb3d668b31de5d588f4292e"),
    name: 'Morris Park Bake Shop',
    avgGrade: 8.2
  }
]
Atlas atlas-8iy36m-shard-0 [primary] sample_restaurants>