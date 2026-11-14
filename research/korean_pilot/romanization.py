"""Yale-style spelling transliteration, preserving morphemes and source text.

Not phonetic transcription: do not apply liaison, neutralisation or assimilation.
The conventional Yale omission of w in /wu/ after labial onsets is applied.
"""
import re
import unicodedata

ONSETS = ('k', 'kk', 'n', 't', 'tt', 'l', 'm', 'p', 'pp', 's', 'ss', '', 'c', 'cc', 'ch', 'kh', 'th', 'ph', 'h')
VOWELS = ('a', 'ay', 'ya', 'yay', 'e', 'ey', 'ye', 'yey', 'o', 'wa', 'way', 'oy', 'yo', 'wu', 'we', 'wey', 'wi', 'yu', 'u', 'uy', 'i')
CODAS = ('', 'k', 'kk', 'ks', 'n', 'nc', 'nh', 't', 'l', 'lk', 'lm', 'lp', 'ls', 'lth', 'lph', 'lh', 'm', 'p', 'ps', 's', 'ss', 'ng', 'c', 'ch', 'kh', 'th', 'ph', 'h')
JAMO = dict(zip('ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ',
                ('k','kk','ks','n','nc','nh','t','tt','l','lk','lm','lp','ls','lth','lph','lh','m','p','pp','ps','s','ss','ng','c','cc','ch','kh','th','ph','h')))
JAMO.update(zip('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ', VOWELS))
HANGUL = re.compile(r'[가-힣ㄱ-ㅎㅏ-ㅣ]')
_TOKEN = r'[A-Za-z0-9_]*-?[가-힣ㄱ-ㅎㅏ-ㅣ]+(?:-[가-힣ㄱ-ㅎㅏ-ㅣ]+)*(?:-[A-Za-z0-9]+)?-?'
PHRASE = re.compile(_TOKEN + r'(?:[ \t]+' + _TOKEN + r')*')
LINK_TARGET = re.compile(r'(?<=\])\([^\n]*?\)')
INLINE_CODE = re.compile(r'(`+)(.*?)(\1)')


def romanize(text):
    result = []
    for c in unicodedata.normalize('NFC', text):
        if '가' <= c <= '힣':
            idx = ord(c) - 0xAC00
            onset, rem = divmod(idx, 21 * 28)
            vowel, coda = divmod(rem, 28)
            v = VOWELS[vowel]
            if vowel == 13 and onset in (6, 7, 8, 17):
                v = 'u'
            result.append(ONSETS[onset] + v + CODAS[coda])
        else:
            result.append(JAMO.get(c, c))
    return ''.join(result)


def annotate_plain(text):
    return PHRASE.sub(lambda m: m[0] + '（' + romanize(m[0]) + '）', text)


def annotate_inline(text):
    """Keep inline code intact; put the reading after its closing backtick."""
    chunks, pos = [], 0
    for m in INLINE_CODE.finditer(text):
        chunks.append(annotate_plain(text[pos:m.start()]))
        chunks.append(m[0])
        if HANGUL.search(m[2]):
            chunks.append('（' + romanize(m[2]) + '）')
        pos = m.end()
    chunks.append(annotate_plain(text[pos:]))
    return ''.join(chunks)


def annotate_markdown(text):
    """Annotate prose and labels, preserving link destinations and code blocks.

    Code blocks must have a separate romanisation row supplied by their writer.
    Use on an unannotated source; it intentionally does not guess whether existing
    author romanisations are equivalents.
    """
    result, fenced = [], False
    for line in text.splitlines(keepends=True):
        if line.startswith('```'):
            fenced = not fenced
            result.append(line)
            continue
        if fenced:
            result.append(line)
            continue
        parts, pos = [], 0
        for m in LINK_TARGET.finditer(line):
            parts.extend((annotate_inline(line[pos:m.start()]), m[0]))
            pos = m.end()
        parts.append(annotate_inline(line[pos:]))
        result.append(''.join(parts))
    return ''.join(result)


def display_width(text):
    return sum(2 if unicodedata.east_asian_width(c) in ('W', 'F') else 1 for c in text)


def aligned_rows(rows):
    tokens = [row.split() for row in rows]
    assert len({len(row) for row in tokens}) == 1
    widths = [max(display_width(word) for word in col) + 2 for col in zip(*tokens)]
    return '\n'.join(''.join(word + ' ' * (width - display_width(word))
                             for word, width in zip(row, widths)).rstrip()
                     for row in tokens)
