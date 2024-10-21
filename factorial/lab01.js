function factorial(n) {
    if (n < 0) {
        return null; // 팩토리얼은 음수에 대해 정의되지 않음
    }
    if (n === 0) {
        return 1; // 0의 팩토리얼은 1
    }
    return n * factorial(n - 1); // 재귀 호출을 통해 팩토리얼 계산
}

module.exports = { factorial };
