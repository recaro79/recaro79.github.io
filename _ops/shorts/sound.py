# 쇼츠 배경음 (직접 합성한 원곡 — 저작권 문제 없음) + 장면 전환·강조 효과음
import json, sys, wave, random
import numpy as np

SR = 44100
OD = sys.argv[2] if len(sys.argv) > 2 else "out"
tm = json.load(open(OD + "/timing.json"))
TOTAL = tm["total"]; STARTS = tm["starts"]
# 강조 효과음 시각(장면 번호, 장면 안 초)
ACCENTS = [(2, 1.8), (4, 2.0), (6, 2.1), (7, 0.3)]
if len(sys.argv) > 1:
    ACCENTS = json.loads(sys.argv[1])

n = int(SR * (TOTAL + 0.5)); out = np.zeros(n)
def note(f, t0, dur, amp, decay=6.0, harm=(1, .5, .25)):
    i0 = int(t0 * SR); m = min(int(dur * SR), n - i0)
    if m <= 0: return
    t = np.arange(m) / SR
    w = sum(a * np.sin(2 * np.pi * f * (k + 1) * t) for k, a in enumerate(harm))
    env = np.exp(-decay * t) * np.minimum(1, t * 200)
    out[i0:i0 + m] += amp * w * env

hz = lambda midi: 440 * 2 ** ((midi - 69) / 12)
# C - G - Am - F (밝고 가벼운 진행), 100bpm
prog = [[60, 64, 67], [55, 59, 62], [57, 60, 64], [53, 57, 60]]
shift = int(sys.argv[3]) if len(sys.argv) > 3 else 0
prog = [[x + shift for x in c] for c in prog]
beat = 0.6; bar = beat * 4; t = 0.0; k = 0
while t < TOTAL:
    ch = prog[k % 4]
    note(hz(ch[0] - 24), t, bar, .22, decay=1.5, harm=(1, .3))            # 베이스
    pat = [0, 1, 2, 1, 2, 1, 0, 2]
    for j, p in enumerate(pat):                                         # 8분음 아르페지오
        note(hz(ch[p] + 12), t + j * beat / 2, .5, .10, decay=7)
    for j in (1, 3):                                                    # 가벼운 박자감(클랩 대용)
        i0 = int((t + j * beat) * SR); m = min(int(.05 * SR), n - i0)
        if m > 0: out[i0:i0 + m] += .05 * np.random.randn(m) * np.exp(-np.arange(m) / SR * 80)
    t += bar; k += 1
# 장면 전환 '휙'
for s in STARTS[1:]:
    i0 = int((s - .12) * SR); m = int(.25 * SR)
    noise = np.random.randn(m); env = np.sin(np.linspace(0, np.pi, m)) ** 2
    out[i0:i0 + m] += .10 * np.convolve(noise, np.ones(30) / 30, "same") * env * 3
# 강조 '띵'
for sc, dt in ACCENTS:
    t0 = STARTS[sc - 1] + dt
    note(hz(84), t0, .6, .16, decay=5, harm=(1, .4)); note(hz(91), t0 + .07, .6, .12, decay=5, harm=(1, .3))
# 끝부분 페이드아웃
fade = int(1.2 * SR); out[n - fade:] *= np.linspace(1, 0, fade)
out = out / np.max(np.abs(out)) * 0.5
w = wave.open(OD + "/bgm.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()
print("bgm ok")
