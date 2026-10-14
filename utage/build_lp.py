import json, sys
from urllib.parse import quote

# ===== Palette (feminine: blush pink / rose / champagne gold) =====
INK   = "#5B4A50"   # body text (warm mocha)
ROSE  = "#D46A82"   # main accent
ROSE_D= "#B8506A"
BLUSH = "#FBE9EC"
CREAM = "#FFF9F6"
GOLD  = "#C9A27E"
WHITE = "#FFFFFF"
CTA_URL = "https://example.com/apply"  # ←申込フォームURLに差し替え

CMAP={INK:None,ROSE:"r",ROSE_D:"rd",GOLD:"g",WHITE:"w"}
def _cls(align,color,weight=None):
    c=[]
    if align=="center": c.append("tc")
    k=CMAP.get(color,"")
    if k: c.append(k)
    if weight: c.append("b")
    return c
def P(html, size=None, align="center", color=INK, weight=None):
    c=_cls(align,color,weight)
    if color not in CMAP: html=f'<span style="color:{color};">{html}</span>'
    return f'<p class="{" ".join(c)}">{html}</p>' if c else f'<p>{html}</p>'

def lines(*ls, align="center", color=INK):
    return "".join(P(l,align=align,color=color) if l else '<p><br></p>' for l in ls)

def mark(t):  # pink highlighter
    return f'<span class="mk">{t}</span>'

def rose(t, b=True):
    return f'<span class="r b">{t}</span>'

def text(content, fs=16, fsm=15, lh="2.0", pb=3, **kw):
    d = {"type":"text","content":content,"font_size":fs,"font_size_mobile":fsm,"line_height":lh,"padding_bottom":pb}
    d.update(kw); return d

def head(content, fs=30, fsm=22, **kw):
    d = {"type":"head","content":content,"font_size":fs,"font_size_mobile":fsm,"line_height":"1.5"}
    d.update(kw); return d

def sub(content, fs=20, fsm=17, **kw):
    d = {"type":"subhead","content":content,"font_size":fs,"font_size_mobile":fsm,"line_height":"1.6","font_weight":"700"}
    d.update(kw); return d

def spacer(h=40, hm=None):
    return {"type":"spacer","height":h,"height_mobile":hm if hm is not None else int(h*0.7)}

def divider(color=GOLD, w=60):
    return {"type":"divider","border_color":color,"border_width":1,"width":w,"padding_top":2,"padding_bottom":2}

def label(en, ja):
    """小さな英字ラベル＋日本語見出し（セクションタイトル）"""
    return [
        text(f'<p style="text-align:center;"><span style="color:{GOLD};letter-spacing:0.25em;">{en}</span></p>', fs=13, fsm=12, lh="1.4", pb=0),
        head(f'<p style="text-align:center;"><span style="color:{ROSE_D};">{ja}</span></p>', fs=28, fsm=21),
        divider(),
    ]

def cta(main="無料体験セミナーに申し込む", sub_t="＼ 未経験・女性・自分のためでもOK ／", light=False):
    if light:
        d=cta(main, sub_t); d.update(background_color=WHITE, background_color_to="#FFF4F1", color=ROSE, sub_color=ROSE); return d
    return {"type":"button","content":main,"sub_content":sub_t,"link_type":"url","link_url":CTA_URL,
            "link_target":"same","cv_tracking":1,"button_color":"btn-red-pill",
            "background_color":"#E7849A","background_color_to":"#F2AE9E","gradient_degree":"90",
            "color":WHITE,"sub_color":WHITE,"font_size":22,"font_size_mobile":18,"sub_font_size":13,"sub_font_size_mobile":12,
            "icon_right":"fas fa-chevron-right","animation":"scale","width":90,"padding_y":20,"align":"center","padding_bottom":2}

def col(children, w=12, **kw):
    d = {"type":"col","col_width_1":w,"children":children}; d.update(kw); return d

def row(cols, width=760, **kw):
    d = {"type":"row","width":width,"children":cols}; d.update(kw); return d

def section(rows, bg=WHITE, bg_to=None, deg="180", name=None, mb=0):
    d = {"type":"section","background_color":bg,"margin_bottom":mb,"children":rows}
    if bg_to: d.update(background_color_to=bg_to, gradient_degree=deg)
    if name: d["element_name"]=name
    return d

def card(children, bg=WHITE, border=None, radius=20, ps=6, pt=6, pb=5, w=12):
    kw = dict(background_color=bg, border_radius=radius, padding_side=ps, padding_top=pt, padding_bottom=pb)
    if border: kw.update(border_width=1, border_color=border, border_style="solid")
    return col(children, w=w, **kw)

