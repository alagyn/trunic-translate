import enum
from typing import List, Dict

import imgui as im


class GlyphParts(enum.IntEnum):
    # vowel
    V1 = enum.auto()  # top left
    V2 = enum.auto()  # top right
    V3 = enum.auto()  # middle
    V4 = enum.auto()  # bottom left
    V5 = enum.auto()  # bottom right

    # consonant
    C1 = enum.auto()  # top left
    C2 = enum.auto()  # top mid
    C3 = enum.auto()  # top right
    C4 = enum.auto()  # middle
    C5 = enum.auto()  # bottom left
    C6 = enum.auto()  # bottom mid
    C7 = enum.auto()  # bottom right

    DOT = enum.auto()


class Cons(enum.IntEnum):
    B = enum.auto()
    P = enum.auto()

    D = enum.auto()
    T = enum.auto()

    F = enum.auto()
    V = enum.auto()

    K = enum.auto()

    G = enum.auto()  # (g)ate
    J = enum.auto()  # (j)udge
    CH = enum.auto()  # (ch)ange

    S = enum.auto()
    Z = enum.auto()

    H = enum.auto()
    R = enum.auto()
    Y = enum.auto()

    M = enum.auto()
    N = enum.auto()
    W = enum.auto()

    NG = enum.auto()

    SH = enum.auto()  # (sh)ield
    ZH = enum.auto()  # u(s)ually

    TH_SOFT = enum.auto()  # no(th)ing
    TH_HARD = enum.auto()  # (th)is

    L = enum.auto()

    def getParts(self) -> List[GlyphParts]:
        match self:
            case Cons.B:
                return [GlyphParts.C2, GlyphParts.C4, GlyphParts.C7]
            case Cons.P:
                return [GlyphParts.C3, GlyphParts.C4, GlyphParts.C6]
            case Cons.D:
                return [
                    GlyphParts.C2, GlyphParts.C4, GlyphParts.C5, GlyphParts.C7
                ]
            case Cons.T:
                return [
                    GlyphParts.C1, GlyphParts.C3, GlyphParts.C4, GlyphParts.C6
                ]
            case Cons.F:
                return [
                    GlyphParts.C3, GlyphParts.C4, GlyphParts.C5, GlyphParts.C6
                ]
            case Cons.V:
                return [
                    GlyphParts.C1, GlyphParts.C2, GlyphParts.C4, GlyphParts.C7
                ]
            case Cons.K:
                return [
                    GlyphParts.C2, GlyphParts.C3, GlyphParts.C4, GlyphParts.C7
                ]
            case Cons.G:
                return [
                    GlyphParts.C3, GlyphParts.C4, GlyphParts.C6, GlyphParts.C7
                ]
            case Cons.J:
                return [GlyphParts.C2, GlyphParts.C4, GlyphParts.C5]
            case Cons.CH:
                return [GlyphParts.C1, GlyphParts.C4, GlyphParts.C6]
            case Cons.S:
                return [
                    GlyphParts.C2, GlyphParts.C3, GlyphParts.C4, GlyphParts.C5,
                    GlyphParts.C6
                ]
            case Cons.Z:
                return [
                    GlyphParts.C1, GlyphParts.C2, GlyphParts.C4, GlyphParts.C6,
                    GlyphParts.C7
                ]
            case Cons.H:
                return [
                    GlyphParts.C2, GlyphParts.C4, GlyphParts.C6, GlyphParts.C7
                ]
            case Cons.R:
                return [
                    GlyphParts.C2, GlyphParts.C3, GlyphParts.C4, GlyphParts.C6
                ]
            case Cons.Y:
                return [
                    GlyphParts.C1, GlyphParts.C2, GlyphParts.C4, GlyphParts.C6
                ]
            case Cons.M:
                return [GlyphParts.C5, GlyphParts.C7]
            case Cons.N:
                return [GlyphParts.C1, GlyphParts.C5, GlyphParts.C7]
            case Cons.W:
                return [GlyphParts.C1, GlyphParts.C3]
            case Cons.NG:
                return [
                    GlyphParts.C1, GlyphParts.C2, GlyphParts.C3, GlyphParts.C4,
                    GlyphParts.C5, GlyphParts.C6, GlyphParts.C7
                ]
            case Cons.SH:
                return [
                    GlyphParts.C1, GlyphParts.C3, GlyphParts.C4, GlyphParts.C5,
                    GlyphParts.C6, GlyphParts.C7
                ]
            case Cons.ZH:
                return [
                    GlyphParts.C1, GlyphParts.C2, GlyphParts.C3, GlyphParts.C4,
                    GlyphParts.C5, GlyphParts.C7
                ]
            case Cons.TH_SOFT:
                return [
                    GlyphParts.C1, GlyphParts.C2, GlyphParts.C3, GlyphParts.C4,
                    GlyphParts.C6
                ]
            case Cons.TH_HARD:
                return [
                    GlyphParts.C2, GlyphParts.C4, GlyphParts.C5, GlyphParts.C6,
                    GlyphParts.C7
                ]
            case Cons.L:
                return [GlyphParts.C2, GlyphParts.C4, GlyphParts.C6]


