#include <iostream>
#include <vector>  // Include the vector header
#include <omp.h>   // Include the OpenMP header

using namespace std;

// Function to partition the array
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Function to implement parallel Quick Sort
void parallelQuickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        // Partition the array
        int pi = partition(arr, low, high);

        // Sort the left and right subarrays in parallel
        #pragma omp parallel sections
        {
            #pragma omp section
            parallelQuickSort(arr, low, pi - 1);

            #pragma omp section
            parallelQuickSort(arr, pi + 1, high);
        }
    }
}

int main() {
    vector<int> arr = {10, 80, 30, 90, 40, 50, 70};
    int n = arr.size();

    // Set the number of threads for parallel execution
    omp_set_num_threads(4);

    cout << "Original array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Perform parallel Quick Sort
    parallelQuickSort(arr, 0, n - 1);

    // Output the sorted array
    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
