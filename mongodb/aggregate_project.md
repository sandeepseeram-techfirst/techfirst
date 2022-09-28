# db.restaurants.aggregate([
  {
    $project: {
      "name": 1,
      "cuisine": 1,
      "address": 1
    }
  },
  {
    $limit: 5
  }
])              

[
    {
      _id: ObjectId("5eb3d668b31de5d588f4292a"),
      address: {
        building: '2780',
        coord: [ -73.98241999999999, 40.579505 ],
        street: 'Stillwell Avenue',
        zipcode: '11224'
      },
      cuisine: 'American',
      name: 'Riviera Caterer'
    },
    {
      _id: ObjectId("5eb3d668b31de5d588f4292b"),
      address: {
        building: '7114',
        coord: [ -73.9068506, 40.6199034 ],
        street: 'Avenue U',
        zipcode: '11234'
      },
      cuisine: 'Delicatessen',
      name: "Wilken'S Fine Food"
    },
    {
      _id: ObjectId("5eb3d668b31de5d588f4292c"),
      address: {
        building: '2206',
        coord: [ -74.1377286, 40.6119572 ],
        street: 'Victory Boulevard',
        zipcode: '10314'
      },
      cuisine: 'Jewish/Kosher',
      name: 'Kosher Island'
    },
    {
      _id: ObjectId("5eb3d668b31de5d588f4292d"),
      address: {
        building: '469',
        coord: [ -73.961704, 40.662942 ],
        street: 'Flatbush Avenue',
        zipcode: '11225'
      },
      cuisine: 'Hamburgers',
      name: "Wendy'S"
    },
    {
      _id: ObjectId("5eb3d668b31de5d588f4292e"),
      address: {
        building: '1007',
        coord: [ -73.856077, 40.848447 ],
        street: 'Morris Park Ave',
        zipcode: '10462'
      },
      cuisine: 'Bakery',
      name: 'Morris Park Bake Shop'
    }
  ]
  Atlas atlas-8iy36m-shard-0 [primary] sample_restaurants>