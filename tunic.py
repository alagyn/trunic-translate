from typing import List, Dict

import imgui as im

from window_boilerplate import window_mainloop
from glyphs import Word, Glyph, GLYPH_TOTAL_Y, GLYPH_TOTAL_X, GLYPH_X, Cons, Vowel, CONS_EXAMPLES, VOW_EXAMPLES
from word_db import WordDB

EDITOR_SCALE = 0.5

TABLE_FLAGS = im.TableFlags.Borders | im.TableFlags.NoHostExtendX | im.TableFlags.SizingStretchSame

SELECT_HIGHLIGHT = im.ColorConvertFloat4ToU32(im.Vec4(0.2, 0.2, 0.2, 1.0))
BTN_HIGHLIGHT = im.ColorConvertFloat4ToU32(im.Vec4(0.3, 0.3, 0.3, 1.0))


def glyphButton(btnID: str,
                g: Glyph,
                dl: im.ImDrawList,
                wordLine: bool,
                scale: float,
                highlight: bool,
                pad: float = 0) -> bool:
    buttonSize = im.Vec2(pad + GLYPH_TOTAL_X * scale,
                         pad + GLYPH_TOTAL_Y * scale)
    pos = im.GetCursorScreenPos()
    out = im.InvisibleButton(btnID, buttonSize)
    if highlight:
        dl.AddRectFilled(pos,
                         im.Vec2(pos.x + buttonSize.x, pos.y + buttonSize.y),
                         SELECT_HIGHLIGHT, 0)
    if im.IsItemHovered():
        dl.AddRectFilled(pos,
                         im.Vec2(pos.x + buttonSize.x, pos.y + buttonSize.y),
                         BTN_HIGHLIGHT, 0)

    glyph_pos = im.Vec2(pos.x + pad / 2, pos.y + pad / 2)
    g.render(dl, glyph_pos, wordLine, scale)

    return out


