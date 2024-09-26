# Laboratory Work 1: Task Management System

This project is a Task Management System implemented using FastAPI, SQLModel, and PostgreSQL.

## Project Structure

- `main.py`: The main application file that sets up the FastAPI app and includes all the routers.
- `database.py`: Handles database connection and session management.
- `schemas.py`: Defines SQLModel schemas for the database tables.
- `routers/`: Directory containing router files for different endpoints:
  - `auth_router.py`: Handles authentication-related endpoints.
  - `participant_router.py`: Manages participant-related operations.
  - `team_member_router.py`: Handles team member operations.
  - `team_router.py`: Manages team-related operations.
  - `task_router.py`: Handles task-related operations.
  - `submission_router.py`: Manages submission-related operations.
- `.env`: Contains environment variables, including the database URL.
- `alembic.ini`: Configuration file for Alembic, used for database migrations.

## Setup

1. Ensure you have Python 3.7+ installed.
2. Install the required dependencies (you may want to use a virtual environment):
   ```
   pip install fastapi sqlmodel psycopg2-binary python-dotenv uvicorn alembic
   ```
3. Set up your PostgreSQL database and update the `.env` file with your database URL.
4. Run database migrations:
   ```
   alembic upgrade head
   ```
5. Start the application:
   ```
   uvicorn main:app --reload
   ```

## API Endpoints

The API provides the following main endpoints:

- `/auth`: Authentication endpoints
- `/participants`: Participant management
- `/team_members`: Team member management
- `/teams`: Team management
- `/tasks`: Task management
- `/submissions`: Submission management

For detailed API documentation, run the server and visit `http://localhost:8000/docs`.

## Database Schema

The main entities in the system are:

- Participant
- Team
- TeamMember (association between Participant and Team)
- Task
- Submission (association between Task and Team)

Refer to `schemas.py` for detailed model definitions.
