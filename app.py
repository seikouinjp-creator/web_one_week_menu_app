import datetime
import random
import streamlit as st

# ==========================================
# 四毒抜き データベース
# ==========================================
BREAKFASTS = [
    ("白米ご飯(普通) ＋ 納豆 ＋ 豆腐わかめ味噌汁 ＋ 焼き海苔", 450),
    ("玄米ご飯(普通) ＋ 焼き塩鮭 ＋ 大根おろし ＋ ほうれん草 ＋ 味噌汁", 500),
    ("雑穀米(普通) ＋ 温泉卵 ＋ 鶏胸肉蒸し焼き ＋ 小松菜煮浸し", 480),
    ("白米ご飯(普通) ＋ 釜揚げしらす ＋ 梅干し ＋ 白菜漬け ＋ 味噌汁", 410),
    ("玄米ご飯(普通) ＋ 納豆 ＋ 鯖塩焼き ＋ モロヘイヤ ＋ 味噌汁", 530),
    ("雑穀米(普通) ＋ 茹で鶏ささみ ＋ 茎わかめ佃煮 ＋ 味噌汁", 440),
    ("白米ご飯(普通) ＋ 卵焼き(出汁) ＋ 焼きタラコ ＋ 根菜味噌汁", 470),
]

SNACKS = [
    ("焼き芋（紅はるか等のサツマイモ）", 180),
    ("栗の渋皮煮（甘酒使用・砂糖不使用）", 160),
    ("干し柿（自然の甘みそのまま）", 150),
    ("焼きリンゴ（シナモン風味）", 120),
    ("寒天ゼリー（100%みかんジュース固め）", 70),
    ("焼き餅（玄米餅を醤油と海苔で）", 210),
    ("蒸し黒豆（塩のみ）", 140),
    ("甘栗（無添加むき甘栗）", 130),
    ("小豆のスープ煮（甘酒風味）", 150),
    ("バナナとアーモンドの素焼き", 200),
]

