// Database Creation
use supply_chain_db;
switched to db supply_chain_db

// Collection Creation
db.createCollection("shipment_logs")
{ ok: 1 }

db.shipment_logs.insertMany([
  {
    "shipment_id": "SH-101",
    "order_id": 1,
    "carrier": "DHL Express",
    "status": "Delivered",
    "origin": "Taipei, TW",
    "destination": "San Jose, US",
    "timestamps": { "shipped_at": ISODate("2026-06-01T10:00:00Z"), "delivered_at": ISODate("2026-06-05T14:20:00Z") }
  },
  {
    "shipment_id": "SH-102",
    "order_id": 2,
    "carrier": "FedEx",
    "status": "In Transit",
    "origin": "Austin, US",
    "destination": "Chicago, US",
    "timestamps": { "shipped_at": ISODate("2026-06-18T08:15:00Z"), "estimated_delivery": ISODate("2026-06-23T17:00:00Z") }
  },
  {
    "shipment_id": "SH-103",
    "order_id": 3,
    "carrier": "UPS",
    "status": "Delayed",
    "origin": "Frankfurt, DE",
    "destination": "Dublin, IE",
    "timestamps": { "shipped_at": ISODate("2026-06-15T12:00:00Z"), "estimated_delivery": ISODate("2026-06-22T12:00:00Z") }
  },
  {
    "shipment_id": "SH-104",
    "order_id": 4,
    "carrier": "DHL Express",
    "status": "Processing",
    "origin": "Tokyo, JP",
    "destination": "London, UK",
    "timestamps": { "shipped_at": null, "estimated_delivery": ISODate("2026-06-28T18:00:00Z") }
  },
  {
    "shipment_id": "SH-105",
    "order_id": 5,
    "carrier": "Maersk Cargo",
    "status": "Delivered",
    "origin": "Le Havre, FR",
    "destination": "Rotterdam, NL",
    "timestamps": { "shipped_at": ISODate("2026-06-10T06:00:00Z"), "delivered_at": ISODate("2026-06-14T09:45:00Z") }
  }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6a37e3ca85497216e3ea5e37'),
    '1': ObjectId('6a37e3ca85497216e3ea5e38'),
    '2': ObjectId('6a37e3ca85497216e3ea5e39'),
    '3': ObjectId('6a37e3ca85497216e3ea5e3a'),
    '4': ObjectId('6a37e3ca85497216e3ea5e3b')
  }
}

db.shipment_logs.find()
{
  _id: ObjectId('6a37e3ca85497216e3ea5e37'),
  shipment_id: 'SH-101',
  order_id: 1,
  carrier: 'DHL Express',
  status: 'Delivered',
  origin: 'Taipei, TW',
  destination: 'San Jose, US',
  timestamps: {
    shipped_at: 2026-06-01T10:00:00.000Z,
    delivered_at: 2026-06-05T14:20:00.000Z
  }
}
{
  _id: ObjectId('6a37e3ca85497216e3ea5e38'),
  shipment_id: 'SH-102',
  order_id: 2,
  carrier: 'FedEx',
  status: 'In Transit',
  origin: 'Austin, US',
  destination: 'Chicago, US',
  timestamps: {
    shipped_at: 2026-06-18T08:15:00.000Z,
    estimated_delivery: 2026-06-23T17:00:00.000Z
  }
}
{
  _id: ObjectId('6a37e3ca85497216e3ea5e39'),
  shipment_id: 'SH-103',
  order_id: 3,
  carrier: 'UPS',
  status: 'Delayed',
  origin: 'Frankfurt, DE',
  destination: 'Dublin, IE',
  timestamps: {
    shipped_at: 2026-06-15T12:00:00.000Z,
    estimated_delivery: 2026-06-22T12:00:00.000Z
  }
}
{
  _id: ObjectId('6a37e3ca85497216e3ea5e3a'),
  shipment_id: 'SH-104',
  order_id: 4,
  carrier: 'DHL Express',
  status: 'Processing',
  origin: 'Tokyo, JP',
  destination: 'London, UK',
  timestamps: {
    shipped_at: null,
    estimated_delivery: 2026-06-28T18:00:00.000Z
  }
}
{
  _id: ObjectId('6a37e3ca85497216e3ea5e3b'),
  shipment_id: 'SH-105',
  order_id: 5,
  carrier: 'Maersk Cargo',
  status: 'Delivered',
  origin: 'Le Havre, FR',
  destination: 'Rotterdam, NL',
  timestamps: {
    shipped_at: 2026-06-10T06:00:00.000Z,
    delivered_at: 2026-06-14T09:45:00.000Z
  }
}

// Creating indexes
db.shipment_logs.createIndex({"status": 1});
status_1

db.shipment_logs.createIndex({"carrier": 1, "shipment_id": 1});
carrier_1_shipment_id_1

db.shipment_logs.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { status: 1 }, name: 'status_1' },
  {
    v: 2,
    key: { carrier: 1, shipment_id: 1 },
    name: 'carrier_1_shipment_id_1'
  }
]