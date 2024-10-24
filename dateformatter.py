import ipywidgets as widgets
from IPython.display import display
import datetime

"""
拡張性
選んだ日付を削除
日付に優先順位をつける（現在は時間順にソート）
時間と分のUI改善
"""

# 日本語の曜日名
weekdays_jp = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

# 日付リストを保持
selected_datetimes = set()

# DatePickerウィジェットの作成
date_picker = widgets.DatePicker(
    description='日付を選択',
    disabled=False
)

# 時間選択のウィジェット作成（スライダーで開始時間を選択）
start_hour_picker = widgets.IntSlider(
    value=12,
    min=0,
    max=23,
    step=1,
    description='開始時:',
    continuous_update=False
)

start_minute_picker = widgets.IntSlider(
    value=0,
    min=0,
    max=59,
    step=1,
    description='開始分:',
    continuous_update=False
)

# 終了時間のウィジェット作成
end_hour_picker = widgets.IntSlider(
    value=13,
    min=0,
    max=23,
    step=1,
    description='終了時:',
    continuous_update=False
)

end_minute_picker = widgets.IntSlider(
    value=0,
    min=0,
    max=59,
    step=1,
    description='終了分:',
    continuous_update=False
)

# ボタン作成
button = widgets.Button(description="追加")

# ボタンが押されたときの処理
def on_button_click(b):
    selected_date = date_picker.value
    start_hour = start_hour_picker.value
    start_minute = start_minute_picker.value
    end_hour = end_hour_picker.value
    end_minute = end_minute_picker.value
    
    if selected_date:
        # 日付と時間を結合
        start_datetime = datetime.datetime.combine(selected_date, datetime.time(start_hour, start_minute))
        end_datetime = datetime.datetime.combine(selected_date, datetime.time(end_hour, end_minute))
        
        selected_datetimes.add((start_datetime, end_datetime))

        # フォーマットして出力
        formatted_output = f"{start_datetime.strftime('%m/%d')}({weekdays_jp[start_datetime.weekday()]}) {start_hour:02d}:{start_minute:02d} - {end_hour:02d}:{end_minute:02d}"
        print(f"追加された日時: {formatted_output}")
    else:
        print("日付を選択してください。")

# すべての選択を表示するボタン作成
show_button = widgets.Button(description="すべての選択を表示")

def show_selected(b):
    if selected_datetimes:
        # 時間順にソート
        sorted_datetimes = sorted(selected_datetimes, key=lambda x: x[0])
        print("選択された日時:")
        for start_dt, end_dt in sorted_datetimes:
            formatted_output = f"{start_dt.strftime('%m/%d')}({weekdays_jp[start_dt.weekday()]}) {start_dt.hour:02d}:{start_dt.minute:02d} - {end_dt.hour:02d}:{end_dt.minute:02d}"
            print(formatted_output)
    else:
        print("まだ日時は選択されていません。")

# ボタンにイベントハンドラを追加
button.on_click(on_button_click)
show_button.on_click(show_selected)

# ウィジェットを表示
display(date_picker, start_hour_picker, start_minute_picker, end_hour_picker, end_minute_picker, button, show_button)
