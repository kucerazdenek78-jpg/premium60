#!/usr/bin/env python3
"""Vyrenderuje reel PREMIUM 60 (1080×1920, 30 fps) z tools/reel/reel.html.
Použití: python3 tools/reel/reel.py VYSTUP.mp4 [--frames t1,t2,...]  (--frames = jen kontrolní snímky JPEG)"""
import sys, subprocess, pathlib, os
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
FPS = 30

def page_html():
    html = (HERE / 'reel.html').read_text(encoding='utf-8')
    svg = (ROOT / 'tools' / 'mapa-kraju.svg').read_text(encoding='utf-8')
    out = HERE / '_reel_build.html'
    out.write_text(html.replace('<!--MAPA-->', svg), encoding='utf-8')
    return out

def main():
    out = pathlib.Path(sys.argv[1]).resolve()
    frames = None
    if '--frames' in sys.argv:
        frames = [float(x) for x in sys.argv[sys.argv.index('--frames') + 1].split(',')]
    build = page_html()
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1920})
        pg.goto(build.as_uri(), wait_until='load')
        pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(300)
        if frames:
            for t in frames:
                pg.evaluate(f'render({t})')
                pg.screenshot(path=str(out.parent / f'{out.stem}-{t:05.2f}.jpg'), type='jpeg', quality=92)
            b.close(); return
        dur = pg.evaluate('window.DURATION')
        # po 4 s kusech (jeden soubor na kus), pak spojit bez překódování
        parts = []; n = int(round(dur * FPS)); chunk = 4 * FPS
        for ci, start in enumerate(range(0, n, chunk)):
            tmp = out.parent / f'_part{ci:02d}.tmp.mp4'; fin = out.parent / f'_part{ci:02d}.mp4'
            ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                                   '-c:v', 'libx264', '-crf', '18', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', str(FPS), str(tmp)], stdin=subprocess.PIPE)
            for f in range(start, min(start + chunk, n)):
                pg.evaluate(f'render({f / FPS})')
                ff.stdin.write(pg.screenshot(type='jpeg', quality=92))
            ff.stdin.close()
            if ff.wait() != 0: raise SystemExit('ffmpeg selhal')
            tmp.rename(fin); parts.append(fin); print('kus', ci, 'hotovo', flush=True)
        b.close()
    lst = out.parent / '_parts.txt'
    lst.write_text(''.join(f"file '{p}'\n" for p in parts))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', '-movflags', '+faststart', str(out)], check=True)
    for p in parts: p.unlink()
    lst.unlink(); build.unlink()
    print('Hotovo:', out)

if __name__ == '__main__':
    main()