def ph(w, h, t, bg="F4D6DB", fg="B8506A"):
    return f"https://placehold.jp/24/{bg}/{fg}/{w}x{h}.png?text={quote(t)}"

E = []

# ---------- 1. HERO ----------
E.append(section([
    row([col([
        spacer(30, 20),
        text(f'<p style="text-align:center;"><span style="color:{WHITE};background-color:{ROSE};border-radius:999px;padding:6px 16px;font-weight:bold;">未経験OK！</span>　<span style="color:{WHITE};background-color:{ROSE};padding:6px 16px;font-weight:bold;">女性OK！</span>　<span style="color:{WHITE};background-color:{ROSE};padding:6px 16px;font-weight:bold;">自分のためでもOK！</span></p>', fs=15, fsm=12, lh="2.6", pb=4),
        sub(lines("起業、副業に最適な今話題の", f"<strong>AIを活用した{rose('コピーライター')}に</strong>", "なりませんか？"), fs=24, fsm=19),
        spacer(10, 6),
        text(P(f"たった{rose('７つのテンプレート')}で集客ページを完成させる"), fs=17, fsm=14, lh="1.6", pb=1),
        head(f'<p style="text-align:center;"><span style="color:{ROSE_D};">AI感情ライター</span><br><span style="color:{INK};">養成講座</span></p>', fs=48, fsm=34, shadow="1", shadow_color=WHITE),
        text(f'<p style="text-align:center;"><span style="color:{WHITE};background-color:{GOLD};padding:8px 28px;font-weight:bold;letter-spacing:0.15em;">１DAY 体験セミナー</span></p>', fs=22, fsm=18, lh="2.4", pb=5),
        cta(),
        spacer(30, 20),
    ])], width=760)
], bg="#FCE4E8", bg_to=CREAM, name="ファーストビュー"))

# ---------- 2. 問いかけ ----------
E.append(section([
    row([col([
        spacer(60, 40),
        head(lines(f"本当に{rose('あなたも')}", "ライターになれるのか？"), fs=30, fsm=22),
        text(P("体験セミナーで力試ししてみませんか？", color=INK), fs=18, fsm=16, pb=5),
    ])]),
    row([card([
        text(lines(f"AIがコピーライターという職業を", "なくすと言われていましたが、", f"{mark('それは間違いでした。')}"), fs=18, fsm=16),
    ], bg=BLUSH, radius=24)]),
    row([col([
        spacer(30, 20),
        {"type":"balloon","content":P("いつか起業したい", align="left"),"image_url":ph(200,200,"♡"),"image_position":"left","image_width":80,"image_width_mobile":60,"font_size":17,"font_size_mobile":15,"background_color":WHITE},
        {"type":"balloon","content":P("自分の力で稼ぐ仕事を探している", align="left"),"image_url":ph(200,200,"♡"),"image_position":"right","image_width":80,"image_width_mobile":60,"font_size":17,"font_size_mobile":15,"background_color":WHITE},
        spacer(10),
        text(lines(f"そんなあなたに{rose('朗報')}です。", "", "時間や場所に縛られず、", "自由に働ける職業、", f"{mark('コピーライター')}になってみませんか？"), fs=18, fsm=16),
        spacer(20),
        sub(P(f"「えっ、今さら文章を書く仕事？」", color=ROSE_D), fs=22, fsm=18),
        text(lines("と思ったかもしれません。", "", "ChatGPTやClaudeにお願いすれば、", "数秒で文章が完成する時代。", "", "むしろ、", "「コピーライターなんて、", "AIに真っ先に仕事を奪われるんじゃないの？」", "そう思うのが普通でしょう。"), fs=17, fsm=15),
        spacer(50, 30),
    ])]),
], bg=CREAM, name="問いかけ"))

