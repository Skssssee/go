from TEAMZYRO import *
import importlib
from TEAMZYRO.modules import ALL_MODULES


async def send_start_message(application):
    try:
        await application.bot.send_message(
            chat_id=START_CHAT_ID,
            text="🤖 Bot Started Successfully!"
        )
    except Exception as e:
        LOGGER("TEAMZYRO").warning(f"Startup message failed: {e}")


async def post_init(application):
    await ZYRO.start()
    await send_start_message(application)


def main() -> None:

    for module_name in ALL_MODULES:
        importlib.import_module("TEAMZYRO.modules." + module_name)

    LOGGER("TEAMZYRO.modules").info(
        "𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳..."
    )

    application.post_init = post_init

    application.run_polling(
        drop_pending_updates=True,
        close_loop=False
    )

    LOGGER("TEAMZYRO").info(
        "╔═════ஜ۩۞۩ஜ════╗\n"
        "  ☠︎︎MADE BY GOJOXNETWORK☠︎︎\n"
        "╚═════ஜ۩۞۩ஜ════╝"
    )


if __name__ == "__main__":
    main()
