# お茶会告知（11月12日）｜画像生成プロンプト

## 使い方
1. ChatGPT（画像生成）／Gemini／Midjourney などに、下の「英語プロンプト」をそのまま貼る
   - 英語のほうが指示の通りがよいため英語にしています（日本語訳は下に記載）
2. 縦長 4:5 を指定（Midjourney なら末尾の `--ar 4:5` がそのまま効きます）
3. できた写真を `overlay.html` で開き、「お茶会」と日付を入れて保存

---

## 英語プロンプト（コピー用）

```
A candid, real-life smartphone photo of a freshly brewed cup of black coffee with gentle, wispy steam rising from it, on a warm wooden table by a window. Shot from a 45-degree high angle, slightly off-center but the coffee cup is the main subject in the middle of the frame.

The cup: a plain white ceramic mug, or a simple handmade-looking cup and saucer with a slightly uneven rim and tiny glaze imperfections. Next to it, one or two homemade baked sweets (a plain financier and a small butter cookie) on a small rustic plate, casually placed, not arranged perfectly.

Table: warm honey-colored wood with natural, irregular grain and small marks of use. A softly wrinkled natural linen cloth in cream, partly covering the table. One small accent of muted terracotta orange only (for example a folded terracotta linen napkin corner), nothing else in that color. A small sprig of soft green leaves or a little potted herb slightly out of focus in the background.

Light: bright natural daylight from a side window around midday, soft shadows, airy and cheerful mood, the feeling that something fun is about to begin.

Color palette: cream, caramel, soft sage green, with a single terracotta accent.

Composition for text space: keep the top 20% of the frame calm and simple (softly blurred window light and plain wall), and keep the bottom 25% of the frame almost empty — just plain cream linen and wood with no objects — so text can be added later.

Style: looks like an unedited photo taken with a phone camera, natural color, slight film-like grain, realistic depth of field, small natural imperfections. Not symmetrical, not too perfect.

Do NOT include: any text, letters, logos or numbers; people, hands or faces; scattered coffee beans; latte art or heart shapes; cinnamon sticks; glossy or shiny surfaces; glow, bloom, sparkles, bokeh particles, light leaks, rainbow fringes; gradient backgrounds; neon; 3D render or CGI look; plastic-smooth textures.

Vertical 4:5 aspect ratio, 1080x1350.
```

Midjourney の場合は末尾に次を追加：
```
--ar 4:5 --style raw --no text, letters, hands, people, coffee beans, latte art, cinnamon, glow, sparkles, neon, gradient, 3d render
```

---

## 日本語訳（確認用）

- スマホで撮ったような自然な写真。窓辺の木のテーブルに、湯気が立つ淹れたての珈琲
- 斜め上45度から。珈琲が画面の中心。ただし少しだけ中心をずらす
- 白いマグ、または手作り風のカップ＆ソーサー（縁に少し不揃い）
- 焼き菓子は1〜2個（フィナンシェ、小さなバタークッキー）。きっちり並べない
- 温かい木目のテーブル＋クリーム色のリネン（少しシワあり）
- 差し色は**テラコッタ（くすんだオレンジ）1色だけ**。ナプキンの端などに少し
- 奥にやわらかい緑（小さな葉やハーブ）をぼかして
- 昼の窓からの自然光。明るく、これから楽しいことが始まる空気
- **上20%**：ぼけた窓の光と壁だけ（「お茶会」を入れる場所）
- **下25%**：リネンと木だけで物を置かない（時間・場所・申込を入れる場所）
- 入れないもの：文字・ロゴ・数字／人の手や顔／コーヒー豆／ラテアート／シナモン／光沢・グロー・きらきら・虹色のにじみ／グラデ背景／ネオン／3D風

---

## うまくいかないときの追加指示（そのまま送ればOK）

| 出てきた問題 | 追加で送る一文 |
|---|---|
| 下に物が置かれて余白がない | `Move everything up. Leave the bottom quarter of the image completely empty linen.` |
| つるっとしてAIっぽい | `Make it look more like a casual phone snapshot: less polished, natural grain, slightly imperfect.` |
| 文字のようなものが入る | `Remove all text, letters and numbers from the image.` |
| 差し色が増えた | `Use terracotta only on the napkin. Everything else cream, caramel and soft green.` |
| 湯気が太すぎる・CGっぽい | `Make the steam faint, thin and irregular, like real steam in daylight.` |
