db.movies.aggregate([
  {
    $search: {
      index: "default",
      text: {
        query: "star wars",
        path: "title"
      },
    },
  },
  {
    $project: {
      title: 1,
      year: 1,
    }
  }
])        


[
  {
    _id: ObjectId("573a13c0f29313caabd62f62"),
    year: 2008,
    title: 'Star Wars: The Clone Wars'
  },
  {
    _id: ObjectId("573a13bdf29313caabd599ca"),
    title: 'Robot Chicken: Star Wars',
    year: 2007
  },
  {
    _id: ObjectId("573a1396f29313caabce37ff"),
    title: 'Star!',
    year: 1968
  },
  {
    _id: ObjectId("573a13a6f29313caabd17d08"),
    title: 'Star',
    year: 2001
  },
  {
    _id: ObjectId("573a1397f29313caabce68f6"),
    year: 1977,
    title: 'Star Wars: Episode IV - A New Hope'
  }
]
Atlas atlas-8iy36m-shard-0 [primary] sample_mflix>