SEASONAL_MEALS = {
    "春": {
        "lunches": [
            ("新玉ねぎと鶏もも肉グリル ＋ 蒸しブロッコリー ＋ 白米ご飯 ＋ すまし汁", 600),
            ("サワラの塩焼き ＋ 新じゃが煮っころがし ＋ 雑穀米 ＋ 豆腐汁", 560),
            ("豚ロース茹でしゃぶポン酢 ＋ 春キャベツ ＋ 玄米ご飯 ＋ 根菜味噌汁", 610),
            ("カツオタタキ ＋ アスパラ塩茹で ＋ 雑穀米 ＋ 玉ねぎワカメ味噌汁", 540),
            ("鶏ささみキュウリ梅肉和え ＋ 焼き椎茸 ＋ 白米ご飯 ＋ 新玉ねぎ味噌汁", 500),
            ("釜揚げしらす丼 ＋ ほうれん草おひたし ＋ 豆腐味噌汁", 510),
            ("鶏胸肉低温調理 ＋ 茹でキャベツ ＋ 玄米ご飯 ＋ 和風スープ", 530),
        ],
        "dinners": [
            ("鯛のあら炊き ＋ 小松菜 ＋ 白米ご飯 ＋ 豆腐味噌汁", 490),
            ("牛すじ大根煮込み ＋ 胡瓜塩もみ ＋ 玄米ご飯 ＋ アオサ味噌汁", 630),
            ("鯖の味噌煮 ＋ 蒸しキャベツ ＋ 白米ご飯 ＋ 玉ねぎすまし汁", 640),
            ("鶏手羽元スープ煮 ＋ 焼き茄子 ＋ 雑穀米", 570),
            ("鮭ホイル焼き ＋ ほうれん草おひたし ＋ 白米ご飯 ＋ 豆腐味噌汁", 550),
            ("ホッケ塩焼き ＋ 大根おろし ＋ 茎わかめ炒り煮 ＋ 玄米ご飯 ＋ 豚汁", 660),
            ("鶏むね肉と根菜ポトフ ＋ ほうれん草白和え ＋ 白米ご飯", 580),
        ],
    },
    "夏": {
        "lunches": [
            ("鶏ももレモン塩焼き ＋ 冷やしトマト ＋ 白米ご飯 ＋ オクラワカメ汁", 590),
            ("アジ塩焼き ＋ ナスピーマン焼き浸し ＋ 玄米ご飯 ＋ 味噌汁", 540),
            ("豚しゃぶ冷製ポン酢 ＋ キュウリワカメ酢の物 ＋ 雑穀米 ＋ 根菜味噌汁", 550),
            ("カツオ刺身定食 ＋ 茹でオクラ和え ＋ 白米ご飯 ＋ アオサお吸い物", 510),
            ("鶏ささみモロヘイヤ和え ＋ 焼き椎茸 ＋ 雑穀米 ＋ トマト玉ねぎスープ", 470),
            ("マグロ漬け丼 ＋ ズッキーニグリル ＋ 豆腐味噌汁", 530),
            ("白身魚ホイル蒸し(レモン) ＋ ナス煮浸し ＋ 玄米ご飯 ＋ 玉ねぎ味噌汁", 480),
        ],
        "dinners": [
            ("タチウオ塩焼き ＋ 夏野菜グリル ＋ 白米ご飯 ＋ 豆腐味噌汁", 530),
            ("豚肉ゴーヤチャンプルー風 ＋ 胡瓜塩もみ ＋ 玄米ご飯 ＋ モロヘイヤスープ", 600),
            ("イサキ煮付け ＋ 蒸しキャベツ ＋ 白米ご飯 ＋ ナス油揚げ味噌汁", 520),
            ("鶏手羽元冬瓜スープ煮 ＋ 焼き茄子 ＋ 雑穀米", 550),
            ("鮭塩焼き ＋ ほうれん草おひたし ＋ 白米ご飯 ＋ トマト和風スープ", 540),
            ("アジ干物 ＋ 大根おろし ＋ キュウリワカメ酢の物 ＋ 玄米ご飯 ＋ 味噌汁", 530),
            ("鶏むね肉冷やし梅肉煮 ＋ 茹でオクラ ＋ 白米ご飯 ＋ 根菜味噌汁", 510),
        ],
    },
    "秋": {
        "lunches": [
            ("秋刀魚塩焼き(すだち) ＋ 大根おろし ＋ 白米ご飯 ＋ 豆腐キノコ味噌汁", 610),
            ("戻り鰹タタキ ＋ 舞茸ホイル焼き ＋ 雑穀米 ＋ 根菜味噌汁", 560),
            ("豚ロース生姜焼き(砂糖不使用) ＋ キャベツ千切り ＋ 玄米ご飯 ＋ 豆腐汁", 630),
            ("サケ塩焼き ＋ ほうれん草胡麻和え ＋ 白米ご飯 ＋ サツマイモ味噌汁", 580),
            ("鶏ささみキノコ温野菜サラダ ＋ 玄米ご飯 ＋ 玉ねぎすまし汁", 490),
            ("ブリ塩焼き ＋ 切り干し大根 ＋ 雑穀米 ＋ 豆腐ワカメ味噌汁", 600),
            ("鶏胸肉グリル ＋ 焼き椎茸 ＋ 白米ご飯 ＋ 根菜味噌汁", 520),
        ],
        "dinners": [
            ("鯛あら炊き ＋ 小松菜 ＋ 白米ご飯 ＋ 豆腐味噌汁", 490),
            ("牛すじ大根ゴボウ煮込み ＋ 胡瓜塩もみ ＋ 玄米ご飯 ＋ アオサ味噌汁", 650),
            ("鯖味噌煮 ＋ 蒸しキャベツ ＋ 白米ご飯 ＋ 玉ねぎすまし汁", 640),
            ("鶏手羽元根菜スープ煮 ＋ 焼き茄子 ＋ 雑穀米", 590),
            ("鮭キノコホイル焼き ＋ ほうれん草おひたし ＋ 白米ご飯 ＋ 豆腐味噌汁", 560),
            ("ホッケ塩焼き ＋ 大根おろし ＋ 茎わかめ炒り煮 ＋ 玄米ご飯 ＋ 豚汁", 660),
            ("鶏むね肉サツマイモ和風煮 ＋ ほうれん草白和え ＋ 白米ご飯", 570),
        ],
    },
    "冬": {
        "lunches": [
            ("ブリ照り焼き風(砂糖不使用) ＋ ほうれん草おひたし ＋ 白米ご飯 ＋ 大根味噌汁", 620),
            ("タラ白菜土鍋スープ蒸し ＋ 雑穀米 ＋ 豆腐味噌汁", 500),
            ("豚ロース茹でしゃぶ ＋ 大根おろしポン酢 ＋ 玄米ご飯 ＋ 根菜たっぷり豚汁", 640),
            ("塩サバグリル ＋ 焼きネギ ＋ 白米ご飯 ＋ 豆腐ワカメ味噌汁", 600),
            ("鶏ささみレンコン炒め煮 ＋ 雑穀米 ＋ 玉ねぎ味噌汁", 510),
            ("カレイ煮付け ＋ ほうれん草胡麻和え ＋ 白米ご飯 ＋ 豆腐汁", 490),
            ("鶏胸肉低温調理(塩麹) ＋ 蒸しブロッコリー ＋ 玄米ご飯 ＋ 根菜すまし汁", 530),
        ],
        "dinners": [
            ("白身魚と根菜の鍋仕立て ＋ 雑穀米", 530),
            ("牛すじ大根里芋煮込み ＋ 胡瓜塩もみ ＋ 玄米ご飯 ＋ アオサ味噌汁", 670),
            ("鯖味噌煮 ＋ 蒸し白菜 ＋ 白米ご飯 ＋ 玉ねぎすまし汁", 630),
            ("鶏手羽元白菜スープ煮 ＋ 焼き椎茸 ＋ 雑穀米", 550),
            ("鮭長ネギホイル焼き ＋ ほうれん草おひたし ＋ 白米ご飯 ＋ 豆腐味噌汁", 540),
            ("ホッケ塩焼き ＋ 大根おろし ＋ 根菜きんぴら ＋ 玄米ご飯 ＋ 豆腐味噌汁", 620),
            ("鶏むね肉冬野菜和風ポトフ ＋ 白米ご飯", 560),
        ],
    },
}


