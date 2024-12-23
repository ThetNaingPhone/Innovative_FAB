from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.crud_operations import create_record, read_records, update_record, delete_record

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace '*' with specific origins for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/create/")
def api_create_record(record: dict, company_name: str):
    """
    Create a new record with a specified company name.
    """
    record_id = create_record(record, company_name)
    return {"message": "Record created successfully!", "id": record_id}

@app.get("/read/")
def api_read_records(company_name: str):
    """
    Read records filtered by company name.
    """
    records = read_records(company_name)
    if not records:
        raise HTTPException(status_code=404, detail="No records found")
    return {"data": records}

@app.put("/update/{year}")
def api_update_record(year: str, updates: dict):
    """
    Update a record by year with provided updates.
    """
    updated_count = update_record(year, updates)
    if updated_count == 0:
        raise HTTPException(status_code=404, detail="Record not found or no changes made")
    return {"message": f"{updated_count} record(s) updated successfully"}

@app.delete("/delete/{year}")
def api_delete_record(year: str):
    """
    Delete a record by year.
    """
    deleted_count = delete_record(year)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"message": f"{deleted_count} record(s) deleted successfully"}
