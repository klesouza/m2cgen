List<double> score(List<double> input) {
    List<double> var0;
    if ((input[3]) <= (0.8)) {
        var0 = [1.0, 0.0, 0.0];
    } else {
        if ((input[2]) <= (4.8500004)) {
            var0 = [0.0, 0.9622641509433962, 0.03773584905660377];
        } else {
            if ((input[3]) <= (1.75)) {
                if ((input[3]) <= (1.6500001)) {
                    var0 = [0.0, 0.25, 0.75];
                } else {
                    var0 = [0.0, 1.0, 0.0];
                }
            } else {
                var0 = [0.0, 0.0, 1.0];
            }
        }
    }
    List<double> var1;
    if ((input[3]) <= (0.8)) {
        var1 = [1.0, 0.0, 0.0];
    } else {
        if ((input[0]) <= (6.1499996)) {
            if ((input[2]) <= (4.8500004)) {
                var1 = [0.0, 0.9090909090909091, 0.09090909090909091];
            } else {
                var1 = [0.0, 0.0, 1.0];
            }
        } else {
            if ((input[3]) <= (1.75)) {
                var1 = [0.0, 0.8666666666666667, 0.13333333333333333];
            } else {
                var1 = [0.0, 0.0, 1.0];
            }
        }
    }
    return mulVectorNumber(addVectors(var0, var1), 0.5);
}
List<double> addVectors(List<double> v1, List<double> v2) {
    List<double> result = new List<double>(v1.length);
    for (int i = 0; i < v1.length; i++) {
        result[i] = v1[i] + v2[i];
    }
    return result;
}
List<double> mulVectorNumber(List<double> v1, double num) {
    List<double> result = new List<double>(v1.length);
    for (int i = 0; i < v1.length; i++) {
        result[i] = v1[i] * num;
    }
    return result;
}
