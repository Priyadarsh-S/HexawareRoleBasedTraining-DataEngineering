// Database 
use food_delivery_assessment_db

// Collection
db.createCollection("restaurants")

// Inserting Data
db.restaurants.insertMany([
  {
    restaurant_id: 1, 
		name: "Spice Hub", 
		city: "Hyderabad", 
		cuisine: "Indian", 
		rating: 4.5, 
		avg_order_value: 450,
		delivery_available: true, 
		tags: ["biryani", "north indian", "family"], 
		contact: { 
			phone: "9876543210", 
			email: "spicehub@mail.com" 
		}
  },
  {
    restaurant_id: 2, 
		name: "Pizza Corner", 
		city: "Bangalore", 
    cuisine: "Italian", 
    rating: 4.2, 
    avg_order_value: 600,
    delivery_available: true, 
    tags: ["pizza", "fast food", "cheese"], 
    contact: { 
      phone: "9876543211", 
      email: "pizza@mail.com" 
    }
  },
  {
    restaurant_id: 3, 
    name: "Green Bowl", 
    city: "Chennai",
    cuisine: "Healthy", 
    rating: 4.7, 
    avg_order_value: 350,
    delivery_available: false, 
    tags: ["salad", "vegan", "healthy"], 
    contact: { 
      phone: null, 
      email: "greenbowl@mail.com" 
    }
  },
  {
    restaurant_id: 4, 
    name: "Burger Street", 
    city: "Hyderabad", 
    cuisine: "Fast Food",
    rating: 3.9, 
    avg_order_value: 300,
    delivery_available: true, 
    tags: ["burger", "fries", "fast food"], 
    contact: { 
      phone: "9876543213", 
      email: null 
    }
  },
  {
   	restaurant_id: 5, 
    name: "Royal Tandoor", 
    city: "Delhi", 
    cuisine: "Indian", 
    rating: 4.8, 
		avg_order_value: 800,
		delivery_available: true, 
		tags: ["tandoor", "north indian", "premium"], 
		contact: { 
			phone: "9876543214", 
			email: "royal@mail.com" 
		} 
  },
  {
    restaurant_id: 6, 
		name: "Tea Tales", 
		city: "Pune", 
		cuisine: "Cafe",
		rating: 4.1, 
		avg_order_value: 200,
		delivery_available: false, 
		tags: ["tea", "snacks", "cafe"], 
		contact: { 
			phone: "9876543215", 
			email: "tea@mail.com" 
		}
  },
  {
    restaurant_id: 7, 
		name: "Ocean Grill", 
		city: "Mumbai", 
		cuisine: "Seafood", 
		rating: 4.6, 
		avg_order_value: 900,
		delivery_available: true, 
		tags: ["fish", "grill", "premium"], 
		contact: { 
		phone: "9876543216", 
		email: "ocean@mail.com" 
		}
  },
  {
    restaurant_id: 8, 
		name: "Dosa Point", 
		city: "Chennai",
		cuisine: "South Indian", 
		rating: 4.3, 
		avg_order_value: 250,
		delivery_available: true, 
		tags: ["dosa", "idli", "breakfast"], 
		contact: { 
			phone: null, 
			email: null 
		}
  }
])

// Assessment Questions (Basic Find Queries)
// 1. Display all restaurants.
db.restaurants.find()

// 2. . Display only: name, city, cuisine, Do not show _id.
db.restaurants.find(
  {},
  {name: 1, city: 1, cuisine: 1, _id:0}
)

// 3. Find all restaurants from Hyderabad.
db.restaurants.find({ city: "Hyderabad"})

// 4. Find all Indian cuisine restaurants.
db.restaurants.find({cuisine: "Indian"})

// 5. Find restaurants where delivery is available.
db.restaurants.find({delivery_available: true})

// Comparison Operators
// 6. Find restaurants with rating greater than 4.5.
db.restaurants.find({
  rating: {$gt:4.5}
})

// 7. Find restaurants where average order value is less than ₹400.
db.restaurants.find({
  avg_order_value: {$lt:400}
})

// 8. Find restaurants where rating is between 4.0 and 4.7.
db.restaurants.find({
  rating: {$gte:4.0},
  rating: {$lte: 4.7}
})

// 9. Find restaurants where average order value is greater than or equal to ₹600.
db.restaurants.find({
  avg_order_value: {$gte:600}
})

// Logical Operators
// 10. Find restaurants from Hyderabad with delivery available.
db.restaurants.find({
  city: "Hyderabad",
  delivery_available: true
})

// 11. Find restaurants that are either from Chennai or cuisine is Indian.
db.restaurants.find({
  $or: [
    {city: "Chennai"},
    {cuisine: "Indian"}
  ]
})

// 12. Find restaurants where delivery is not available
db.restaurants.find({
  delivery_available: false
})