CONS_EXAMPLES: Dict[Cons, str] = {
    Cons.G: "(g)ate",
    Cons.J: "(j)udge",
    Cons.CH: "(ch)ange",
    Cons.SH: "(sh)ield",
    Cons.ZH: "u(s)ual",
    Cons.TH_SOFT: "no(th)ing",
    Cons.TH_HARD: "(th)is",
}


class Vowel(enum.IntEnum):
    AY = enum.auto()  # s(ay)
    AI = enum.auto()  # s(i)gn
    OI = enum.auto()  # t(oy)
    OU = enum.auto()  # f(ou)nd

    AA = enum.auto()  # h(a)s
    AH = enum.auto()  # f(o)x
    IH = enum.auto()  # h(i)t
    EH = enum.auto()  # pr(e)ss

    UU = enum.auto()  # sh(ou)ld
    UH = enum.auto()  # s(o)me

    EE = enum.auto()  # w(e)
    OO = enum.auto()  # y(ou)
    OH = enum.auto()  # th(ough)

    UR = enum.auto()  # dang(er)
    OR = enum.auto()  # y(our)
    AR = enum.auto()  # f(ar)
    IR = enum.auto()  # n(ear)
    ER = enum.auto()  # sc(are)

    def getParts(self) -> List[GlyphParts]:
        match self:
            case Vowel.AA:
                return [GlyphParts.V1, GlyphParts.V2, GlyphParts.V3]
            case Vowel.AH:
                return [GlyphParts.V1, GlyphParts.V3]
            case Vowel.IH:
                return [GlyphParts.V4, GlyphParts.V5]
            case Vowel.EH:
                return [GlyphParts.V3, GlyphParts.V4, GlyphParts.V5]
            case Vowel.UU:
                return [GlyphParts.V3, GlyphParts.V4]
            case Vowel.UH:
                return [GlyphParts.V1, GlyphParts.V2]
            case Vowel.EE:
                return [
                    GlyphParts.V1, GlyphParts.V3, GlyphParts.V4, GlyphParts.V5
                ]
            case Vowel.OO:
                return [
                    GlyphParts.V1, GlyphParts.V2, GlyphParts.V3, GlyphParts.V4
                ]
            case Vowel.UR:
                return [
                    GlyphParts.V2, GlyphParts.V3, GlyphParts.V4, GlyphParts.V5
                ]
            case Vowel.OR:
                return [
                    GlyphParts.V1, GlyphParts.V2, GlyphParts.V3, GlyphParts.V5
                ]
            case Vowel.AR:
                return [
                    GlyphParts.V1, GlyphParts.V2, GlyphParts.V4, GlyphParts.V5
                ]
            case Vowel.IR:
                return [GlyphParts.V1, GlyphParts.V3, GlyphParts.V5]
            case Vowel.AY:
                return [GlyphParts.V1]
            case Vowel.AI:
                return [GlyphParts.V2]
            case Vowel.OI:
                return [GlyphParts.V4]
            case Vowel.OU:
                return [GlyphParts.V5]
            case Vowel.OH:
                return [
                    GlyphParts.V1, GlyphParts.V2, GlyphParts.V3, GlyphParts.V4,
                    GlyphParts.V5
                ]
            case Vowel.ER:
                return [GlyphParts.V3, GlyphParts.V5]
            # Consonants

            case _:
                return []


