"""Lists related humanization."""

from __future__ import annotations

from typing import Iterable, Sequence

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

__all__ = ["natural_list"]


def natural_list(
    items: Sequence[Any] | Iterable[Any],
    conjunction: str = "and",
) -> str:
    """Natural list.

    Convert a list of items into a human-readable string with commas and a
    final conjunction (default ``"and"``).  Pass ``"or"`` (or any other
    word) to change the final separator:

    Examples:
        >>> natural_list(["one", "two", "three"])
        'one, two and three'
        >>> natural_list(["one", "two", "three"], conjunction="or")
        'one, two or three'
        >>> natural_list(["one", "two"])
        'one and two'
        >>> natural_list(["one"])
        'one'

    Args:
        items: An iterable of items.
        conjunction: Word to use between the penultimate and last item.
            Defaults to ``"and"``; pass ``"or"`` to produce a disjunction
            list like ``"a, b or c"``.

    Returns:
        A string with commas and the chosen conjunction in the right
        places.  Returns an empty string for an empty input.
    """
    items_list = list(items)
    if not items_list:
        return ""
    if len(items_list) == 1:
        return str(items_list[0])
    if len(items_list) == 2:
        return f"{items_list[0]} {conjunction} {items_list[1]}"
    return ", ".join(str(item) for item in items_list[:-1]) + f" {conjunction} {items_list[-1]}"
