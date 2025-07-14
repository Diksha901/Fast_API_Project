
##  Setup Instructions
1. Clone the repo
2. Create virtual environment & activate :
     * run : python -m venv .<Your_Virtual_Environment_Name>
     * to activate : .<Your_Virtual_Environment_Name>\Scripts\activate
4. Run: `pip install -r requirements.txt`
5. Set DB URL in `.env`
6. Run migrations if needed
7. Start: `uvicorn app.main:app --reload`

##  APIs Implemented
1. `/api/forms/bogie-checksheet` , POST request , submits the details of bogie through form number to the table created in the database 
2. `/api/forms/wheel-specification`,POST rerquest, submits the details of wheels to the table in database
3. `/api/forms/wheel-specification`,GET rerquest, fetches the details of wheels from the table in database using query on form number

##  Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

##  Features
- Follows Swagger spec
- Request/Response validation
- Modular code structure