VOW_EXAMPLES: Dict[Vowel, str] = {
    Vowel.AY: "s(ay)",
    Vowel.AI: "s(i)gn",
    Vowel.OI: "t(oy)",
    Vowel.OU: "f(ou)nd",
    Vowel.AA: "h(a)s",
    Vowel.AH: "f(o)x",
    Vowel.IH: "h(i)t",
    Vowel.EH: "pr(e)ss",
    Vowel.UU: "sh(ou)ld",
    Vowel.UH: "s(o)me",
    Vowel.EE: "w(e)",
    Vowel.OO: "y(ou)",
    Vowel.OH: "th(ough)",
    Vowel.UR: "dang(er)",
    Vowel.OR: "y(our)",
    Vowel.AR: "f(ar)",
    Vowel.IR: "n(ear)",
    Vowel.ER: "sc(are)",
}

GLYPH_OUTER_Y = 15
GLYPH_C_Y1 = 2 * GLYPH_OUTER_Y
GLYPH_C_Y2 = GLYPH_C_Y1 + (2 * GLYPH_OUTER_Y)

GLYPH_MID_Y = 4 * GLYPH_OUTER_Y

GLYPH_TOTAL_Y = (2 * GLYPH_OUTER_Y) + GLYPH_MID_Y
GLYPH_X = GLYPH_OUTER_Y * 2
GLYPH_TOTAL_X = GLYPH_X * 2

WORD_LINE_Y = GLYPH_TOTAL_Y / 2

GLYPH_COL = im.ColorConvertFloat4ToU32(im.Vec4(1.0, 1.0, 1.0, 1))
GLYPH_THICK = 3

GLYPH_DOT_RAD = 5