def get_season_from_month(month):
  if month in [3, 4, 5]:
    return "春"
  elif month in [6, 7, 8]:
    return "夏"
  elif month in [9, 10, 11]:
    return "秋"
  else:
    return "冬"


def calc_target_calories(gender, age, activity):
  if gender == "男性":
    if 50 <= age <= 64:
      if activity == "低い (デスクワーク)":
        return 2200
      elif activity == "普通 (通勤・家事)":
        return 2500
      else:
        return 2800
    else:
      if activity == "低い (デスクワーク)":
        return 2100
      elif activity == "普通 (通勤・家事)":
        return 2400
      else:
        return 2700
  else:
    if 50 <= age <= 64:
      if activity == "低い (デスクワーク)":
        return 1750
      elif activity == "普通 (通勤・家事)":
        return 2000
      else:
        return 2300
    else:
      if activity == "低い (デスクワーク)":
        return 1700
      elif activity == "普通 (通勤・家事)":
        return 1950
      else:
        return 2250


def filter_menu(menu_list, ng_words):
  if not ng_words:
    return menu_list
  filtered = []
  for item, cal in menu_list:
    if not any(ng in item for ng in ng_words if ng != ""):
      filtered.append((item, cal))
  return filtered


# Streamlitの画面構築
st.title("🌱 四毒抜き 旬の1週間献立ジェネレーター")
st.markdown(
    "小麦粉・植物油・砂糖・乳製品を一切使わない、和食ベースの献立自動生成アプリです。"
)

# サイドバーまたは入力エリア
with st.sidebar:
  st.header("⚙ 条件・カロリー設定")
  month_val = st.selectbox(
      "月を選択", [f"{i}月" for i in range(1, 13)], index=datetime.datetime.now().month - 1
  )
  gender_val = st.radio("性別", ["男性", "女性"], index=0)
  age_val = st.number_input("年齢", min_value=10, max_value=100, value=50)
  activity_val = st.selectbox(
      "活動量", ["低い (デスクワーク)", "普通 (通勤・家事)", "高い (運動・労働)"]
  )
  ng_val = st.text_input("除外食材(NG・カンマ区切り)", value="鯖, キノコ")

month = int(month_val.replace("月", ""))
season = get_season_from_month(month)
target_cal = calc_target_calories(gender_val, age_val, activity_val)
ng_words = [w.strip() for w in ng_val.replace("、", ",").split(",") if w.strip()]

avail_b = filter_menu(BREAKFASTS, ng_words)
avail_s = filter_menu(SNACKS, ng_words)
avail_l = filter_menu(SEASONAL_MEALS[season]["lunches"], ng_words)
avail_d = filter_menu(SEASONAL_MEALS[season]["dinners"], ng_words)

days = ["月", "火", "水", "木", "金", "土", "日"]
day_themes = {
    "月": "週の始まり：活力チャージ・バランス重視",
    "火": "平日の基本：手軽で栄養をしっかり摂る日",
    "水": "週の中日：胃腸にやさしい和食仕立て",
    "木": "週末直前：スタミナと満足感のある定食",
    "金": "華金：少し贅沢な魚・肉のメイン料理",
    "土": "週末：じっくり煮込みやオーブン料理",
    "日": "休日：家族みんなで楽しむ旬の味わい",
}

# セッション状態を使ってリロード時のランダム変化を防ぐ、またはボタンで生成
if "menu_data" not in st.session_state:
  st.session_state.menu_data = None

