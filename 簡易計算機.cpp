#include <iostream>
#include <cmath>

using namespace std;

// 函數聲明
float add(float a, float b);
float subtract(float a, float b);
float multiply(float a, float b);
float divide(float a, float b);
float power(float base, float exponent);

int main() {
    float num1, num2;
    char op;
    char continueChoice;

    do {
        // 提示輸入數字和運算符號
        cout << "\n輸入第一個數字: ";
        cin >> num1;

        cout << "\n輸入運算符號 (+, -, *, /, ^): ";
        cin >> op;

        if (op != '^') {
            cout << "\n輸入第二個數字: ";
            cin >> num2;
        } else {
            // 若是次方運算，輸入第二個數字即為指數
            cout << "\n輸入指數: ";
            cin >> num2;
        }

        // 計算結果
        switch (op) {
            case '+':
                cout << "\n結果: " << add(num1, num2) << endl;
                break;
            case '-':
                cout << "\n結果: " << subtract(num1, num2) << endl;
                break;
            case '*':
                cout << "\n結果: " << multiply(num1, num2) << endl;
                break;
            case '/':
                // 檢查除數是否為0
                if (num2 != 0) {
                    cout << "\n結果: " << divide(num1, num2) << endl;
                } else {
                    cout << "\n錯誤: 除數不能為0" << endl;
                }
                break;
            case '^':
                cout << "\n結果: " << power(num1, num2) << endl;
                break;
            default:
                cout << "\n錯誤: 不支持的運算符號" << endl;
                break;
        }

        // 詢問是否繼續
        cout << "\n繼續嗎？輸入 'Y' 繼續，'N' 結束: ";
        cin >> continueChoice;

    } while (continueChoice == 'y' || continueChoice == 'Y');

    return 0;
}

// 函數實現
float add(float a, float b) {
    return a + b;
}

float subtract(float a, float b) {
    return a - b;
}

float multiply(float a, float b) {
    return a * b;
}

float divide(float a, float b) {
    return a / b;
}

float power(float base, float exponent) {
    return pow(base, exponent);
}