class Glyph:

    def __init__(self,
                 cons: Cons | None = None,
                 vowel: Vowel | None = None,
                 dot: bool = False) -> None:
        self.cons: Cons | None = cons
        self.vowel: Vowel | None = vowel
        self.dot = dot

        self._parts: List[GlyphParts] | None = None

    def invalidate(self):
        self._parts = None

    def render(self,
               dl: im.ImDrawList,
               pos: im.Vec2,
               wordline: bool,
               scale: float = 1.0):
        if self._parts is None:
            self._parts = []

            if self.cons is not None:
                self._parts.extend(self.cons.getParts())
            if self.vowel is not None:
                self._parts.extend(self.vowel.getParts())
            if self.dot:
                self._parts.append(GlyphParts.DOT)

        # precompute consonant vertices
        c1 = im.Vec2(pos.x + (GLYPH_X * scale), pos.y + (GLYPH_C_Y1 * scale))
        c2 = im.Vec2(c1.x, pos.y + (GLYPH_C_Y2 * scale))

        if wordline:
            w1 = im.Vec2(pos.x, pos.y + (WORD_LINE_Y * scale))
            w2 = im.Vec2(pos.x + GLYPH_TOTAL_X * scale, w1.y)
            dl.AddLine(w1, w2, GLYPH_COL, GLYPH_THICK * scale)

        for p in self._parts:
            match p:
            # Vowel parts
                case GlyphParts.V1:
                    v1 = im.Vec2(pos.x, pos.y + (GLYPH_OUTER_Y * scale))
                    v2 = im.Vec2(pos.x + (GLYPH_X * scale), pos.y)
                case GlyphParts.V2:
                    v1 = im.Vec2(pos.x + (GLYPH_X * scale), pos.y)
                    v2 = im.Vec2(v1.x + (GLYPH_X * scale),
                                 v1.y + (GLYPH_OUTER_Y * scale))
                case GlyphParts.V3:
                    v1 = im.Vec2(pos.x, pos.y + (GLYPH_OUTER_Y * scale))
                    v2 = im.Vec2(pos.x, v1.y + (GLYPH_MID_Y * scale))
                    if wordline:
                        v3 = im.Vec2(pos.x, pos.y + (WORD_LINE_Y * scale))

                        dl.AddLine(im.Vec2(pos.x, c2.y), v2, GLYPH_COL,
                                   GLYPH_THICK * scale)

                        v2 = v3

                case GlyphParts.V4:
                    v1 = im.Vec2(pos.x,
                                 pos.y + (GLYPH_OUTER_Y + GLYPH_MID_Y) * scale)
                    v2 = im.Vec2(pos.x + GLYPH_X * scale,
                                 v1.y + GLYPH_OUTER_Y * scale)
                case GlyphParts.V5:
                    v1 = im.Vec2(pos.x + GLYPH_X * scale,
                                 pos.y + GLYPH_TOTAL_Y * scale)
                    v2 = im.Vec2(v1.x + GLYPH_X * scale,
                                 v1.y - GLYPH_OUTER_Y * scale)
                # consonant parts
                case GlyphParts.C1:
                    v1 = im.Vec2(pos.x, pos.y + GLYPH_OUTER_Y * scale)
                    v2 = c1
                case GlyphParts.C2:
                    v1 = im.Vec2(pos.x + GLYPH_X * scale, pos.y)
                    v2 = c1
                case GlyphParts.C3:
                    v1 = c1
                    v2 = im.Vec2(v1.x + GLYPH_X * scale,
                                 pos.y + GLYPH_OUTER_Y * scale)
                case GlyphParts.C4:
                    v1 = c1
                    if wordline:
                        v2 = im.Vec2(v1.x, pos.y + WORD_LINE_Y * scale)
                    else:
                        v2 = c2
                case GlyphParts.C5:
                    v1 = c2
                    v2 = im.Vec2(pos.x,
                                 pos.y + (GLYPH_OUTER_Y + GLYPH_MID_Y) * scale)
                case GlyphParts.C6:
                    v1 = c2
                    v2 = im.Vec2(v1.x, pos.y + GLYPH_TOTAL_Y * scale)
                case GlyphParts.C7:
                    v1 = c2
                    v2 = im.Vec2(v1.x + GLYPH_X * scale,
                                 pos.y + (GLYPH_OUTER_Y + GLYPH_MID_Y) * scale)
                case GlyphParts.DOT:
                    v1 = im.Vec2(
                        pos.x + GLYPH_X * scale,
                        pos.y + (GLYPH_TOTAL_Y + GLYPH_DOT_RAD) * scale)
                    dl.AddCircle(v1,
                                 GLYPH_DOT_RAD * scale,
                                 GLYPH_COL,
                                 thickness=GLYPH_THICK * scale)
                    return

                case _:
                    pass

            dl.AddLine(v1, v2, GLYPH_COL, GLYPH_THICK * scale)

    def getSoundStr(self) -> str:
        out = []
        if self.dot:
            if self.vowel:
                out.append(self.vowel.name)
            if self.cons:
                out.append(self.cons.name)
        else:
            if self.cons:
                out.append(self.cons.name)
            if self.vowel:
                out.append(self.vowel.name)
        return "".join(out)


class Word:

    def __init__(self, *glyphs: Glyph) -> None:
        self.glyphs: List[Glyph] = list(glyphs)
        self.value = im.StrRef(50)

    def getSoundStr(self) -> str:
        out = []
        for g in self.glyphs:
            out.append(g.getSoundStr())

        return "|".join(out)
