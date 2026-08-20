"""Formatting for optimizer output stored in Calibre job details."""

from .optimizer import _human


def summary_lines(payload):
    books = payload.get('books', [])
    total_orig = sum(b['orig_size'] for b in books)
    total_new = sum(b['new_size'] for b in books)
    total_imgs = sum(b['images'] for b in books)
    total_fixes = sum(b['fixes'] for b in books)
    total_err = sum(b['errors'] for b in books)
    saved = total_orig - total_new
    pct = (saved / float(total_orig) * 100.0) if total_orig else 0.0
    return [
        '',
        '------------------------------',
        'Done: %d book(s), %d image(s), %d fix(es)%s' % (
            len(books), total_imgs, total_fixes,
            ('   %d error(s)' % total_err) if total_err else ''),
        'Total size: %s -> %s  (%+.0f%%)' % (
            _human(total_orig), _human(total_new), -pct),
    ]
