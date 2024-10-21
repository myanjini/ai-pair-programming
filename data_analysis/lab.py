# 아래 데이터의 전체 합계 금액을 구하서 출력하는 프로그램을 작성
# 사과 2000원, 수량 5개, 세율은 10%
# 라디오 2만 원, 수량 1, 세율 0.1
# 연필 삼천원,수량5,세율0.08

items = [
    {"name": "사과", "unit_price": 2000, "quantity": 5, "tax_rate": 0.1},
    {"name": "라디오", "unit_price": 20000, "quantity": 1, "tax_rate": 0.1},
    {"name": "연필", "unit_price": 3000, "quantity": 5, "tax_rate": 0.08}
]

total_price = 0

# 테이블 헤더 출력
print(f"{'품목':<10} {'단가':<10} {'수량':<10} {'세율':<10} {'합계 금액':<20}")

for item in items:
    # 각 항목의 총 금액을 계산 (단가 * 수량 * (1 + 세율))
    item_total = item["unit_price"] * item["quantity"] * (1 + item["tax_rate"])
    total_price += item_total
    # 각 항목의 정보를 테이블 형식으로 출력
    print(f"{item['name']:<10} {item['unit_price']:<10} {item['quantity']:<10} {item['tax_rate']:<10} {item_total:<20.2f}")

# 전체 합계 금액 출력
print(f"\n전체 합계 금액: {total_price:.2f} 원")
    item_total = item["unit_price"] * item["quantity"] * (1 + item["tax_rate"])
    total_price += item_total
    # 각 항목의 정보를 마크다운 테이블 형식으로 출력
    print(
        f"| {adjust_width(item['name'], 10)} | {adjust_width(f'{item['unit_price']:,}', 15, 'right')} | "
        f"{adjust_width(str(item['quantity']), 10, 'right')} | {adjust_width(f'{item['tax_rate']:.1%}', 10, 'right')} | "
        f"{adjust_width(f'{item_total:,.1f}', 20, 'right')} |"
    )

# 전체 합계 금액 출력
print(f"\n전체 합계 금액: {total_price:,.1f} 원")