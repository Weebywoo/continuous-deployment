import datetime
from contextlib import contextmanager
from enum import Enum


class LogType(Enum):
    INFO: str = "INFO"
    WARNING: str = "WARNING"
    ERROR: str = "ERROR"
    TASK_DONE: str = "TASK DONE"
    IN_PROGRESS: str = "IN PROGRESS"


_log_type_colors: dict[str, str] = {
    "INFO": "\033[38;2;0;255;0m",
    "WARNING": "\033[38;2;255;255;0m",
    "ERROR": "\033[38;2;255;0;0m",
    "DONE": "\033[38;2;0;255;0m",
    "IN_PROGRESS": "\033[38;2;128;0;128m",
}

reset: str = "\033[m"
cyan: str = "\033[38;2;0;255;255m"


def get_color(log_type: LogType) -> str:
    return _log_type_colors[log_type.name]


def timestamp():
    return datetime.datetime.now().strftime(format="%d-%m-%Y %H:%M:%S")


def log(log_type: LogType, message: str, end: str = None):
    timestamp_str: str = timestamp()
    log_type_buffer: int = len(max(LogType, key=lambda lt: len(lt.name)).name)
    color: str = get_color(log_type)

    if end is None:
        print(
            f"[{cyan + timestamp_str + reset}] [{color + log_type.value.ljust(log_type_buffer) + reset}] {message}",
            flush=True,
        )

    if end is not None:
        print(
            f"[{cyan + timestamp_str + reset}] [{(color + log_type.name.ljust(log_type_buffer) + reset)}] {message}",
            end=end,
            flush=True,
        )


@contextmanager
def progress(log_type: LogType, start: str, stop: str) -> None:
    log(log_type, start, end=" ")

    try:
        yield

    finally:
        print(stop)
