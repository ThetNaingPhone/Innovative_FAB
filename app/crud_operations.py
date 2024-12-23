from app.database import get_database

db = get_database()
collection = db["sales_data"]

current_id = 1

def get_next_id():
    global current_id
    next_id = current_id
    current_id += 1
    return next_id

def create_record(record, company_name):
    try:
        record_id = get_next_id()
        record["id"] = record_id
        record["company_name"] = company_name
        result = collection.insert_one(record)
        return record_id
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to insert record: " + str(e))

def read_records(company_name=None):
    query = {}
    if company_name:
        query["company_name"] = company_name
    return list(collection.find(query, {"_id": 0}))  # Exclude MongoDB's default _id field

def update_record(year, updates):
    result = collection.update_one({"Year": year}, {"$set": updates})
    return result.modified_count

def delete_record(year):
    result = collection.delete_one({"Year": year})
    return result.deleted_count
