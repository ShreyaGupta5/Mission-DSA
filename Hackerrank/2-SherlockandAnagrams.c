#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void sortString(char *str) {
    int n = strlen(str);
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (str[i] > str[j]) {
                char temp = str[i];
                str[i] = str[j];
                str[j] = temp;
            }
        }
    }
}

int sherlockAndAnagrams(char *s) {
    int n = strlen(s);
    int anagramPairs = 0;

    char **signatures = (char **)malloc(sizeof(char *) * (n * (n + 1) / 2));
    int signatureCount = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int len = j - i + 1;
            char *sub = (char *)malloc(sizeof(char) * (len + 1));
            strncpy(sub, s + i, len);
            sub[len] = '\0';
            sortString(sub);
            signatures[signatureCount++] = sub;
        }
    }

    for (int i = 0; i < signatureCount; i++) {
        for (int j = i + 1; j < signatureCount; j++) {
            if (strcmp(signatures[i], signatures[j]) == 0) {
                anagramPairs++;
            }
        }
    }

    for (int i = 0; i < signatureCount; i++) {
        free(signatures[i]);
    }
    free(signatures);

    return anagramPairs;
}

int main() {
    int q;
    scanf("%d", &q);
    while (q--) {
        char s[101];
        scanf("%s", s);
        int result = sherlockAndAnagrams(s);
        printf("%d\n", result);
    }
    return 0;
}