# ---------- 3. アメリカで起きていること ----------
E.append(section([
    row([col([spacer(60, 40), *label("TURNING POINT", "ところが──"),
        text(lines("今、AIの最先端であるアメリカでは、", f"{rose('まったく逆の現象')}が起きています。", "", "AIが文章を書けるようになった結果、", f"{mark('「人間のコピーライター」の価値が上がり始めている')}", "のです。"), fs=18, fsm=16),
        spacer(20),
        text(lines("象徴的な出来事があります。", "", "Claudeという、世界的に注目されている生成AIがあります。", "そのClaudeを開発しているのが、", "アメリカのAI企業、Anthropic（アンソロピック）です。", "", "世界最高峰のAI研究者やエンジニアたちが集まり、", "AIの未来をつくっている企業の一つ。", "", "そのAnthropicが、ある求人を出しました。", "募集していたのは、", "エンジニアでも、AI研究者でもありません。"), fs=16, fsm=15),
        spacer(10),
    ])]),
    row([card([
        text(P("その職種は──", color=GOLD), fs=15, fsm=14, pb=0),
        head(f'<p style="text-align:center;"><span style="color:{ROSE_D};">「Standards Editor」</span></p>', fs=32, fsm=24),
        text(lines("簡単に言えば、", "会社が世の中に出す文章について、"), fs=16, fsm=15, pb=1),
        {"type":"bullet","content":"<ul><li>文法は正しいか。</li><li>言葉遣いは適切か。</li><li>会社らしいトーンになっているか。</li><li>文章はわかりやすいか。</li><li>そして、余計なコンマが一つ残っていないか。</li></ul>","check_style":"check-fa-check","check_color":ROSE,"font_size":16,"font_size_mobile":15,"item_spacing":8,"padding_side":4},
        text(lines("そこまで人間の目でチェックし、", f"{mark('文章の品質を守る仕事')}です。"), fs=16, fsm=15),
    ], bg=WHITE, border="#F2C4CD", radius=24)]),
    row([col([spacer(30,20),
        text(lines("では、この仕事に", f"Anthropicは{rose('いくら払おうとしていたのか？')}"), fs=19, fsm=17),
    ])]),
    row([card([
        text(P("提示された給与レンジ", color=WHITE), fs=15, fsm=14, pb=0),
        head(f'<p style="text-align:center;"><span style="color:{WHITE};">年俸 26万5,000～29万5,000ドル</span></p>', fs=26, fsm=19),
        text(f'<p style="text-align:center;"><span style="color:{WHITE};">日本円にすれば…</span><br><span style="color:{WHITE};font-size:36px;font-weight:bold;">約4,000万円</span><span style="color:{WHITE};">クラス</span></p>', fs=16, fsm=15, lh="1.6"),
        text(P("※為替によって変動します", color="#FFE9EE"), fs=12, fsm=11, pb=0),
    ], bg=ROSE, radius=24, pt=5, pb=4)]),
    row([col([spacer(30,20),
        text(lines("AIが世界中の文章を書き始めようとしている時代に、", "そのAIを作っている会社が、", f"人間の{mark('「文章を見る力」')}に、", "これだけのお金を払おうとしている。", "", f"{rose('しかも、これだけではありません。')}", "", "Anthropicは、コピーやコンテンツ全体を率いる", "「Head of Copy」というポジションも募集しました。"), fs=16, fsm=15),
    ])]),
    row([card([
        text(P("Head of Copy の提示年俸", color=WHITE), fs=15, fsm=14, pb=0),
        head(f'<p style="text-align:center;"><span style="color:{WHITE};">32万～40万ドル</span></p>', fs=30, fsm=22),
        text(f'<p style="text-align:center;"><span style="color:{WHITE};">日本円なら</span><br><span style="color:{WHITE};font-size:32px;font-weight:bold;">5,000万円～6,000万円</span><span style="color:{WHITE};">クラス</span></p>', fs=16, fsm=15, lh="1.6", pb=1),
    ], bg=GOLD, radius=24, pt=5, pb=4)]),
    row([col([spacer(60,40)])]),
], bg=WHITE, name="Anthropicの事例"))

