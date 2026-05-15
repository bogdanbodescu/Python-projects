from datetime import datetime, date

from flask import Flask, flash, make_response, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from werkzeug.wrappers import Response


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///spendwise.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "my_secret_key"

db = SQLAlchemy(app)

CATEGORIES: list[str] = [
    "Food",
    "Transport",
    "Rent",
    "Entertainment",
    "Utilities",
    "Other",
]


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, default=date.today)


with app.app_context():
    db.create_all()


def parse_date_or_none(date_string: str) -> date | None:
    """Convert a YYYY-MM-DD string to a date object, or return None if invalid."""
    if not date_string:
        return None

    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return None


@app.route("/")
def index() -> str:
    """Render the dashboard with filtered expenses, totals and chart data."""
    start_str: str = request.args.get("start_date", "").strip()
    end_str: str = request.args.get("end_date", "").strip()
    selected_category: str = request.args.get("category", "").strip()

    start_date: date | None = parse_date_or_none(start_str)
    end_date: date | None = parse_date_or_none(end_str)

    if start_str and not start_date:
        flash("Invalid start date format. Please use YYYY-MM-DD.", "error")

    if end_str and not end_date:
        flash("Invalid end date format. Please use YYYY-MM-DD.", "error")

    if start_date and end_date and start_date > end_date:
        flash("Start date cannot be after end date.", "error")
        start_date = None
        end_date = None
        start_str = ""
        end_str = ""

    query = Expense.query

    if start_date:
        query = query.filter(Expense.date >= start_date)

    if end_date:
        query = query.filter(Expense.date <= end_date)

    if selected_category and selected_category in CATEGORIES:
        query = query.filter(Expense.category == selected_category)

    all_expenses: list[Expense] = query.order_by(
        Expense.date.desc(),
        Expense.id.desc()
    ).all()

    total_amount: float = sum(expense.amount for expense in all_expenses)

    category_query = db.session.query(
        Expense.category,
        func.sum(Expense.amount)
    )

    if start_date:
        category_query = category_query.filter(Expense.date >= start_date)

    if end_date:
        category_query = category_query.filter(Expense.date <= end_date)

    if selected_category and selected_category in CATEGORIES:
        category_query = category_query.filter(Expense.category == selected_category)

    category_rows = category_query.group_by(Expense.category).all()

    category_labels: list[str] = [
        category for category, total in category_rows
    ]

    category_values: list[float] = [
        round(float(total or 0), 2) for category, total in category_rows
    ]

    daily_query = db.session.query(
        Expense.date,
        func.sum(Expense.amount)
    )

    if start_date:
        daily_query = daily_query.filter(Expense.date >= start_date)

    if end_date:
        daily_query = daily_query.filter(Expense.date <= end_date)

    if selected_category and selected_category in CATEGORIES:
        daily_query = daily_query.filter(Expense.category == selected_category)

    daily_rows = daily_query.group_by(Expense.date).order_by(Expense.date).all()

    daily_labels: list[str] = [
        day.isoformat() for day, total in daily_rows
    ]

    daily_values: list[float] = [
        round(float(total or 0), 2) for day, total in daily_rows
    ]

    return render_template(
        "index.html",
        categories=CATEGORIES,
        today=date.today().isoformat(),
        all_expenses=all_expenses,
        total_amount=total_amount,
        start_str=start_str,
        end_str=end_str,
        selected_category=selected_category,
        category_labels=category_labels,
        category_values=category_values,
        daily_labels=daily_labels,
        daily_values=daily_values,
    )


