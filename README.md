# galactic-industry-architect
Eve Online industry planner for personal, corp, alliance, and bloc operations.

# Plan

Creating a containerized Python application that utilizes the EVE Online ESI API to pull information into a local database for industry planning involves several steps. Here's a high-level overview:

1. **Set Up the Development Environment**:
   - Install Python and relevant libraries like `requests` for API interaction, `sqlalchemy` for database management, and `docker` for containerization.
   - Set up a local development environment that includes a text editor or an IDE.

2. **Obtain API Access**:
   - Register an application with EVE Online to get API credentials (Client ID and Secret Key).
   - Implement OAuth 2.0 authentication to access the ESI API securely.

3. **Design Database Schema**:
   - Define the database schema to store data like materials, stations, PI progress, and manufacturing details.
   - Use an SQL database like PostgreSQL or MySQL.

4. **Develop Data Retrieval Logic**:
   - Write Python scripts to interact with the ESI API and retrieve the necessary data.
   - Handle data parsing, transformation, and storage in your local database.

5. **Implement Industry Planning Features**:
   - Develop logic for calculating material requirements, station targeting, and tracking PI and manufacturing progress.
   - Create functions to analyze and output this data in a user-friendly format.

6. **Containerize the Application**:
   - Write a Dockerfile to define the container environment.
   - Use Docker to build and run your application in an isolated container.

7. **User Interface Development** (Optional):
   - Consider developing a web interface or a command-line interface for easier interaction with your application.

8. **Testing and Iteration**:
   - Test the application for functionality, performance, and security.
   - Iteratively improve based on feedback and new requirements.

9. **Documentation and Deployment**:
   - Document the setup and usage instructions.
   - Deploy the application as per your requirement (locally, on a server, etc.).

This project requires a good understanding of Python programming, EVE Online's ESI API, database management, and containerization principles. Each step should be carefully planned and executed for the successful development of the application.

# Database Schema
Designing a database schema for your EVE Online industry planning application involves considering the types of data you'll be handling and how they interrelate. Here's a high-level design:

1. **Users Table**: Stores user information.
   - Fields: UserID (Primary Key), Username, Email, etc.

2. **Blueprints Table**: Stores blueprint details.
   - Fields: BlueprintID (Primary Key), Name, TypeID, MaterialEfficiency, TimeEfficiency, etc.

3. **Materials Table**: Contains details about different materials.
   - Fields: MaterialID (Primary Key), Name, Volume, etc.

4. **BlueprintMaterials Table**: Links blueprints to the materials required.
   - Fields: BlueprintID (Foreign Key), MaterialID (Foreign Key), Quantity, etc.

5. **Stations Table**: Information about different stations.
   - Fields: StationID (Primary Key), Name, Location, etc.

6. **MiningActivities Table**: Tracks mining activities.
   - Fields: ActivityID (Primary Key), UserID (Foreign Key), AsteroidType, StartTime, EndTime, QuantityMined, etc.

7. **IndustryJobs Table**: For tracking manufacturing, reactions, research.
   - Fields: JobID (Primary Key), BlueprintID (Foreign Key), StationID (Foreign Key), StartTime, EndTime, Status, etc.

8. **PlanetaryInteraction Table**: Details about planetary infrastructure projects.
   - Fields: ProjectID (Primary Key), UserID (Foreign Key), PlanetType, Structure, StartTime, EndTime, ProductionRate, etc.

Each table should have appropriate indexes for performance optimization, especially on foreign keys. The schema should be normalized to reduce data redundancy. As your application grows, you might need to add more tables or modify existing ones to accommodate additional features.