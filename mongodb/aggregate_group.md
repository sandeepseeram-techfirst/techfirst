# db.listingsAndReviews.aggregate(
    [ { $group : { _id : "$property_type" } } ]
)              

[
  { _id: 'Aparthotel' },
  { _id: 'Apartment' },
  { _id: 'Barn' },
  { _id: 'Bed and breakfast' },
  { _id: 'Boat' },
  { _id: 'Boutique hotel' },
  { _id: 'Bungalow' },
  { _id: 'Cabin' },
  { _id: 'Camper/RV' },
  { _id: 'Campsite' },
  { _id: 'Casa particular (Cuba)' },
  { _id: 'Castle' },
  { _id: 'Chalet' },
  { _id: 'Condominium' },
  { _id: 'Cottage' },
  { _id: 'Earth house' },
  { _id: 'Farm stay' },
  { _id: 'Guest suite' },
  { _id: 'Guesthouse' },
  { _id: 'Heritage hotel (India)' }
]
Atlas atlas-8iy36m-shard-0 [primary] sample_airbnb>