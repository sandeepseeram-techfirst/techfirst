# db.listingsAndReviews.aggregate([ 
  { $match : { property_type : "House" } },
  { $limit: 2 },
  { $project: {
    "name": 1,
    "bedrooms": 1,
    "price": 1
  }}
])      


[
  {
    _id: '16253247',
    name: 'Gorgeous Remodeled Modern Home w/ Beach Across St.',
    bedrooms: 2,
    price: 194.00
  },
  {
    _id: '18616850',
    name: 'The Paddington Cottage | Sydney Eastern Suburbs',
    bedrooms: 3,
    price: 350.00
  }
]
Atlas atlas-8iy36m-shard-0 [primary] sample_airbnb>