# ---------- 4. なぜ人間の書き手？ ----------
E.append(section([
    row([col([spacer(60,40), *label("WHY HUMAN?", "なぜ「人間の書き手」が必要なのか"),
        text(lines("世界最高峰のAIを作っている会社が、", "これほど高い報酬を払ってまで、", "「人間の書き手」を必要としているのでしょうか？"), fs=16, fsm=15),
        sub(P("答えはシンプルです。", color=ROSE_D), fs=20, fsm=17),
    ])]),
    row([card([
        text(lines("AIは文章を作れる。", "でも、その文章が", f"{mark('「人の心を動かすか」')}を判断するのは、", f"{rose('人間だからです。')}"), fs=20, fsm=17, lh="1.9", pb=1),
    ], bg=WHITE, radius=24)]),
    row([col([spacer(30,20),
        text(lines("AIに、「40代女性に向けた広告を書いて」と言えば、", "ものの数秒でそれらしい文章を作ってくれます。", "", f"{rose('でも──')}"), fs=16, fsm=15),
    ])]),
    row([card([
        {"type":"bullet","content":"<ul><li>その女性が夜、一人になったとき、どんなことに不安を感じているのか？</li><li>会社を辞めたいと思いながら、なぜ辞められないのか？</li><li>「起業したい」という言葉の裏側に、どんな期待と恐怖があるのか？</li><li>どんな一言を読んだ瞬間、「これ、私のことだ……」と思うのか？</li><li>どんな言葉なら、その人の背中をそっと押せるのか？</li></ul>","check_style":"check-fa-check","check_color":ROSE,"font_size":16,"font_size_mobile":15,"line_height":"1.8","item_spacing":14},
    ], bg=WHITE, border="#F2C4CD", radius=24, pt=5, pb=3)]),
    row([col([spacer(30,20),
        text(lines("そこには、", f"{mark('人間を理解する力')}が必要になります。", "", "つまり、これから価値がなくなるのは、", f"{rose('「ただ文章を量産するだけの人」')}です。", "", "しかし、AIを使いこなしながら──"), fs=17, fsm=15),
    ])]),
    row([
        card([sub(P("誰に", color=ROSE_D), fs=20, fsm=17)], w=3, radius=999, ps=1, pt=3, pb=2),
        card([sub(P("何を", color=ROSE_D), fs=20, fsm=17)], w=3, radius=999, ps=1, pt=3, pb=2),
        card([sub(P("どんな順番で", color=ROSE_D), fs=17, fsm=15)], w=3, radius=999, ps=1, pt=3, pb=2),
        card([sub(P("どんな言葉で", color=ROSE_D), fs=17, fsm=15)], w=3, radius=999, ps=1, pt=3, pb=2),
    ], display_style="2on2", column_gap=12, column_gap_mobile=10),
    row([col([spacer(20),
        text(lines("伝えれば人の感情が動き、", "行動してもらえるのかを考えられる人。", "", "つまり、"), fs=17, fsm=15),
        head(P(f'「AI × コピーライティング」<br>ができる人', color=ROSE_D), fs=30, fsm=22),
        text(lines("の価値は、", f"{mark('むしろこれから高くなっていく可能性があります。')}"), fs=18, fsm=16),
        spacer(60,40),
    ])]),
], bg=BLUSH, name="なぜ人間か"))

# ---------- 5. 日本にも波が来る ----------
E.append(section([
    row([col([spacer(60,40), *label("COMING SOON", "この波は、まもなく日本にもやってくる"),
        text(lines("シリコンバレーに象徴されるような、", "アメリカのビジネスやマーケティングに関して、", f"日本は{rose('３年遅れている')}とよく言われます。", "", "今アメリカで当たり前になりつつあるものが、", "日本で当たり前になるまでに", "３年くらいかかるからです。", "", "ということは、", f"{mark('この波は３年後の日本で当たり前になってくる')}", "と予測できます。"), fs=16, fsm=15),
    ])]),
    row([card([
        text(lines("早いうちにこのスキルを身につけておけば、", "これから来るであろう", f"{rose('ライター募集の絶頂期')}には、", f"{mark('実績を積んだ状態でエントリーできる')}", "ということです。"), fs=18, fsm=16, lh="1.9", pb=1),
    ], bg=CREAM, border="#EAD7C3", radius=24)]),
    row([col([spacer(60,40)])]),
], bg=WHITE, name="日本にも波が来る"))

# ---------- 6. 会社員にも ----------
def tag(t):
    return card([text(P(t, color=ROSE_D, weight="bold"), fs=15, fsm=13, lh="1.5", pb=0)], w=3, radius=999, ps=1, pt=2, pb=2)
