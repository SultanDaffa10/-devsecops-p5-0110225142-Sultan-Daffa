def validate_title(title: str) -> str:
    if not isinstance(title, str):
        raise TypeError("Title must be a string.")

    cleaned_title = title.strip()

    if not cleaned_title:
        raise ValueError("Title cannot be empty.")

    if len(cleaned_title) > 100:
        raise ValueError("Title cannot exceed 100 characters.")

    return cleaned_title