class State:

    def __init__(self) -> None:
        self.wordLine = im.BoolRef(True)
        self.words: List[Word] = []

        self.words.append(Word(Glyph()))

        self.selectedWordIdx = 0
        self.selectedGlyphIdx = 0
        self.wordDB = WordDB()

    def render(self) -> bool:

        if im.Begin("Input"):
            im.CheckBox("Word Line", self.wordLine)

            wl = im.GetWindowDrawList()

            # These indices should never be invalid, error if they are
            selectedWord = self.words[self.selectedWordIdx]
            selectedGlyph = selectedWord.glyphs[self.selectedGlyphIdx]

            im.Text("Consonants")
            if im.BeginTable("Letter_Table", 12, TABLE_FLAGS):
                for con in Cons:
                    im.TableNextColumn()
                    im.Text(con.name)
                    try:
                        example = CONS_EXAMPLES[con]
                    except KeyError:
                        example = ""
                    im.BeginDisabled()
                    im.Text(example)
                    im.EndDisabled()
                    hl = selectedGlyph.cons == con
                    if glyphButton(f"add{con.name}", Glyph(con), wl,
                                   self.wordLine.val, EDITOR_SCALE, hl, 10):
                        selectedGlyph.cons = con
                        selectedGlyph.invalidate()
                        self.wordDB.getWord(selectedWord)

                im.EndTable()

            im.Dummy(im.Vec2(0, 10))
            im.Text("Vowels")
            # same ID so settings are shared
            if im.BeginTable("Letter_Table", 12, TABLE_FLAGS):
                for vow in Vowel:
                    im.TableNextColumn()
                    im.Text(vow.name)
                    im.BeginDisabled()
                    im.Text(VOW_EXAMPLES[vow])
                    im.EndDisabled()
                    hl = selectedGlyph.vowel == vow
                    if glyphButton(f"add{vow.name}", Glyph(None, vow), wl,
                                   self.wordLine.val, EDITOR_SCALE, hl, 10):
                        selectedGlyph.vowel = vow
                        selectedGlyph.invalidate()
                        self.wordDB.getWord(selectedWord)

                im.TableNextColumn()
                im.Text("Dot")
                if glyphButton(f"addDot", Glyph(None, None,
                                                True), wl, self.wordLine.val,
                               EDITOR_SCALE, selectedGlyph.dot, 10):
                    selectedGlyph.dot = not selectedGlyph.dot
                    selectedGlyph.invalidate()
                    self.wordDB.getWord(selectedWord)
                im.EndTable()

        im.End()

        text = []

        if im.Begin("Data"):
            dl = im.GetWindowDrawList()
            wPos = im.GetWindowPos()
            wSize = im.GetWindowSize()
            yScroll = im.GetScrollY()
            pos = im.Vec2(wPos.x + 10, wPos.y + 25 - yScroll)

            for wIdx, word in enumerate(self.words):
                if pos.x + len(word.glyphs) * GLYPH_TOTAL_X > wPos.x + wSize.x:
                    pos.x = wPos.x + 10
                    pos.y += GLYPH_TOTAL_Y + 10
                    text.append("\n")
                if len(word.value) == 0:
                    text.append(word.getSoundStr())
                else:
                    text.append(word.value.copy())
                for gIdx, g in enumerate(word.glyphs):
                    im.SetCursorScreenPos(pos)
                    selected = wIdx == self.selectedWordIdx and gIdx == self.selectedGlyphIdx
                    if glyphButton(f"select{wIdx},{gIdx}", g, dl,
                                   self.wordLine.val, 1.0, selected):

                        self.selectedWordIdx = wIdx
                        self.selectedGlyphIdx = gIdx
                    pos.x += GLYPH_TOTAL_X

                pos.x += GLYPH_X

        im.End()

        preventInput = False

        if im.Begin("Translation"):
            if im.InputText("Trans", selectedWord.value):
                self.wordDB.storeWord(selectedWord)
            if im.IsItemFocused():
                preventInput = True
            im.Text(" ".join(text))
        im.End()

        if not preventInput:
            if im.IsKeyPressed(im.ImKey.Space):
                selectedWord.glyphs.insert(self.selectedGlyphIdx + 1, Glyph())
                self.wordDB.getWord(selectedWord)
                self.selectedGlyphIdx += 1
            elif im.IsKeyPressed(im.ImKey.Backspace):
                if len(selectedWord.glyphs) > 1:
                    selectedWord.glyphs.pop(self.selectedGlyphIdx)
                    if self.selectedGlyphIdx > 0:
                        self.selectedGlyphIdx -= 1
                        self.wordDB.getWord(selectedWord)
                elif len(self.words) > 1:
                    self.words.pop(self.selectedWordIdx)
                    if self.selectedWordIdx > 0:
                        self.selectedWordIdx -= 1
                        self.selectedGlyphIdx = len(
                            self.words[self.selectedWordIdx].glyphs) - 1
                else:
                    g = self.words[0].glyphs[0]
                    g.cons = None
                    g.vowel = None
                    g.dot = False
                    self.words[0].value.set("")
                    g.invalidate()

            elif im.IsKeyPressed(im.ImKey.Enter):
                self.words.insert(self.selectedWordIdx + 1, Word(Glyph()))
                self.selectedWordIdx += 1
                self.selectedGlyphIdx = 0
            elif im.IsKeyPressed(im.ImKey.RightArrow):
                if self.selectedGlyphIdx + 1 < len(
                        self.words[self.selectedWordIdx].glyphs):
                    self.selectedGlyphIdx += 1
                elif self.selectedWordIdx + 1 < len(self.words):
                    self.selectedWordIdx += 1
                    self.selectedGlyphIdx = 0
            elif im.IsKeyPressed(im.ImKey.LeftArrow):
                if self.selectedGlyphIdx - 1 >= 0:
                    self.selectedGlyphIdx -= 1
                elif self.selectedWordIdx - 1 >= 0:
                    self.selectedWordIdx -= 1
                    self.selectedGlyphIdx = len(
                        self.words[self.selectedWordIdx].glyphs) - 1
        return False


def main():
    s = State()
    window_mainloop("Trunic Translate", s.render)


if __name__ == '__main__':
    main()
