from controllers.schedule import handle_schedule
from controllers.shift import handle_shift
from controllers.help import handle_help
from controllers.rang import handle_rang

commands = [
    {"aliases": ["/jadwal", "/schedule"], "handler": handle_schedule},
    {"aliases": ["/shift", "/sh"], "handler": handle_shift},
    {"aliases": ["/help"], "handler": handle_help},
    {"aliases": ["rang", "Rang"], "handler": handle_rang},
]

