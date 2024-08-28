def check_is_spaceheat_name(v: str) -> None:
    """Check SpaceheatName Format. Used in data_classes.utls"""
    try:
        x = v.split("-")
    except Exception as e:
        raise ValueError(f"Failed to seperate <{v}> into words with split'-'") from e
    first_word = x[0]
    first_char = first_word[0]
    if not first_char.isalpha():
        raise ValueError(
            f"Most significant word of <{v}> must start with alphabet char."
        )
    for word in x:
        if not word.isalnum():
            raise ValueError(f"words of <{v}> split by by '-' must be alphanumeric.")
    if not v.islower():
        raise ValueError(f"All characters of <{v}> must be lowercase.")
