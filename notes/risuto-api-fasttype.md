# リザストAPI：ファストタイプの入れ方（2026-10-17 確かめた）

キーはクラウドの会話で自動で付く。キーの中身はここに書かない。
リクエストは1秒以上あける（あけないと rate_limited）。

| やること | 送り方 | 確認 |
|---|---|---|
| 一覧 | GET `/api/fast_types` | 動いた |
| 1件の中身 | GET `/api/fast_type_detail?fast_type_id=ID` | 動いた |
| 新しく作る | POST `/api/create_fast_type`（title） | 動いた。状態は `prepare`（公開前） |
| 設定を変える | POST `/api/update_fast_type`（fast_type_id, description=LPのHTML, header_image_url など） | 動いた |
| タイプを作る | POST `/api/create_fast_type_result`（fast_type_id, name, header_message=見出し, message=回答メール文, i_order） | 動いた |
| タイプを直す | POST `/api/update_fast_type_result`（fast_type_result_id ＋直す項目） | 動いた |
| 質問を作る | POST `/api/create_fast_type_question`（fast_type_id, question, answers） | 動いた |
| 画像を上げる | POST `/api/upload_image`（multipart の file） | 動いた。返ってきた url を header_image_url に入れる |

| ステップメール一覧 | GET `/api/step_mails` | 動いた（id・title・subscribers_count だけ） |
| ステップメールを作る | POST `/api/create_step_mail`（title） | 動いた。**作った時点で public（公開）・reception（受付中）になる**。中身のメールは付かない（articles を送っても無視された） |

- ステップメールの中身（1通ずつのメール）を入れる窓口は、見つからなかった（2026-10-17）
  - step_mail_detail / create_step_mail_article など十数通り試して、すべて404
  - `create_mail_magazine_article` にステップメールの番号を入れると「件名と本文がない」とだけ返る。ただ、「登録の何日後か」を決める項目がないため、試していない
- answers の形：`[{"answer_text": "選択肢", "scores": {"タイプのID": 点数}}]`
  - scores を配列で送ると、エラー（500）になる
- 公開・削除はしない（リザストは下書きまで、の決まり）

## 今回入れたもの
- 221番「学んできたのに、なぜ口コミが広がらない？ お客様の「ひとこと」でわかる5つのタイプ診断」（公開前）
  - タイプ5つ（ID 1011〜1015）、質問8問、LP（`fasttype-lp-v1.html`）、バナーB
  - 配信グループは、作ったときに自動で 127648「クチコミで人気教室運営・セラピストになれるメール講座」が入っていた
- ステップメール 371128「口コミタイプ診断フォロー」：入れ物だけ。中身は空。公開・受付中になっている。ファストタイプにはまだつないでいない
- 216番「あ」、217番「２」は、美智代さんが10/16に試しに作った枠。触っていない