E.append(section([
    row([col([spacer(60,40), *label("MERIT 01", "起業しなくても、身につけられる"),
        text(lines("このスキルの素晴らしいところは、", f"{mark('起業しなくても身につけられること。')}", "", "もし今、あなたが会社員なら、", "その会社の中で力を発揮することができます。"), fs=17, fsm=15),
        spacer(10),
    ])]),
    row([tag("商品紹介文"), tag("営業メール"), tag("ホームページ"), tag("SNS")], display_style="2on2", column_gap=10, column_gap_mobile=8),
    row([tag("プレゼン資料"), tag("採用ページ"), tag("お客様への案内"), tag("広告")], display_style="2on2", column_gap=10, column_gap_mobile=8),
    row([col([spacer(20),
        text(lines("会社は毎日、", f"{rose('「人を動かすための言葉」')}を使っています。", "", "しかも、これから多くの会社が", "AIを使って文章を作るようになるでしょう。", "", "そこで必要になるのは、", "AIに何を指示するのかを考え、", "出てきた文章を見て──"), fs=16, fsm=15),
        {"type":"balloon","content":P("これはいい", align="left"),"image_url":ph(200,200,"✓"),"image_position":"left","image_width":60,"image_width_mobile":50,"font_size":16,"font_size_mobile":15},
        {"type":"balloon","content":P("これは伝わらない", align="left"),"image_url":ph(200,200,"✓"),"image_position":"right","image_width":60,"image_width_mobile":50,"font_size":16,"font_size_mobile":15},
        {"type":"balloon","content":P("もっとこうしたほうが人は動く", align="left"),"image_url":ph(200,200,"✓"),"image_position":"left","image_width":60,"image_width_mobile":50,"font_size":16,"font_size_mobile":15},
        text(lines("と判断できる人です。"), fs=16, fsm=15),
    ])]),
    row([card([
        text(lines("コピーライティングは", "副業や起業のためだけの能力ではありません。", "", f"{mark('会社員としてのあなたの価値まで')}", f"{mark('高めてくれるスキル')}なのです。"), fs=18, fsm=16, lh="1.9", pb=1),
    ], bg=WHITE, radius=24)]),
    row([col([spacer(60,40)])]),
], bg=BLUSH, name="会社員にも"))

# ---------- 7. PC一台 ----------
def place(icon, t):
    return card([text(f'<p style="text-align:center;"><span style="font-size:34px;">{icon}</span><br><span style="color:{ROSE_D};font-weight:bold;">{t}</span></p>', fs=16, fsm=14, lh="1.6", pb=0)], w=4, radius=20, ps=1, pt=4, pb=3, border="#F2C4CD")
E.append(section([
    row([col([spacer(60,40), *label("MERIT 02", "パソコン一台で、場所を選ばない"),
        text(lines("必要なのは、基本的にパソコン一台。", "", "お店を借りる必要もない。", "在庫を抱える必要もない。", "高額な設備もいらない。"), fs=17, fsm=15),
    ])]),
    row([place("🏠","自宅でもいい"), place("☕","カフェでもいい"), place("✈","旅先でもいい")], column_gap=14, column_gap_mobile=8),
    row([col([spacer(20),
        text(lines(f"{mark('場所を選ばず仕事ができます。')}", "", "しかも今は、", f"AIという{rose('強力なアシスタント')}がいます。"), fs=17, fsm=15),
    ])]),
    row([card([
        {"type":"bullet","content":"<ul><li>リサーチを手伝ってもらう</li><li>アイデアを出してもらう</li><li>構成を考えてもらう</li><li>文章のたたき台を作ってもらう</li></ul>","check_style":"check-fa-check","check_color":GOLD,"font_size":16,"font_size_mobile":15,"item_spacing":8},
        text(lines("それを人間が、", f"{mark('「人を動かす文章」')}に仕上げる。"), fs=17, fsm=15, pb=1),
    ], bg=CREAM, border="#EAD7C3", radius=24, pt=5, pb=4)]),
    row([col([spacer(30,20),
        text(lines("この働き方なら、", "「会社員だから時間がない」という人でも、", f"{rose('平日の夜や休日などのスキマ時間')}から", "始めることができます。", "", "最初から会社を辞めなくていい。", "まずは会社員を続けながら──"), fs=16, fsm=15),
    ])]),
    row([
        card([text(f'<p style="text-align:center;"><span style="color:{INK};">STEP 1</span><br><span style="color:{ROSE};font-size:26px;font-weight:bold;">月3万円</span></p>', fs=13, fsm=12, lh="1.5", pb=0)], w=4, bg="#FDF0F2", radius=16, ps=1, pt=3, pb=3),
        card([text(f'<p style="text-align:center;"><span style="color:{INK};">STEP 2</span><br><span style="color:{ROSE};font-size:26px;font-weight:bold;">月5万円</span></p>', fs=13, fsm=12, lh="1.5", pb=0)], w=4, bg="#FAE0E5", radius=16, ps=1, pt=3, pb=3),
        card([text(f'<p style="text-align:center;"><span style="color:{WHITE};">STEP 3</span><br><span style="color:{WHITE};font-size:26px;font-weight:bold;">月10万円</span></p>', fs=13, fsm=12, lh="1.5", pb=0)], w=4, bg=ROSE, radius=16, ps=1, pt=3, pb=3),
    ], column_gap=10, column_gap_mobile=6),
    row([col([spacer(20),
        text(lines("自分の力で稼ぐ経験を", "少しずつ積み上げていけばいいのです。"), fs=17, fsm=15),
        spacer(50,30),
    ])]),
], bg=WHITE, name="PC一台"))