// IN / NOT IN
// 13. Find restaurants from these cities: Hyderabad, Delhi, Mumbai 
db.restaurants.find({
  city: { $in: ["Hyderabad", "Delhi", "Mumbai"]}
})

// 14. Find restaurants whose cuisine is either: Indian, Italian, Cafe
db.restaurants.find({
  cuisine: { $in: ["Indian", "Italian", "Cafe"]}
})
 
// 15. Find restaurants not located in: Hyderabad, Bangalore
db.restaurants.find({
  city: { $nin: ["Hyderabad", "Bangalore"]}
})

// LIKE Equivalent / Regex
// 16. Find restaurants whose name starts with P.
db.restaurants.find({
  name: /^P/
})

// 17. Find restaurants whose name contains Point.
db.restaurants.find({
  name: /Point/
})

// 18. Find restaurants whose cuisine contains Food.
db.restaurants.find({
  cuisine: /Food/
})

// NULL Handling
// 19. Find restaurants where contact phone is null.
db.restaurants.find({
  "contact.phone": null
})

// 20. Find restaurants where contact email is null.
db.restaurants.find({
  "contact.email": null
})

// 21. Find restaurants where either phone or email is null.
db.restaurants.find({
  $or: [
    {"contact.phone": null},
    {"contact.email": null}
  ]
})

// Arrays
// 22. Find restaurants having tag premium
db.restaurants.find({
  tags: "premium"
})

// 23. Find restaurants having tag fast food
db.restaurants.find({
  tags: "fast food"
})

// 24. Find restaurants having both tags: north indian, premium 
db.restaurants.find({
  tags: {
    $all:["north indian", 'premium']
  }
})

// Sorting and Limit
// 25. Sort restaurants by rating descending.
db.restaurants.find().sort({rating: -1})

// 26. Display top 3 highest rated restaurants.
db.restaurants.find().sort({rating: -1}).limit(3)

// 27. Sort restaurants by average order value ascending.
db.restaurants.find().sort({avg_order_value: 1})

// 28. Display top 2 expensive restaurants by average order value.
db.restaurants.find().sort({avg_order_value: -1}).limit(2)


// Update Operations
// 29. Update Burger Street rating to 4.0.
db.restaurants.updateOne(
  {name: "Burger Street"},
  {$set: {rating: 4.0}}                       
)

// 30. Change Tea Tales delivery availability to true.
db.restaurants.updateOne(
  {name: "Tea Tales"},
  {$set: {delivery_available: true}}                       
)

// 31. Add a new field to all restaurants: active: true 
db.restaurants.updateMany(
  {},
  {$set: {active: true}}
)

// 32. Add a new tag popular to Spice Hub.
db.restaurants.updateOne(
  {name: "Spice Hub"},
  {$push: {tags: "popular"}}                       
)

// 33. Remove the field active from all restaurants.
db.restaurants.updateMany(
  {},
  {$unset: {active: ""}}
)

// Delete Operations
// 34. Delete the restaurant whose restaurant_id is 6.
db.restaurants.deleteOne(
  {restaurant_id: 6}
)

// 35. Delete all restaurants where rating is less than 4.0
 db.restaurants.deleteMany(
  {rating: {$lt: 4.0}}
)

// Count and Distinct
// 36. Count total restaurants.
db.restaurants.countDocuments()

// 37. Count restaurants where delivery is available.
db.restaurants.countDocuments({
  delivery_available: true
})

// 38. Display distinct cities.
db.restaurants.distinct("city")

// 39. Display distinct cuisines.
db.restaurants.distinct("cuisine")

// Aggregation
// 40. Count restaurants by city.
db.restaurants.aggregate([
  {
    $group: {
      _id: "city",
      total_restaurants: {$sum: 1}
    }
  }
])

// 41. Count restaurants by cuisine.
db.restaurants.aggregate([
  {
    $group: {
      _id: "cuisine",
      total_restaurants: {$sum: 1}
    }
  }
])

// 42. Find average rating by cuisine.
db.restaurants.aggregate([
  {
    $group: {
      _id: "$cuisine",
      average_rating: {$avg: '$rating'}
    }
  }
])

// 43. Find average order value by city.
db.restaurants.aggregate([
  {
    $group: {
      _id: "$city",
      average_order_value: {$avg: '$avg_order_value'}
    }
  }
])

// 44. Find highest average order value by cuisine.
db.restaurants.aggregate([
  {
    $group: {
      _id: "$city",
      average_order_value: {$avg: '$avg_order_value'}
    }
  },
  {
    $sort: {avg_order_value: -1}
  },
  {
    $limit: 1
  }
])

// 45. Show cuisines having more than one restaurant.
db.restaurants.aggregate([
  {
    $group: {
      _id: "$cuisine",
      restaurant_count: {$sum: 1}
    }
  },
  {
    $match: {
      restaurant_count: {$gt: 1}
    }
  }
])
