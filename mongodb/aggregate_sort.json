# db.listingsAndReviews.aggregate([ 
  { 
    $sort: { "accommodates": -1 } 
  },
  {
    $project: {
      "name": 1,
      "accommodates": 1
    }
  },
  {
    $limit: 5
  }
])           



[
  {
    _id: '19990097',
    name: 'House close to station & direct to opera house....',
    accommodates: 16
  },
  { _id: '19587001', name: 'Kaena O Kekai', accommodates: 16 },
  {
    _id: '20958766',
    name: 'Great Complex of the Cellars',
    accommodates: 16
  },
  {
    _id: '12509339',
    name: 'Barra da Tijuca beach house',
    accommodates: 16
  },
  {
    _id: '20455499',
    name: 'DOWNTOWN VIP MONTREAL ,HIGH END DECOR,GOOD VALUE..',
    accommodates: 16
  }
]
Atlas atlas-8iy36m-shard-0 [primary] sample_airbnb>