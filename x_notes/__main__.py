from loguru import logger

from .helpers import load_notes, save_metadata, save_notes
from .notes import get_notes
from .statuses import add_statuses

if __name__ == "__main__":
    logger.info("Fetching notes ...")
    notes = load_notes()
    notes = get_notes(notes)

    logger.info("Fetching statuses ...")
    notes = add_statuses(notes)

    logger.info("Sorting ...")
    notes = dict(sorted(notes.items(), key=lambda x: x[1]["created_at"], reverse=True))

    logger.info("Saving ...")
    save_notes(notes)
    save_metadata(notes)

    logger.info("Done.")