if st.button("🚀 献立を生成する", type="primary"):
  pool_b, pool_s, pool_l, pool_d = (
      list(avail_b),
      list(avail_s),
      list(avail_l),
      list(avail_d),
  )
  random.shuffle(pool_b)
  random.shuffle(pool_s)
  random.shuffle(pool_l)
  random.shuffle(pool_d)

  b_idx, s_idx, l_idx, d_idx = 0, 0, 0, 0
  temp_data = {}

  for day in days:
    temp_data[day] = {
        "朝": (
            pool_b[b_idx % len(pool_b)]
            if pool_b
            else ("条件に合うメニューなし", 0)
        ),
        "昼": (
            pool_l[l_idx % len(pool_l)]
            if pool_l
            else ("条件に合うメニューなし", 0)
        ),
        "おやつ": (
            pool_s[s_idx % len(pool_s)]
            if pool_s
            else ("条件に合うメニューなし", 0)
        ),
        "夜": (
            pool_d[d_idx % len(pool_d)]
            if pool_d
            else ("条件に合うメニューなし", 0)
        ),
    }
    b_idx += 1
    l_idx += 1
    s_idx += 1
    d_idx += 1
  st.session_state.menu_data = temp_data

# 画面表示
if st.session_state.menu_data:
  report = []
  report.append("=" * 68)
  report.append(
      f"     【 四毒抜き 旬の1週間献立表（目標カロリー完全一致版） 】"
  )
  report.append(
      f"     対象: {gender_val} / {age_val}歳 / 活動量: {activity_val}"
      f" ({month}月・{season})"
  )
  report.append(f"     🎯 1日の目標摂取カロリー: 約 {target_cal} kcal")
  if ng_words:
    report.append(f"     除外食材(NG): {', '.join(ng_words)}")
  report.append("     ※ 小麦粉・植物油・砂糖・乳製品は一切不使用")
  report.append("=" * 68 + "\n")

  total_week_cal = 0

  for day in days:
    b_name, b_c = st.session_state.menu_data[day]["朝"]
    l_name, l_c = st.session_state.menu_data[day]["昼"]
    s_name, s_c = st.session_state.menu_data[day]["おやつ"]
    d_name, d_c = st.session_state.menu_data[day]["夜"]

    raw_sum = b_c + l_c + s_c + d_c
    scale = (target_cal / raw_sum) if raw_sum > 0 else 1.0

    b_cal = int(b_c * scale)
    l_cal = int(l_c * scale)
    s_cal = int(s_c * scale)
    d_cal = int(d_c * scale)

    current_day_total = b_cal + l_cal + s_cal + d_cal
    d_cal += target_cal - current_day_total
    day_total_cal = b_cal + l_cal + s_cal + d_cal
    total_week_cal += day_total_cal

    st.subheader(f"■ {day}曜日 【 {day_themes[day]} 】")
    st.text(f"  [朝食] {b_name} （{b_cal} kcal）")
    st.text(f"  [昼食] {l_name} （{l_cal} kcal）")
    st.text(f"  [おやつ] {s_name} （{s_cal} kcal）")
    st.text(f"  [夕食] {d_name} （{d_cal} kcal）")
    st.info(f"  👉 【{day}曜日の合計】 : {day_total_cal} kcal （目標比: 0 kcal）")

    report.append(f"■ {day}曜日 【 {day_themes[day]} 】")
    report.append(f"  [朝食] {b_name} （{b_cal} kcal）")
    report.append(f"  [昼食] {l_name} （{l_cal} kcal）")
    report.append(f"  [おやつ] {s_name} （{s_cal} kcal）")
    report.append(f"  [夕食] {d_name} （{d_cal} kcal）")
    report.append(f"  👉 【{day}曜日の合計】 : {day_total_cal} kcal")
    report.append("-" * 63 + "\n")

  avg_week_cal = total_week_cal // 7
  report.append("=" * 68)
  report.append(f"  📊 1週間合計カロリー: {total_week_cal} kcal")
  report.append(f"  📊 1日平均カロリー: 約 {avg_week_cal} kcal/日")
  report.append(f"  🎯 設定された目標カロリー: 約 {target_cal} kcal/日")
  report.append("=" * 68)

  # テキストダウンロードボタン
  txt_data = "\n".join(report)
  st.download_button(
      label="💾 献立表をテキストファイルでダウンロード",
      data=txt_data,
      file_name="四毒抜き1週間献立表.txt",
      mime="text/plain",
  )
else:
  st.info(
      "左側のサイドバーで条件を設定し、「🚀 献立を生成する」ボタンを押してください。"
  )