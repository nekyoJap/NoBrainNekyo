import tkinter as tk
from nekyo import *

"""グローバル変数の定義
"""
entry = None  # 入力エリアのオブジェクト
response_area = None  # 応答エリアのオブジェクト
lb = None  # ログ表示用リストオブジェクト
action = None  # 'オプション'メニューの状態
nekyo = Nekyo('nekyo')


def putlog(str):
    """対話ログをリストボックスに表示する
        ＠str 入力文字列または応答メッセージ
    """
    lb.insert(tk.END, str)


def prompt():
    """ねきょのプロンプトをつくる
    """
    n = nekyo.name
    if (action.get()) == 0:
        n += ':' + nekyo.responder.name
    return n + '>'


def talk():
    """対話を行う関数
    　　・Nekyoクラスのdialog()を実行
    　　・入力文字列と応答メッセージをログに出力
    """
    value = entry.get()
    # 何も入力されなかった場合
    if not value:
        response_area.configure(text='なに？')
    # 入力された場合には処理を行う
    else:
        # 入力に対して応答する
        response = nekyo.dialogue(value)
        response_area.configure(text=response)
        # 入力への応答
        putlog('> ' + value)
        putlog(prompt() + response)
        # 入力エリアをクリア
        entry.delete(0, tk.END)


# ==================================================
# 画面を描画する
# ==================================================

def run():
    global entry, response_area, lb, action

    # メインウィンドを作成、体裁を整える
    root = tk.Tk()
    root.geometry('880x560')
    root.title('Your Friend Nekyo')
    font = ('Helevetica', 14)
    font_log = ('Helevetica', 11)

    # メニューバーの作成
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    # 「ファイルメニュー」
    filemenu = tk.Menu(menubar)
    menubar.add_cascade(label='ファイル', menu=filemenu)
    filemenu.add_command(label='閉じる', command=root.destroy)
    #  オプションメニュー
    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label='オプション', menu=optionmenu)
    optionmenu.add_radiobutton(
        label='Responderを表示',  # アイテム名
        variable=action,  # 選択時の値
        value=0  # actionの値を０にする
    )
    optionmenu.add_radiobutton(
        label='Responderを表示しない',  # アイテム名
        variable=action,  # 選択時の値
        value=1  # actionの値を１にする
    )

    # キャンパスの作成
    canvas = tk.Canvas(
        root,  # 親要素をメインウィンドウに設定
        width=500,
        height=300,
        relief=tk.RIDGE,  # 枠線を表示
        bd=2  # 枠線の幅
    )
    canvas.place(x=370, Y=0)

    img = tk.PhotoImage(file='img1.gif')
    canvas.create_image(
        0,
        0,
        image=img,
        anchor=tk.NW  # 配置の起点
    )

    # 応答エリアを作成
    response_area = tk.Label(
        root,  # 親要素をメインウィンドウに設定
        width=50,
        height=10,
        bg='yellow',
        font=font,
        relief=tk.RIDGE,
        bd=2
    )
    response_area.place(x=370, y=305)

    # フレームの作成

    frame = tk.Frame(
        root,
        relief=tk.RIDGE,
        borderwidth=4
    )

    # 入力ボックスの作成

    entry = tk.Entry(
        frame,
        width=70,
        font=font
    )
    entry.pack(side=tk.LEFT)
    entry.focus_set()
    # ボタンの作成
    button = tk.Button(
        frame,
        width=15,
        text='話す',
        command=talk()
    )
    button.pack(side=tk.LEFT)
    frame.place(x=30, y=520)

    # リストボックスを作成
    lb = tk.Listbox(
        root,
        width=42,
        height=30,
        font=font_log
    )

    # 縦のスクロールバー
    sb1 = tk.Scrollbar(
        root,
        orient=tk.VERTICAL,
        command=lb.yview()
    )

    # 横のスクロールバー

    sb2 = tk.Scrollbar(
        root,
        orient=tk.HORIZONTAL,
        command=lb.xview()
    )

    # リストボックスとスクロールバーを連動
    lb.configure(yscrollcommand=sb1.set())
    lb.configure(xscrollcommand=sb2.set())

    # grid()でリストボックス、スクロールバーを画面上に配置
    lb.grid(row=0, column=0)
    sb1.grid(row=0, column=1, sticky=tk.NS)
    sb2.grid(row=1, column=0, sticky=tk.EW)

    root.mainloop()

    # プログラムの開始

    if __name__ == '__main__':
        run()