@app.route("/add_expense", methods=["POST"])
def add_expense() -> Response:
    """Create a new expense after validating form data."""
    description: str = (request.form["description"] or "").strip()
    amount_str: str = (request.form["amount"] or "").strip()
    category: str = (request.form["category"] or "").strip()
    expense_date: str = (request.form["date"] or "").strip()

    if not description or not amount_str or not category or not expense_date:
        flash("All fields are required! Please fill in all fields.", "error")
        return redirect(url_for("index"))

    if category not in CATEGORIES:
        flash("Invalid category selected.", "error")
        return redirect(url_for("index"))

    try:
        amount: float = float(amount_str)

        if amount <= 0:
            flash("Amount must be a positive number.", "error")
            return redirect(url_for("index"))

    except ValueError:
        flash("Invalid amount. Please enter a valid positive number.", "error")
        return redirect(url_for("index"))

    date_parsed: date | None = parse_date_or_none(expense_date)

    if not date_parsed:
        flash("Invalid date format. Please use YYYY-MM-DD.", "error")
        return redirect(url_for("index"))

    expense = Expense(
        description=description,
        amount=amount,
        category=category,
        date=date_parsed,
    )

    db.session.add(expense)
    db.session.commit()

    flash("Expense added successfully!", "success")
    return redirect(url_for("index"))


@app.route("/delete_expense/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id: int) -> Response:
    """Delete an existing expense by ID."""
    expense: Expense = Expense.query.get_or_404(expense_id)

    db.session.delete(expense)
    db.session.commit()

    flash("Expense deleted successfully!", "success")
    return redirect(url_for("index"))


@app.route("/export_csv")
def export_csv() -> Response:
    """Export filtered expenses as a CSV file."""
    start_date: date | None = parse_date_or_none(
        request.args.get("start_date", "").strip()
    )
    end_date: date | None = parse_date_or_none(
        request.args.get("end_date", "").strip()
    )
    selected_category: str = request.args.get("category", "").strip()

    query = Expense.query

    if start_date:
        query = query.filter(Expense.date >= start_date)

    if end_date:
        query = query.filter(Expense.date <= end_date)

    if selected_category and selected_category in CATEGORIES:
        query = query.filter(Expense.category == selected_category)

    expenses: list[Expense] = query.order_by(
        Expense.date.desc(),
        Expense.id.desc()
    ).all()

    lines: list[str] = ["Description,Amount,Category,Date\n"]

    for expense in expenses:
        lines.append(
            f'"{expense.description}",'
            f"{expense.amount},"
            f'"{expense.category}",'
            f"{expense.date.isoformat()}\n"
        )

    csv_data: str = "".join(lines)

    response = make_response(csv_data)
    response.headers["Content-Disposition"] = "attachment; filename=expenses.csv"
    response.headers["Content-Type"] = "text/csv"

    return response


@app.route("/edit/<int:expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id: int) -> str | Response:
    """Edit an existing expense."""
    expense: Expense = Expense.query.get_or_404(expense_id)

    if request.method == "POST":
        description: str = (request.form["description"] or "").strip()
        amount_str: str = (request.form["amount"] or "").strip()
        category: str = (request.form["category"] or "").strip()
        expense_date: str = (request.form["date"] or "").strip()

        if not description or not amount_str or not category or not expense_date:
            flash("All fields are required!", "error")
            return redirect(url_for("edit_expense", expense_id=expense.id))

        try:
            amount: float = float(amount_str)

            if amount <= 0:
                flash("Amount must be positive.", "error")
                return redirect(url_for("edit_expense", expense_id=expense.id))

        except ValueError:
            flash("Invalid amount.", "error")
            return redirect(url_for("edit_expense", expense_id=expense.id))

        date_parsed: date | None = parse_date_or_none(expense_date)

        if not date_parsed:
            flash("Invalid date.", "error")
            return redirect(url_for("edit_expense", expense_id=expense.id))

        if category not in CATEGORIES:
            flash("Invalid category selected.", "error")
            return redirect(url_for("edit_expense", expense_id=expense.id))

        expense.description = description
        expense.amount = amount
        expense.category = category
        expense.date = date_parsed

        db.session.commit()

        flash("Expense updated successfully!", "success")
        return redirect(url_for("index"))

    return render_template(
        "edit.html",
        expense=expense,
        categories=CATEGORIES,
        today=date.today().isoformat(),
    )


if __name__ == "__main__":
    app.run(debug=True)