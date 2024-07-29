Overview
This project provides a system to offer real-time flight status updates and notifications to passengers. The system includes a frontend built with React.js and a backend powered by Flask. It integrates with MongoDB and PostgreSQL databases and utilizes Firebase Cloud Messaging for notifications.

Features
Real-time Updates: Display current flight status (delays, cancellations, gate changes).
Push Notifications: Send notifications for flight status changes via SMS, email, or app notifications using Firebase Cloud Messaging.
Integration with Airport Systems: Pull data from airport databases for accurate information.

Technologies Used

Frontend:
HTML
CSS
React.js

Backend:
Python
Flask

Database
MongoDB

Notifications
Firebase Cloud Messaging

Prerequisites
Node.js and npm (for frontend)
Python 3.x (for backend)
MongoDB
PostGResql
Firebase account for Cloud Messaging

Frontend Setup

1. Navigate to the frontend directory:
   cd frontend
2. Install dependencies:
   Install dependencies:
3. Start the frontend development server:
   npm start

Backend Setup

1. Navigate to the backend directory:
   cd backend
2. Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate
3. Install dependencies:
