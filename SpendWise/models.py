from datetime import date

from extensions import db


class Expense(db.Model):
    """
    Database model representing a single expense entry.

    Attributes:
        id: Unique identifier for the expense.
        description: Short description of the expense.
        amount: Expense amount.
        category: Expense category.
        date: Date when the expense occurred.
    """

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, default=date.today)