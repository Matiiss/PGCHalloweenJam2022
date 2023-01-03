import enum


class EntityState(enum.Enum):
    IDLE = enum.auto()  # NOQA
    WALK = enum.auto()  # NOQA
    RUN = enum.auto()  # NOQA
    JUMP = enum.auto()  # NOQA
