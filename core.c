void add_arrays(int size, double *a, double *b, double *c){
    for (int i = 0; i < size; ++i){
        c[i] = a[i] + b[i];
    }
}
