#include <iostream>
#include <cmath>

using namespace std;

// ����n��
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
        // ���ܿ�J�Ʀr�M�B��Ÿ�
        cout << "\n��J�Ĥ@�ӼƦr: ";
        cin >> num1;

        cout << "\n��J�B��Ÿ� (+, -, *, /, ^): ";
        cin >> op;

        if (op != '^') {
            cout << "\n��J�ĤG�ӼƦr: ";
            cin >> num2;
        } else {
            // �Y�O����B��A��J�ĤG�ӼƦr�Y������
            cout << "\n��J����: ";
            cin >> num2;
        }

        // �p�⵲�G
        switch (op) {
            case '+':
                cout << "\n���G: " << add(num1, num2) << endl;
                break;
            case '-':
                cout << "\n���G: " << subtract(num1, num2) << endl;
                break;
            case '*':
                cout << "\n���G: " << multiply(num1, num2) << endl;
                break;
            case '/':
                // �ˬd���ƬO�_��0
                if (num2 != 0) {
                    cout << "\n���G: " << divide(num1, num2) << endl;
                } else {
                    cout << "\n���~: ���Ƥ��ର0" << endl;
                }
                break;
            case '^':
                cout << "\n���G: " << power(num1, num2) << endl;
                break;
            default:
                cout << "\n���~: ��������B��Ÿ�" << endl;
                break;
        }

        // �߰ݬO�_�~��
        cout << "\n�~��ܡH��J 'Y' �~��A'N' ����: ";
        cin >> continueChoice;

    } while (continueChoice == 'y' || continueChoice == 'Y');

    return 0;
}

// ��ƹ�{
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



