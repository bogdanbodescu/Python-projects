from datetime import datetime, date

from sqlalchemy import func

from extensions import db
from models import Expense


CATEGORIES: list[str] = [
    "Food",
    "Transport",
    "Rent",
    "Entertainment",
    "Utilities",
    "Other",
]


def parse_date_or_none(date_string: str) -> date | None:
    """
    Convert a string in YYYY-MM-DD format into a date object.

    Args:
        date_string: Date string provided by the user.

    Returns:
        A date object if parsing succeeds, otherwise None.
    """
    if not date_string:
        return None

    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return None


def build_filtered_query(
    start_date: date | None,
    end_date: date | None,
    selected_category: str,
):
    """
    Build a filtered SQLAlchemy query based on date range and category.

    Args:
        start_date: Optional start date filter.
        end_date: Optional end date filter.
        selected_category: Optional category filter.

    Returns:
        Filtered Expense query.
    """
    query = Expense.query

    if start_date:
        query = query.filter(Expense.date >= start_date)

    if end_date:
        query = query.filter(Expense.date <= end_date)

    if selected_category and selected_category in CATEGORIES:
        query = query.filter(Expense.category == selected_category)

    return query


def get_expenses_total(expenses: list[Expense]) -> float:
    """
    Calculate the total amount for a list of expenses.

    Args:
        expenses: List of Expense objects.

    Returns:
        Total expense amount.
    """
    return sum(expense.amount for expense in expenses)


def get_category_chart_data(
    start_date: date | None,
    end_date: date | None,
    selected_category: str,
) -> tuple[list[str], list[float]]:
    """
    Calculate total expenses grouped by category.

    Args:
        start_date: Optional start date filter.
        end_date: Optional end date filter.
        selected_category: Optional category filter.

    Returns:
        A tuple containing category labels and category values.
    """
    category_query = db.session.query(
        Expense.category,
        func.sum(Expense.amount),
    )

    if start_date:
        category_query = category_query.filter(Expense.date >= start_date)

    if end_date:
        category_query = category_query.filter(Expense.date <= end_date)

    if selected_category and selected_category in CATEGORIES:
        category_query = category_query.filter(
            Expense.category == selected_category
        )

    category_rows = category_query.group_by(Expense.category).all()

    category_labels: list[str] = [
        category for category, total in category_rows
    ]

    category_values: list[float] = [
        round(float(total or 0), 2)
        for category, total in category_rows
    ]

    return category_labels, category_values


def get_daily_chart_data(
    start_date: date | None,
    end_date: date | None,
    selected_category: str,
) -> tuple[list[str], list[float]]:
    """
    Calculate total expenses grouped by date.

    Args:
        start_date: Optional start date filter.
        end_date: Optional end date filter.
        selected_category: Optional category filter.

    Returns:
        A tuple containing daily labels and daily values.
    """
    daily_query = db.session.query(
        Expense.date,
        func.sum(Expense.amount),
    )

    if start_date:
        daily_query = daily_query.filter(Expense.date >= start_date)

    if end_date:
        daily_query = daily_query.filter(Expense.date <= end_date)

    if selected_category and selected_category in CATEGORIES:
        daily_query = daily_query.filter(Expense.category == selected_category)

    daily_rows = daily_query.group_by(
        Expense.date
    ).order_by(
        Expense.date
    ).all()

    daily_labels: list[str] = [
        day.isoformat()
        for day, total in daily_rows
    ]

    daily_values: list[float] = [
        round(float(total or 0), 2)
        for day, total in daily_rows
    ]

    return daily_labels, daily_values