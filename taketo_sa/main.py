import sys

# --- 商品データ（マスター） ---
PRODUCTS = [
    {"id": 1, "name": "リンゴ", "price": 150},
    {"id": 2, "name": "バナナ", "price": 100},
    {"id": 3, "name": "オレンジ", "price": 120},
]

# ★【新機能】アプリを起動してから今までの「全員の注文の累計金額」を保存する変数
TOTAL_SALES = 0


def show_products():
    """2. 商品一覧画面"""
    print("\n--- 商品一覧 ---")
    for p in PRODUCTS:
        print(f"ID: {p['id']} | {p['name']} - {p['price']}円")
    print("----------------")


def create_order():
    """3 & 4. 注文入力・確認画面（複数商品を連続で追加可能）"""
    global TOTAL_SALES  # 外側にある累計カウンターを書き換えるための設定
    cart = []

    while True:
        show_products()
        print(f"現在のカートの中身: {len(cart)}種類の商品が入っています")

        product_id_input = input(
            "購入したい商品のIDを入力してください (注文を終了して合計へ進む場合は 'q' ): "
        )

        if product_id_input.lower() == "q":
            if not cart:
                print("カートが空なのでメニューに戻ります。")
                return
            break

        if not product_id_input.isdigit():
            print("【エラー】数字または 'q' を入力してください。")
            continue
        product_id = int(product_id_input)

        product = None
        for p in PRODUCTS:
            if p["id"] == product_id:
                product = p
                break

        if product is None:
            print("【エラー】その商品IDは見つかりません。")
            continue

        quantity_input = input(f"「{product['name']}」の数量を入力してください: ")
        if not quantity_input.isdigit():
            print("【エラー】正しい数量（数字）を入力してください。")
            continue
        quantity = int(quantity_input)
        if quantity <= 0:
            print("【エラー】数量は1以上にしてください。")
            continue

        cart.append(
            {
                "name": product["name"],
                "price": product["price"],
                "quantity": quantity,
                "subtotal": product["price"] * quantity,
            }
        )
        print(f"🛒 カートに「{product['name']} × {quantity}個」を追加しました！\n")

        next_choice = input("さらに商品を追加しますか？ (y/n): ")
        if next_choice.lower() != "y":
            break

    # --- 4. 注文確認画面（今回の注文の合計） ---
    print("\n=== 📄 今回の注文内容 ===")
    current_total = 0  # 今回の注文だけの合計

    for item in cart:
        print(f"・{item['name']} × {item['quantity']}個 : {item['subtotal']}円")
        current_total += item["subtotal"]

    print("----------------------------")
    print(f"今回の小計: {current_total}円")
    print("==============================")

    # ★【新機能】今回の売上を、全体の累計金額に足し算する
    TOTAL_SALES += current_total
    print(f"📢 これまでの売上総額（累計）: {TOTAL_SALES}円")
    print("==============================")

    input("\n[Enter]キーを押すとメニューに戻ります...")


# ==========================================
# 1. メニュー画面（メインループ）
# ==========================================
def main():
    while True:
        print("\n=== メニュー ===")
        print("1. 商品一覧を表示")
        print("2. 商品を注文（連続追加・金額計算）")
        # ★ メニューの段階でも今の累計金額がチラ見えするようにしました
        print(f"3. 終了 (本日の総売上: {TOTAL_SALES}円)")
        print("================")

        choice = input("番号を選んでください (1-3): ")

        if choice == "1":
            show_products()
        elif choice == "2":
            create_order()
        elif choice == "3":
            print(
                f"\n本日の総売上高は【 {TOTAL_SALES}円 】でした！"
            )
            print("アプリを終了します。ありがとうございました！")
            sys.exit()
        else:
            print("【エラー】1から3の数字を選んでください。")


if __name__ == "__main__":
    main()
