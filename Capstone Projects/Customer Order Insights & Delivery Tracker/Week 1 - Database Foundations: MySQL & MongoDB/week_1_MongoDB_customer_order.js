// Database Creation 
use customer_insights_db;
switched to db customer_insights_db

// Collection Creation
db.createCollection("customer_feedback")
{ ok: 1 }

db.customer_feedback.insertMany([
  {
    "feedback_id": "FB-001", 
    "customer_id": 1001, 
    "customer_name": "Alice Smith",
    "rating": 5, 
    "comments": "Super fast shipment of my wireless headphones! Packaging was perfectly intact and setup was plug-and-play.",
    "tags": ["fast_delivery", "satisfied"]
  },
  {
    "feedback_id": "FB-002", 
    "customer_id": 1002, 
    "customer_name": "Bob Jones",
    "rating": 2, 
    "comments": "The ergonomic chair took forever to arrive. It sat at the localized sorting facility hub for 5 days without any tracking updates.",
    "incident_reported": true,
    "routing_logs": ["Hub A", "Hub B", "Delayed at Sorting Facility"]
  },
  {
    "feedback_id": "FB-003", 
    "customer_id": 1004, 
    "customer_name": "Diana Prince",
    "rating": 1, 
    "comments": "The delivery box came completely crushed. The 4K monitor display panel glass was shattered on arrival. Need a replacement immediately.",
    "support_ticket_created": true,
    "damage_type": "Shattered Screen"
  },
  {
    "feedback_id": "FB-004", 
    "customer_id": 1005, 
    "customer_name": "Evan Wright",
    "rating": 3, 
    "comments": "The USB-C hub functions as expected, but the carrier left the package out in the heavy rain without placing it under the porch cover."
  }
])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a3d2acccc0098a07be2ce1d'),
    '1': ObjectId('6a3d2acccc0098a07be2ce1e'),
    '2': ObjectId('6a3d2acccc0098a07be2ce1f'),
    '3': ObjectId('6a3d2acccc0098a07be2ce20')
  }
}

// Creating indexes
db.customer_feedback.createIndex({"customer_id": 1})
customer_id_1

db.customer_feedback.getIndexes()
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { customer_id: 1 }, name: 'customer_id_1' }
]

db.customer_feedback.find({"customer_id":1002})
{
  _id: ObjectId('6a3d2acccc0098a07be2ce1e'),
  feedback_id: 'FB-002',
  customer_id: 1002,
  customer_name: 'Bob Jones',
  rating: 2,
  comments: 'The ergonomic chair took forever to arrive. It sat at the localized sorting facility hub for 5 days without any tracking updates.',
  incident_reported: true,
  routing_logs: [
    'Hub A',
    'Hub B',
    'Delayed at Sorting Facility'
  ]
}