# ---------- 8. 恐怖が自信に ----------
E.append(section([
    row([col([spacer(60,40),
        text(lines("すると、"), fs=16, fsm=15, pb=1),
    ])]),
    row([card([
        text(P("「会社を辞めたら、生きていけない」", color="#8A7A80"), fs=18, fsm=15, pb=1),
        text(P("という恐怖が、少しずつ…", color=INK), fs=15, fsm=14, pb=1),
        text(P("▼", color=ROSE), fs=20, fsm=18, pb=1, lh="1.2"),
        text(P(f"「もしかしたら私、<br>自分の力でも生きていけるかもしれない」", color=ROSE_D, weight="bold"), fs=21, fsm=17, lh="1.7", pb=1),
        text(P("という自信に変わっていきます。", color=INK), fs=15, fsm=14, pb=0),
    ], bg=WHITE, radius=24)]),
    row([col([spacer(30,20),
        text(lines("そのとき初めて、", "", "会社員を続けるのか。", "副業を大きくするのか。", "独立するのか。", "起業するのか。", "", f"{mark('あなた自身が選べばいいのです。')}", "", "その選択肢をあなたに与えてくれる可能性があるのが、", "AI時代だからこそ価値を持つ、"), fs=16, fsm=15),
        head(P("「人を動かす言葉の技術」", color=ROSE_D), fs=30, fsm=22),
        text(lines("です。", "", "そのノウハウを、あなたにお伝えしようと思います。"), fs=17, fsm=15),
        spacer(60,40),
    ])]),
], bg="#FCE4E8", bg_to=CREAM, name="恐怖が自信に"))

# ---------- 9. スワイプファイル ----------
E.append(section([
    row([col([spacer(60,40), *label("SWIPE FILE", "本当に誰でもライターになれるの？"),
        text(lines("でも、ライターってすぐになれないでしょ？", "と思われるかもしれません。", "", "もちろん一人で始めたら無理でしょう。", "", "しかし、ちゃんとしたプロのサポートを受けさえすれば、", f"{mark('AIを駆使することで、すぐに売れる文章を書くことができます。')}", "", "その理由の1つが、", f"{rose('「スワイプファイル」')}というものです。"), fs=16, fsm=15),
    ])]),
    row([card([
        sub(P("スワイプファイルとは？", color=ROSE_D), fs=20, fsm=17),
        text(lines("実は集客ページには", f"{rose('売れるテンプレート（型）')}があり、", "そのテンプレート通りに真似して書いていくだけで", "完成させることができるのです。", "", "今回の講師である小嶋（おじま）さんのところには、", "過去に反応の良かった原稿が沢山あり、", "そのテンプレートを取り入れることで、", f"{mark('プロが書いたような原稿を作成できてしまう')}のです。", "", "この見本原稿のことをスワイプファイルと言います。"), fs=15, fsm=14, pb=1),
    ], bg=BLUSH, radius=24, pt=5, pb=4)]),
    row([col([spacer(30,20),
        text(lines("実は、プロのコピーライターも", "このスワイプファイルを見ながら", "原稿を作成していることがほとんどです。", "", "しかし、実際に売れている原稿を真似しなければ", "意味がありません。", "見栄えの良いページでも、", "全く売れていない集客ページは世の中に沢山あります。", "それを真似しても、売れなくて当然です。", "", f"{mark('実際に売れている原稿の構成を真似て書くだけ')}なので、", "初心者でも書くことができるのです。"), fs=16, fsm=15),
    ])]),
    row([card([
        text(P("実 績", color=GOLD, weight="bold"), fs=14, fsm=13, pb=0),
        text(lines("３ヶ月前からライターとして", "ゼロからスタートした人が、"), fs=16, fsm=15, pb=0),
        head(P(f'すでに<span style="font-size:44px;">３件</span>も案件を獲得！', color=ROSE_D), fs=26, fsm=20),
    ], bg=WHITE, border=GOLD, radius=24, pt=5, pb=3)]),
    row([col([spacer(60,40)])]),
], bg=WHITE, name="スワイプファイル"))

