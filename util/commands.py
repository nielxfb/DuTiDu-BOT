from controllers.schedule import handle_schedule
from controllers.shift import handle_shift
from controllers.help import handle_help

commands = [
    {
        "aliases": ["/jadwal", "/schedule"],
        "handler": handle_schedule
    },
    {
        "aliases": ["/shift", "/sh"],
        "handler": handle_shift
    },
    {
        "aliases": ["/help"],
        "handler": handle_help
    }
]