from typing import Optional, Union, Iterable

def send_mail(to: Union[str, Iterable[str]], subject: str, message: str, bcc: Optional[Union[str, Iterable[str]]]) -> None:
    """Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`."""
    pass