# ---------- 10. 体験の勧め ----------
E.append(section([
    row([col([spacer(60,40),
        head(P("まずは、ライター体験<br>してみませんか？", color=ROSE_D), fs=32, fsm=24),
        divider(),
        text(lines("これからますますAIが広がっていく中で、", f"{mark('「書ける人材」の価値')}が上がってきます。", "", "皆が気付く前に、", "少しでも早くスキルを身につけることが大事です。", f"{rose('皆が学び始めたら価値も下がり、報酬も下がるから')}です。", "", "ですので、少しでも興味があるのであれば、", "あなたにセミナー集客ライターとしての", "適性があるかどうか？", "体験してみませんか？"), fs=16, fsm=15),
        spacer(10),
        cta(),
        spacer(60,40),
    ])]),
], bg=BLUSH, name="体験の勧め"))

# ---------- 11. セミナー内容 ----------
items = [
    "これを知るだけで反応の取れるページに変わります！<strong>売れるテンプレートとは？</strong>",
    "内容をわかりやすく伝えるだけでは意味がありません。<strong>素人が知らないキャッチコピーの秘密とは？</strong>",
    "ターゲットを絞るとなぜ売れるようになるの？<strong>プロでも知らない売れる広告の秘密とは？</strong>",
    "実は集客ライティングで難しいのは２箇所だけ。<strong>これだけできればAIには真似できない売れるLPが作れます</strong>",
    "ここが決まらなければ全く売れることはありません。<strong>セミナーコンセプトメイキングのテクニックとは？</strong>",
    "リサーチでは何を質問すればいいのか？<strong>プロのライターが使う質問集をプレゼント！</strong>",
    "あなたのライティング力をアップさせる、<strong>小嶋式トレーニング法とは？</strong>",
]
E.append(section([
    row([col([spacer(60,40), *label("SEMINAR CONTENTS", "体験セミナーの内容")])]),
    row([card([
        {"type":"bullet","content":"<ul>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>","check_style":"check-fa-check","check_color":ROSE,"font_size":16,"font_size_mobile":15,"line_height":"1.8","item_spacing":18},
    ], bg=WHITE, border="#F2C4CD", radius=24, pt=6, pb=4)]),
    row([col([spacer(40,30), cta(), spacer(60,40)])]),
], bg=CREAM, name="セミナー内容"))

# ---------- 12. 講師プロフィール ----------
E.append(section([
    row([col([spacer(60,40), *label("PROFILE", "講師プロフィール")])]),
    row([card([
        {"type":"image-text","image_url":ph(400,400,"講師写真"),"image_position":"left","image_width":"35","image_width_mobile":"100","image_design":"circle",
         "content":f'<p><span style="color:{GOLD};font-size:13px;">株式会社オン・プレーン 代表取締役</span></p><p><span style="color:{ROSE_D};font-size:26px;font-weight:bold;">小嶋 優來</span> <span style="color:{INK};font-size:13px;">（おじま）</span></p><p><span style="color:{INK};">言葉の力を使って中小企業の集客、販売促進を支援するコピーライター 兼 マーケティングコンサルタント。</span></p>',
         "font_size":15,"font_size_mobile":14,"line_height":"1.8"},
        spacer(20),
        text(lines(
            "1976年生まれ。経営者の家系に育ち、大学卒業後に上場企業のカー用品店に入社。販売促進室の責任者として活躍。",
            "10年間、チラシ、ラジオ、テレビCM、DM、新聞、雑誌などあらゆるジャンルの広告媒体を経験し、コピーライティングの技術を身につける。",
            f"2010年に独立し、ネット通販会社代表に。1年目はまったく売れなかったが、改めて中小企業向けのマーケティングを勉強して改善。{rose('2年目には年商1億、3年目には年商4億')}まで成長させるなど、実践でマーケターとして活躍する。",
            "しかし、東日本大震災で仕入れ不能の事態に陥り物販の危うさを感じ、2014年に過去の経験を活かした集客コピーライター兼マーケティングコンサルタントとしても活動を開始。",
            f"さまざまな企業のコンサルティングに関わるほか、{rose('1.8億円を売上げたコンサルタント養成講座')}、{rose('年間3000人集客の営業セミナー')}を主催するなど、結果を出し続けている。",
            f"毎月開催している私塾「マーケティングの寺子屋」は、{rose('受講者の70%が1年以上継続')}する人気講座。",
            align="left"), fs=15, fsm=14, lh="1.9"),
    ], bg=WHITE, radius=24, pt=6, pb=4)]),
    row([col([spacer(30,20)])]),
    row([
        col([{"type":"image","image_url":ph(300,420,"書影"),"width":200,"align":"center","padding_bottom":0}], w=4),
        col([
            text(f'<p><span style="color:{GOLD};font-size:13px;letter-spacing:0.15em;">BOOK</span></p><p><span style="color:{ROSE_D};font-size:20px;font-weight:bold;">『うまくいっている会社の<br>非常識な儲け方』</span></p><p><span style="color:{INK};">2023年2月 すばる舎より出版。<br>紀伊國屋書店、丸善、有隣堂など大型書店で{rose("ランキング１位")}をはじめ上位を獲得。</span></p>', fs=15, fsm=14, lh="1.8", pb=0),
        ], w=8, padding_top=2),
    ], column_gap=24, column_gap_mobile=10),
    row([col([spacer(60,40)])]),
], bg=BLUSH, name="講師プロフィール"))

