import csv
from app import create_app, db
from app.models import Guest

app = create_app()

with app.app_context():
    from app.models import Guest  # ✅ moved inside the app context

    # Optional: Clear existing guests
    Guest.query.delete()

    # Load CSV data
    with open('guests.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            guest = Guest(name=row['name'], occupation=row['occupation'])
            db.session.add(guest)

    db.session.commit()
    print("🌱 Guests seeded successfully!")
