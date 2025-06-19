#!/usr/bin/env python3

from app import app
from models import db, User

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        User.query.delete()
        
        print("Seeding users...")
        
        # Create sample users
        user1 = User(username="johndoe", email="john@example.com")
        user1.password_hash = "password123"
        
        user2 = User(username="janedoe", email="jane@example.com")
        user2.password_hash = "password123"
        
        db.session.add_all([user1, user2])
        db.session.commit()
        
        print("Database seeded successfully!")