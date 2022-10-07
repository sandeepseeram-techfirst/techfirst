# db.posts.aggregate([
  {
    $match: { likes: { $gt: 1 } }
  },
  {
    $group: { _id: "$category", totalLikes: { $sum: "$likes" } }
  }
])    


[ { _id: 'News', totalLikes: 3 }, { _id: 'Event', totalLikes: 8 } ]
Atlas atlas-8iy36m-shard-0 [primary] blog>