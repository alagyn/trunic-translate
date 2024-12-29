import os
import sqlite3

from glyphs import Word, wordFromStr

SCHEMA = """
CREATE TABLE IF NOT EXISTS words
(
    sounds UNIQUE NOT NULL, 
    value NOT NULL
)
"""

GET_WORD = "SELECT value FROM words WHERE sounds = ?"
STORE_WORD = "INSERT INTO words VALUES (:sounds, :value) ON CONFLICT DO UPDATE SET value = :value"
REM_WORD = "DELETE FROM words WHERE sounds = ?"
LOOKUP_WORD = "SELECT sounds FROM words WHERE value = ?"


class WordDB:

    def __init__(self) -> None:
        self.con = sqlite3.connect(
            os.path.join(os.path.dirname(__file__), "words.db"))
        self.cur = self.con.cursor()
        #self.con.set_trace_callback(print)

        self.cur.execute(SCHEMA)

    def storeWord(self, word: Word):
        if len(word.value) == 0:
            self.cur.execute(REM_WORD, (word.getSoundStr(), ))
        else:
            soundStr = word.getSoundStr()
            value = word.value.copy()
            self.cur.execute(STORE_WORD, {"sounds": soundStr, "value": value})

        self.con.commit()

    def getWord(self, word: Word):
        soundStr = word.getSoundStr()
        res = self.cur.execute(GET_WORD, (soundStr, ))
        value = res.fetchone()
        if value is not None:
            word.value.set(value[0])
        else:
            word.value.set("")

    def lookupWord(self, text: str) -> Word | None:
        res = self.cur.execute(LOOKUP_WORD, (text, ))
        value = res.fetchone()
        if value is None:
            return None

        word = wordFromStr(value[0])
        word.value.set(text)

        return word