# ---------- 13. 最終CTA ----------
E.append(section([
    row([col([spacer(70,50),
        text(P("＼ 本当にあなたもライターになれるのか？ ／", color=WHITE), fs=16, fsm=13, pb=1),
        head(P("AI感情ライター養成講座<br>１DAY体験セミナー", color=WHITE), fs=34, fsm=24),
        text(P("体験セミナーで、力試ししてみませんか？", color=WHITE), fs=17, fsm=15, pb=5),
        cta("今すぐ体験セミナーに申し込む", "＼ 未経験・女性・自分のためでもOK ／", light=True),
        spacer(70,50),
    ])]),
], bg="#E7849A", bg_to="#F2B8A8", deg="135", name="最終CTA"))

E.append(section([row([col([text(P("© 株式会社オン・プレーン All Rights Reserved.", color="#9C8A90"), fs=12, fsm=11, pb=2, padding_top=4)])])], bg=WHITE, name="フッター"))

out = {
    "page_settings": {
        "title": "AI感情ライター養成講座 1DAY体験セミナーLP",
        "page_title": "AI感情ライター養成講座｜1DAY体験セミナー",
        "pc_width": 100,
        "background_color": CREAM,
        "css": "@import url('https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@400;500;700;900&display=swap');\nbody, p, h1, h2, h3, .btn { font-family: 'Zen Maru Gothic', 'Hiragino Maru Gothic ProN', sans-serif !important; letter-spacing: 0.04em; }",
        "meta_title": "AI感情ライター養成講座 1DAY体験セミナー",
        "meta_description": "未経験OK！女性OK！たった7つのテンプレートで集客ページを完成させる、AIを活用したコピーライターの体験セミナー。",
    },
    "elements": E,
}
REPL=[
 ('<p style="text-align:center;">','<p class="tc">'),
 (f'<span style="color:{WHITE};font-size:36px;font-weight:bold;">','<span class="w b f36">'),
 (f'<span style="color:{WHITE};font-size:32px;font-weight:bold;">','<span class="w b f32">'),
 (f'<span style="color:{WHITE};font-size:26px;font-weight:bold;">','<span class="w b f26">'),
 (f'<span style="color:{ROSE};font-size:26px;font-weight:bold;">','<span class="r b f26">'),
 (f'<span style="color:{WHITE};background-color:{ROSE};border-radius:999px;padding:6px 16px;font-weight:bold;">','<span class="badge">'),
 (f'<span style="color:{WHITE};background-color:{ROSE};padding:6px 16px;font-weight:bold;">','<span class="badge">'),
 (f'<span style="color:{WHITE};">','<span class="w">'),
 (f'<span style="color:{INK};">','<span>'),
 (f'<span style="color:{GOLD};letter-spacing:0.25em;">','<span class="g ls">'),
 (f'<span style="color:{ROSE_D};">','<span class="rd">'),
]
def comp(o):
    if isinstance(o,dict): return {k:comp(v) for k,v in o.items()}
    if isinstance(o,list): return [comp(v) for v in o]
    if isinstance(o,str):
        for a,b in REPL: o=o.replace(a,b)
    return o
out["elements"]=comp(out["elements"])
out["page_settings"]["css"] += """
.tc{text-align:center}.b{font-weight:bold}.r{color:#D46A82}.rd{color:#B8506A}.g{color:#C9A27E}.w{color:#fff}.ls{letter-spacing:.25em}
.f26{font-size:26px}.f32{font-size:32px}.f36{font-size:36px}
.mk{background:linear-gradient(transparent 60%,#F9D3DB 60%);font-weight:bold}
.badge{color:#fff;background:#D46A82;border-radius:999px;padding:6px 16px;font-weight:bold;white-space:nowrap}
p{color:#5B4A50}
@media(max-width:600px){.f36{font-size:28px}.f32{font-size:24px}.f26{font-size:22px}}"""
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=2)
print("sections:", len(E))
